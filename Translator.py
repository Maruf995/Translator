from translate import Translator
while True:
    languageName=input('На какой язык вы хотите перевести?: ')
    transalat=input('Что вы хотите перевести?: ')
    translator = Translator(to_lang=languageName)
    translation = translator.translate(transalat)
    print(translation)