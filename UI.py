from methods import classicDocument, listDocument
import sys


def chooseMethod():
    chooseAct = int(input('Выберите вид реферата:\n'
                    '1 - Классический реферат\n'
                    '2 - Реферат в виде списка ключевых слов\n'
                    '3 - Выход\n'))
    if chooseAct == 1:
        classicDocument()
    elif chooseAct == 2:
        listDocument()
    elif chooseAct == 3:
        print('До новых встреч!')
        sys.exit()


def expectation():
    while True:
        act = int(input('Желаете продолжить?\n'
                        '1 - Да\n'
                        '2 - Нет\n'))
        if act == 1:
            chooseMethod()
        elif act == 2:
            print('До новых встреч!')
            break