# Паша очень любит кататься на общественном транспорте,
# а получая билет, сразу проверяет,
# счастливый ли ему попался.
# Билет считается счастливым, если сумма первых трех цифр совпадает с суммой последних трех цифр номера билета.
#
# Однако Паша очень плохо считает в уме, поэтому попросил вас написать программу,
# которая проверит равенство сумм и выведет "Счастливый",
# если суммы совпадают, и "Обычный", если суммы различны.
#
# На вход программе подаётся строка из шести цифр.
#
# Выводить нужно только слово "Счастливый" или "Обычный",
# с большой буквы.

x = str(input())
val = (int(x[0]) + int(x[1]) + int(x[2]))
val2 = (int(x[3]) + int(x[4]) + int(x[5]))

if (val == val2):
    print("Счастливый")
else:
    print("Обычный")
