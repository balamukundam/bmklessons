
class EngToTelugu:

    _curLang = 0
    

    def getStringInTranscript(self, str1):
        str2 = self._findandReplaceAnuswaras(str1)
        str2 = self._findandReplaceChars(str2)

        str2 = str2.replace('A', 'ā').replace('I', 'ī').replace('U', 'ū').replace('R', 'r̥').replace('F', 'r̥̄').replace('z', 'l̥').replace('Z', 'l̥̄').replace('E', 'ē').replace('Y', 'ai').replace('O', 'ō').replace('W', 'au').replace('M', 'ṃ').replace('Ĥ', 'ḥ').replace('K', 'kh').replace('G', 'gh').replace('Á', 'ṅ').replace('C', 'ch').replace('J', 'jh').replace('Ñ', 'ñ').replace('T', 'ṭ').replace('Ŧ', 'ṭh').replace('D', 'ḍ').replace('Ð', 'ḍh').replace('N', 'ṇ').replace('ť', 'th').replace('đ', 'dh').replace('f', 'P').replace('P', 'ph').replace('B', 'bh').replace('w', 'v').replace('S', 'ś').replace('Ś', 'ṣ').replace('L', 'ḷ').replace('Ŕ', 'ṟ').replace('H', 'h')
        str2 = str2.replace('^', '').replace('x', '').replace('X', '').replace('q', '').replace('Q', '').replace('V', '')
        return str2
    
    def getStringInTelugu(self, str1):
        self._curLang = 0
        return self._convertToTeluguAll(str1)
    
    def getStringInSanskrit(self, str1):
        self._curLang = 1
        str2 = self._findandReplaceAnuswaras(str1)
        str2 = self._convertToTeluguAll(str1).replace(chr(3133), 'ऽ').replace(chr(3075), 'ः')
        return str2

    def _convertToTeluguAll(self, str1):
        str1 = '£' + str1
        sRetString  = ''
        telugu_arr = str1.split('`')
        bConvert = True
        for i in range(len(telugu_arr)):
            if len(telugu_arr[i]) > 0:
                if bConvert:
                    sRetString += self._get_telugu_string(telugu_arr[i])
                else:
                    sRetString += telugu_arr[i]

            bConvert = not bConvert

        return sRetString[1:]
    

    def _findandReplaceChars(self, str1):
        return str1.replace( 'aa', 'A').replace( 'ee', 'I').replace( 'ii', 'I').replace( 'uu', 'U').replace( 'oo', 'U').replace( 'Ru', 'F').replace( 'zu', 'Z').replace( 'ea', 'E').replace( 'ai', 'Y').replace( 'oe', 'O').replace( 'ou', 'W').replace( 'au', 'W').replace( '@h', 'Ĥ').replace( 'kh', 'K').replace( 'gh', 'G').replace( '~m', 'Á').replace( 'ch', 'c').replace( '~c', 'Ç').replace( 'Ch', 'C').replace( '~j', 'Ĵ').replace( '~n', 'Ñ').replace( 'Th', 'Ŧ').replace( 'Dh', 'Ð').replace( 'th', 'ť').replace( 'dh', 'đ').replace( 'f', 'P').replace( 'ph', 'P').replace( 'bh', 'B').replace( 'w', 'v').replace( 'sh', 'Ś').replace( 'lh', 'L').replace( '~r', 'Ŕ').replace( 'h', 'H')

    def _findandReplaceAnuswaras(self, str1):
        return str1.replace('Mk', 'Ák').replace('MK', 'ÁK').replace('Mg', 'Ág').replace('MG', 'ÁG').replace('Mc', 'Ñc').replace('MC', 'ÑC').replace('Mj', 'Ñj').replace('MJ', 'ÑJ').replace('MT', 'NT').replace('MD', 'ND').replace('Mt', 'nt').replace('Md', 'nd').replace('Mp', 'mp').replace('Mb', 'mb')
        

    def _get_telugu_string(self, str1):
        str1 = self._findandReplaceChars(str1)
        telugu_arr = list(str1)
        teluguWord = ''
        sTempWord = ''
        for i in range(len(telugu_arr)):
            if self._is_TeluguChar(telugu_arr[i]):
                sTempWord += telugu_arr[i]
            
            else:
                if sTempWord != '':
                    teluguLetters = self._split_on_achulu(sTempWord)
                    for j in range(len(teluguLetters)):
                        teluguWord += self._get_telugu_letter(teluguLetters[j])
                sTempWord = ''
                teluguWord += telugu_arr[i]
        
        teluguLetters = self._split_on_achulu(sTempWord)

        for j in range(len(teluguLetters)):
            teluguWord += self._get_telugu_letter(teluguLetters[j])

        return teluguWord
    

    def _get_telugu_letter(self, str1):
        str_return = ''
        if str1 == '':
            return str_return    

        if len(str1) == 1:
            if self._is_ach(str1):
                return self._get_pure_ach(str1)
            
        ltrs_arr = list(str1)
        if not self._is_achForHal(ltrs_arr[len(ltrs_arr)-1]):
            ltrs_arr.append('^')

        for i in range(len(ltrs_arr)-1):
            if i > 0:
                i_nmbr_join_hallu = 3149
                if self._curLang == 1:
                    i_nmbr_join_hallu = 2381
                str_return += chr(i_nmbr_join_hallu)

            str_return += self._get_hallu(ltrs_arr[i])

        if ltrs_arr[len(ltrs_arr)-1] != 'a':
            str_return += self._get_achForHallu(ltrs_arr[len(ltrs_arr)-1])

        return str_return


    def _is_TeluguChar(self, str1):
        telugu_chars = ['a', 'A', 'i', 'I', 'u', 'U', 'R', 'F', 'z', 'Z', 'e', 'E', 'Y', 'o', 'O', 'W', 'M', 'Ĥ', 'k', 'K', 'g', 'G', 'Á', 'c', 'Ç', 'C', 'j', 'Ĵ', 'J', 'Ñ', 'T', 'Ŧ', 'D', 'Ð', 'N', 't', 'ť', 'd', 'đ', 'n', 'p', 'P', 'b', 'B', 'm', 'y', 'r', 'l', 'v', 'S', 'Ś', 's', 'H', 'L', 'Ŕ', '^', 'x', 'X', 'q', 'Q', 'V']
        return str1 in telugu_chars
    
    def _is_ach(self, str1):
        telugu_achchus = ['a', 'A', 'i', 'I', 'u', 'U', 'R', 'F', 'z', 'Z', 'e', 'E', 'Y', 'o', 'O', 'W', 'M', 'Ĥ', 'x', 'X', 'q', 'Q', 'V']
        return str1 in telugu_achchus
    
    def _is_achForHal(self, str1):
        telugu_achchus = ['a', 'A', 'i', 'I', 'u', 'U', 'R', 'F', 'z', 'Z', 'e', 'E', 'Y', 'o', 'O', 'W', '^']
        return str1 in telugu_achchus
    
    def _get_pure_ach(self, str1):
        telugu_achchus = ['a', 'A', 'i', 'I', 'u', 'U', 'R', 'F', 'z', 'Z', 'e', 'E', 'Y', 'o', 'O', 'W', 'M', 'Ĥ', 'x', 'X', 'q', 'Q', 'V']
        achu_nbrs = [3077, 3078, 3079, 3080, 3081, 3082, 3083, 3168, 3084, 3169, 3086, 3087, 3088, 3090, 3091, 3092, 3074, 3075, 3073, 3133, 2386, 2385, 7386]
        if self._curLang == 1:
            achu_nbrs = [2309, 2310, 2311, 2312, 2313, 2314, 2315, 2400, 2316, 2401, 2318, 2319, 2320, 2322, 2323, 2324, 2306, 3075, 3073, 3133, 2386, 2385, 7386]
        return chr(achu_nbrs[telugu_achchus.index(str1)])
    
    def _get_achForHallu(self, str1):
        telugu_achchus = ['A', 'i', 'I', 'u', 'U', 'R', 'F', 'z', 'Z', 'e', 'E', 'Y', 'o', 'O', 'W', '^']
        achu_nbrs = [3134, 3135, 3136, 3137, 3138, 3139, 3140, 3170, 3171, 3142, 3143, 3144, 3146, 3147, 3148, 3149]
        nbrCorrect = 0
        if self._curLang == 1:
            nbrCorrect =-768
        extr_string = ''
        if str1 == '^':
            extr_string = chr(8204)
        return chr(achu_nbrs[telugu_achchus.index(str1)]+nbrCorrect) + extr_string
    
    def _get_hallu(self, str1):
        telugu_hallus = ['k', 'K', 'g', 'G', 'Á', 'c', 'Ç', 'C', 'j', 'Ĵ', 'J', 'Ñ', 'T', 'Ŧ', 'D', 'Ð', 'N', 't', 'ť', 'd', 'đ', 'n', 'p', 'P', 'b', 'B', 'm', 'y', 'r', 'l', 'v', 'S', 'Ś', 's', 'H', 'L', 'Ŕ']
        hallu_nbrs = [3093, 3094, 3095, 3096, 3097, 3098, 3160, 3099, 3100, 3161, 3101, 3102, 3103, 3104, 3105, 3106, 3107, 3108, 3109, 3110, 3111, 3112, 3114, 3115, 3116, 3117, 3118, 3119, 3120, 3122, 3125, 3126, 3127, 3128, 3129, 3123, 3121]
        nbrCorrect = 0
        if self._curLang == 1:
            nbrCorrect =-768
        return chr(hallu_nbrs[telugu_hallus.index(str1)]+nbrCorrect)
    
    def _split_on_achulu(self, str1):
        str2 = str1.replace('a', 'a ').replace('A', 'A ').replace('i', 'i ').replace('I', 'I ').replace('u', 'u ').replace('U', 'U ').replace('R', 'R ').replace('F', 'F ').replace('z', 'z ').replace('Z', 'Z ').replace('e', 'e ').replace('E', 'E ').replace('Y', 'Y ').replace('o', 'o ').replace('O', 'O ').replace('W', 'W ').replace('^', '^ ').replace('M', 'M ').replace('Ĥ', 'Ĥ ').replace('x', 'x ').replace('X', 'X ').replace('q', 'q ').replace('Q', 'Q ').replace('V', 'V ')
        return str2.split(' ')
    
    def getLekhini(self, str1):
        return str1.lower().replace('ā', 'A').replace('ī', 'I').replace('ū', 'U').replace('r̥', 'R').replace('r̥̄', 'F').replace('l̥', 'z').replace('l̥̄', 'Z').replace('ē', 'E').replace('ō', 'O').replace('ṁ', 'M').replace('ṃ', 'M').replace('ḥ', '@h').replace('ṅ', '~m').replace('ch', 'C').replace('jh', 'J').replace('ñ', '~n').replace('ṭ', 'T').replace('ṭh', 'Th').replace('D', 'D').replace('Ð', 'Dh').replace('ṇ', 'N', ).replace('ś', 'S', ).replace('ṣ', 'sh', ).replace('ḷ', 'lh', ).replace('ṟ', '~r', )



