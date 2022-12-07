def printExpectation():
    printAct = int(input('Желаете распечатать документ?\n'
                           '1 - Да\n'
                           '2 - Нет\n'))
    if printAct == 1:
        chooseInformation()


def chooseInformation():
    chooseAct = int(input('Какой документ хотите распечатать?\n'
                           '1 - Классический реферат\n'
                           '2 - Реферат в виде списка ключевых слов\n'
                           '3 - Назад\n'))
    if chooseAct == 1:
        printClassicDocument()
    elif chooseAct == 2:
        printListDocument()
    elif chooseAct == 3:
        print('')
        printExpectation()


def printClassicDocument():
    print('В разработке')

def printListDocument():
    print('В разработке')