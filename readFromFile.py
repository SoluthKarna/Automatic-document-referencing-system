import os


def LoadFile():
    dirName = os.path.abspath("texts/")
    files = os.listdir("texts/")
    string = ''.join(files)
    file = (dirName + '/' + string)
   # print(file)
    return file


def readFromFile():
    file = open(LoadFile(),  encoding='utf-8')
    content = file.read()
    #print(content)
    return content
