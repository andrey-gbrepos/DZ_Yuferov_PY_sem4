# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой 
# грядке, причём кусты высажены только по окружности. Таким образом, у каждого куста 
# есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло 
# различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта 
# система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий 
# модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может 
# собрать за один заход собирающий модуль, находясь перед некоторым кустом 
# заданной во входном файле грядки.

import random

print('\n''Программа определяет и выводит максимльную сумму (3-х) рядом стоящих элементов закольцованного списка.')
print('(Количество элементов определяет пользователь. Набор элементов формируется по случайному закону.)''\n')

QUAN = 3 # Количество суммируемых элементов
MIN = 1
MAX = 10

q = int(input("Введите количество элементов: "))
if q < QUAN: 
    print("Невозможно посчитать сумму ", QUAN, " элементов" )
else:
    q_list = []

    for i in range(q):                          # Заполнение списка
        q_list.append(random.randint(MIN, MAX)) 
    print("Полученный набор: ",*q_list)
    
    max_sum = 0
    temp_sum = 0
    id_kusta = 0
    
    for i in range(q):             
        for j in range(QUAN):
            temp_sum += q_list[(i+j)%q]   
        if max_sum < temp_sum: 
            max_sum = temp_sum
            id_kusta = (i%q+2)%q
        temp_sum = 0
    print('Номер (с 1-цы) центрального куста: ', id_kusta) 
    print('Максимальная сумма: ', max_sum, '\n')     
