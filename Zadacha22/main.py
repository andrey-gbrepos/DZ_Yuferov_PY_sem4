# Задача 22: Даны два неупорядоченных набора целых чисел 
# (может быть, с повторениями). Выдать без повторений в 
# порядке возрастания все те числа, которые встречаются 
# в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов 
# первого множества. m — кол-во элементов второго 
# множества. Затем пользователь вводит сами элементы множеств.

import random

print('\n''Программа выведет, в порядке возрастания, все числа, встречающиеся в двух множествах, без повторений.')
print('(Размер множеств определяет пользователь. Набор множеств формируется по случайному закону.)''\n')

n = int(input("Введите количество элементов 1-го множества: "))
m = int(input("Введите количество элементов 2-го множества: "))
n_list = []
m_list = []
MIN = 0
MAX = 50

for i in range(n):
    n_list.append(random.randint(MIN, MAX)) 
print("1-е множество: ",*n_list)
for i in range(m):
    m_list.append(random.randint(MIN, MAX))
print("2-е множество: ", *m_list)

result = list(set(n_list).intersection(set(m_list))) # Формирование множества -> списка
result.sort()

print('\n','Результат: ',*result, '\n')