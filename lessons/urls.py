from django.urls import path
#from . import views
from .views import IndexView, LessonView

urlpatterns = [
    #path('', views.index, name='index'),
    path('', IndexView.as_view(), name='index'),
    path('detail/<int:pk>', LessonView.as_view(), name='detail'),
]