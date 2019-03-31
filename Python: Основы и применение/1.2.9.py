# Реализуйте программу, которая будет вычислять количество различных объектов в списке.
# Два объекта a и b считаются различными, если a is b равно False.
#
# Вашей программе доступна переменная с названием objects,
# которая ссылается на список, содержащий не более 100 объектов.
# Выведите количество различных объектов в этом списке.
#
# Формат ожидаемой программы:
#
# ans = 0
# for obj in objects: # доступная переменная objects
#     ans += 1
#
# print(ans)
#
# Примечание:
# Количеством различных объектов называется максимальный размер множества объектов,
# в котором любые два объекта являются различными.
#
# Рассмотрим пример:
# objects = [1, 2, 1, 2, 3] # будем считать, что одинаковые числа соответствуют одинаковым объектам,
# а различные – различным
#
# Тогда все различные объекты являют собой множество {1, 2, 3}﻿.
# Таким образом, количество различных объектов равно трём.

objects = [1, 2, 3, 4, 5, 1, 2]
list_different_numbers = []
for different_number in objects:
    if different_number not in list_different_numbers:
        list_different_numbers.append(different_number)
print(len(list_different_numbers))
