import pandas as pd
import numpy as np
from sys import argv
import histogram as h

prompt = '---> '


def start_input():
    # создаем пустой массив
    A = []
    # пробуем считать несколько первых чисел до появления нуля
    a = input("Введите положительное натуральное число " + prompt)  # считываем первое значение
    # TODO запустить диагностику проблемы с выводом соответсвующей ошибкой
    while (int(a) > 0):  # запускаем цикл на считывание данных пока положительное. Может вылезти ошибка
        A.append(int(a))
        a = input(prompt)  # повторение считывания и записи

    return A


def initial_list():
    A = list([2, 4, 5, 7, 8, 10, 12, 13, 14, 16, 17, 19])
    return A


def read_txt_file(filename):
    txt = open(filename)
    data = txt.read()
    txt.close()
    A = list(map(int, data.split(sep=',')))  # перевод list(string) -> list(int)
    return A


def read_csv_file(filename):
    csv = pd.read_csv(filename, sep=";")
    A = np.array(csv["array"])
    return A


def prob_dis(A):  # специальная функция для построения массива при неравновероятном исходе
    for i in range(len(A)):
        A[i] = i * A[i] * len(A)
    return A


def stat_array(A):
    # Выводим информацию о массиве
    A.sort()  # встроенная функция в листы
    print("В массиве содержится следующие элементы  ---> {}\nРазмер массива равен  ---> {}".format(A, len(A)))
    print("Максимальное значение в массиве равно  ---> {}".format(A[-1]))
    print("Минимальное значение в массиве равно  ---> {}".format(A[0]))
    h.hist(A)
    # создаем новый массив в виде нампи-массива для более глубокой работы
    A = np.array(A)

    # используем функции нампи
    print("Среднее значение в массиве равно  ---> {0:.2f}".format(A.mean()))
    print("Стандартное отклонение в массиве равно  ---> {0:.2f}".format(A.std()))
    print("Значение первого квартиля в массиве равно  ---> {}".format(np.quantile(A, 0.25)))
    print("Значение второго квартиля в массиве равно  ---> {}".format(np.quantile(A, 0.5)))
    print("Значение третьего квартиля в массиве равно  ---> {}".format(np.quantile(A, 0.75)))

