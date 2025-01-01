from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Lesson, Book, Category
from lessons.utils.engtotelugu import EngToTelugu

# Create your views here.

# def index(request):

#     ett = EngToTelugu()

#     lessons =  Lesson.objects.all()
#     return render(request, 'lessons/index.html', {
#         'lesson': l
#     })

class IndexView(ListView):
    model = Lesson
    template_name = 'lessons/index.html'

    def get_context_data(self, **kwargs):        
        context = super().get_context_data(**kwargs)
        properties_to_display = ['book__category__name', 'book__book_name', 'lesson_number', 'title', 'id']
        queryset = Lesson.objects.all().select_related('related_model').values(*properties_to_display)
        context['object_list'] = queryset
        return context
    
class LessonView(DetailView):
    model = Lesson
    template_name = 'lessons/detail.html'
    ett = EngToTelugu()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object = context['object']
        jsondata = object.get_json_data()
        jsondata['TitleT'] = self.ett.getStringInTelugu(jsondata['TitleT'])

        blogs=[]
        iLeft = False
        count = 0
        for blog in jsondata["Blogs"]:
            lines=[]
            if not blog["image"] =="" :
                iLeft = not iLeft
                blog["left"] = iLeft
            for line in blog["lines"]:
                count += 1
                line = str(count) + ". " + self.ett.getStringInTelugu(line)
                lines.append(line)
            blog['lines'] = lines
            blogs.append(blog)

        count = 0
        questions = []
        for question in jsondata["Questions"]:
            count += 1
            questions.append(str(count) + ". " + question)

        jsondata['Blogs'] = blogs
        jsondata['Questions'] = questions
        object.json_data = jsondata

        context['object'] = object
        return context




