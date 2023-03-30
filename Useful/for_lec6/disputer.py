# Приложение-спорщик
import random


words = ("Ты сам-то понял, что написал", "Аргументируй", "И?")

phrase = input('Ваш вопрос: ')
while phrase != 'stop':
    print(random.choice(words))
    phrase = input('Ваш вопрос: ')
print("Был рад вам помочь!")
