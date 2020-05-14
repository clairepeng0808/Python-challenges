from translate import Translator

translator = Translator(to_lang="zh")

try:
    with open('./original.txt', 'r') as original:
        translation = translator.translate(original.read())
        print(translation)
        with open('./translation_zh.txt', 'w') as translation_zh:
            translation_zh.write(translation)

except FileNotFoundError:
    print('Check your file directory!')
