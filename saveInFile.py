def SaveFile(result,type):
    actSave = int(input('Желаете сохранить результат?\n'
                    '1 - Да\n'
                    '2 - Нет\n'))
    if actSave == 1:
        if type == 1:
            file = open("results/result1.txt", "w")
            file.write(str(result))
            print(str(result))
            file.close()
        elif type == 2:
            file = open("results/result2.txt", "w")
            file.write(str(result))
            file.close()
