import re
import nltk.data
import math
import pymorphy2
import collections
import string
import operator

from nltk import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

from printDocumets import printExpectation
from readFromFile import readFromFile
from saveInFile import SaveFile


def classicDocument():
    #result = 'В разработке!'
    #print(result)
    text = readFromFile()
    sentences_original = sent_tokenize(text)
    s = text.strip('\t\n')
    words_chopped = word_tokenize(s.lower())
    sentences_chopped = sent_tokenize(s.lower())
    stop_words = set(stopwords.words("english"))
    punc = set(string.punctuation)
    filtered_words = []
    for w in words_chopped:
        if w not in stop_words and w not in punc:
            filtered_words.append(w)
    total_words = len(filtered_words)
    # Определение частоты каждого отфильтрованного слова
    word_frequency = {}
    output_sentence = []
    for w in filtered_words:
        if w in word_frequency.keys():
            word_frequency[w] += 1.0
        else:
            word_frequency[w] = 1.0
    # Присвоение весов каждому слову в соответствии с частотой и общим количеством слов
    for word in word_frequency:
        word_frequency[word] = (word_frequency[word] / total_words)
    tracker = [0.0] * len(sentences_original)
    for i in range(0, len(sentences_original)):
        for j in word_frequency:
            if j in sentences_original[i]:
                tracker[i] += word_frequency[j]

    # Получение предложений с наибольшим весом
    for i in range(0, len(tracker)):
        # Извлечение индекса с наибольшей взвешенной частотой из трекера
        index, value = max(enumerate(tracker), key=operator.itemgetter(1))
        if (len(output_sentence) + 1 <= 10) and (sentences_original[index] not in output_sentence):
            output_sentence.append(sentences_original[index])
        tracker.remove(tracker[index])

    sorted_output_sent = sort_sentences(sentences_original, output_sentence)
    save_return = ""
    for output in sorted_output_sent:
        result = output
        print(result)
        save_return += result
    SaveFile(save_return, 2)
    printExpectation()

 #Сортировка в том порядке, как было в исходном тексте
def sort_sentences(original, output):
    sorted_sent_arr = []
    sorted_output = []
    for i in range(0, len(output)):
        if output[i] in original:
            sorted_sent_arr.append(original.index(output[i]))
    sorted_sent_arr = sorted(sorted_sent_arr)

    for i in range(0, len(sorted_sent_arr)):
        sorted_output.append(original[sorted_sent_arr[i]])
    return sorted_output


def listDocument():
    # инициализируем словарь
    dict = {}
    # читаем файл и делим на слова
    words = readFromFile().split()
    # инициализируем счётчик
    counter = 0
    # создаём анализатор
    morph = pymorphy2.MorphAnalyzer()
    # подсчитываем количество вхождений именно лексемы в текст
    counted_lexemes = count_lexemes(words)
    # идём по каждому слову в тексте
    for word in words:
        # очищаем слово от сех символов, не относящихся к алфавиту
        word = re.sub('(\W|[0-9])', '', word)
        # если после очистки длина слова 2 и меньше символа, то идём дальше, т.к. скорее всего это был знак припинания,
        # или просто местоимение/предлог, сдвигаем счётчик и идём дальше
        if len(word) > 2:
            # парсим слово анализатором
            word_morph = morph.parse(word)[0]
            # достаём лексему
            lexeme = word_morph.normal_form
            # если эта лексема встречается в тексте больше 10 раз, начинаем извлечение словосочетания (пары слов)
            # если нет, сдвигаем счётчик и идём дальше
            if counted_lexemes.get(lexeme, 0) > 10:
                # если эта лексема  не в словаре, добавляем и инициализируем пустым списком
                if lexeme not in dict.keys():
                    dict[lexeme] = []
                try:
                    next_word = None
                    # переменная для отслеживания текущего положения за счётчиком counter
                    wrong_word_type_counter = 0
                    # проверяем последующие слова на знаки припинания и всё, что меньше 2-х символов. Всё, что меньше 2-х
                    # скипаем до следующего слова
                    while True:
                        wrong_word_type_counter = wrong_word_type_counter + 1
                        next_word = words[counter + wrong_word_type_counter]
                        next_word = re.sub('(\W|[0-9])', '', next_word)
                        if len(next_word) > 2:
                            break
                    # если следующее слово не копия текущего, добавляем это словосочетание в список лексемы
                    if next_word is not word:
                        dict[lexeme].append(word + ' ' + next_word)
                    # сдвигаем счётчик на следующее слово
                    counter = counter + 1
                # Если падает IndexError, значит мы вышли за границы текста и прошли его конец.
                except IndexError:
                    # text end
                    pass
            else:
                counter = counter + 1
        else:
            counter = counter + 1
    # выводим в консоль то, что получилось
    save_result = ""
    for key, value in dict.items():
        if len(value) > 0:
            result = key + ' -> ' + str(value)
            print(result)
            save_result += result + "\n"
    SaveFile(save_result, 1)


    printExpectation()

def count_lexemes(words):
    counter = {}
    morph = pymorphy2.MorphAnalyzer()
    for word in words:
        temp = re.sub('(\W|[0-9])', '', word)
        if len(temp) > 2:
            lexeme = morph.parse(temp)[0].normal_form
            counter[lexeme] = counter.get(lexeme, 0) + 1
    return counter
