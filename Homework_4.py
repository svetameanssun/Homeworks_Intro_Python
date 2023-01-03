
# Домашнее задание Семинар 4
#---------------------------------------------------------------------------------
# Задача 22:
#---------------------------------------------------------------------------------
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа.
# n - кол-во элементов первого набора.
# m - кол-во элементов второго набора.
# Значения генерируются случайным образом.

# Input: 11 6
# (значения сгенерированы случайным образом
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18)

# Output: 11 6
# 6 12

# import random
# n = int(input('Introduce n: '))
# m = int(input('Introduce m: '))
# list_n = []
# list_m = []
# for i in range(n):
#     random_num = round(random.randint(1,n+1))
#     list_n.append(random_num)
# print(list_n)

# for i in range(m):
#     random_num = round(random.randint(1,m+1))
#     list_m.append(random_num)
# print(list_m)

# list_l = []
# for i in range(0,len(list_n)):
#     for j in range(0,len(list_m)):
#         if list_n[i] == list_m[j]:
#             list_l.append(list_m[j])
#             j+=1
#     i+=1
# # 12, 11, 1, 5
# # 0   1   2  3 
# # i

# # 1, 4, 55, 5, 12, 11
# # 0, 1,  2, 3,  4,  5
# # j

# # print(list_l)

# set_l = set(list_l)
# print(f'result: {set_l}')





#---------------------------------------------------------------------------------
# Задача 24:
#---------------------------------------------------------------------------------
# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке,
# причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних.
# Всего на грядке растет N кустов. Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.

# Напишите программу для нахождения максимального числа ягод,
# которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

# Input: 4
# (значения сгенерированы случайным образом
# 4 2 3 1 )

# Output: 9
# Домашнее задание Семинар 5* (сдавать только к семинару 5!)

# n = int(input("Введите кол-во кустов: "))
# array = []
# for i in range(n):
#     array.append(int(input('Введите кол-во ягод на кусте: ')))
# print(array)

# result = []

# for i in range(n):
#     result.append(array[i] + array[i-1] + array[i-2])
#     print(f'{array[i]} + {array[i-1]} + {array[i-2]} = {result[i]}')
# print(result)

# max_value = -1
# for i in result:
#     if i > max_value:
#         max_value = i
# print(f'Максимальное число ягод, которое может собрать \nза один заход собирающий модуль: {max_value}')



    

#---------------------------------------------------------------------------------
# Задача 26:
#---------------------------------------------------------------------------------
# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

# a = int(input('Introduce a: '))# m
# b = int(input('Input b: ')) # n
# # m = число
# # n = степень
# def kvadrat(m,n):
#     if n == 1:
#         return m
#     else:
#         return m * kvadrat(m,n-1)

# print(kvadrat(a,b))


        

#---------------------------------------------------------------------------------
# Задача 28:
#---------------------------------------------------------------------------------
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# a = int(input('Introduce a: '))# m
# b = int(input('Input b: ')) # n
# coll = [a,b]
# summa = sum(coll)

# print(summa)

# # summa2 = sum(coll,55) # Это к сумме элементов коллекции прибавляет еще 55
# # print(summa2)
