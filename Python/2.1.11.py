# Напишите программу, которая считывает со стандартного ввода целые числа,
# по одному числу в строке, и после первого введенного нуля выводит сумму полученных на вход чисел.

x = None
res = 0
while (x != 0):
    x = int(input())
    res += x
else:
    print(res)