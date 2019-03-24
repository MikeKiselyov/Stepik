# Напишите программу, которая принимает на вход список чисел
# в одной строке и выводит на экран в одну строку значения,
# которые повторяются в нём более одного раза.
#
# Для решения задачи может пригодиться метод sort списка.
#
# Выводимые числа не должны повторяться, порядок их вывода может быть произвольным.

a = [i for i in input().split()]
lenght_list = len(a)
sorted_list = sorted(a)
valera = ['']
super_list = ['']
for i in range(int(lenght_list) - 1):
    if (sorted_list[i] == sorted_list[i + 1]):
        if (sorted_list[i] not in valera):
            valera.append(sorted_list[i])
print(' '.join(valera))
