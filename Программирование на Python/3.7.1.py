# Напишите программу, которая принимает на стандартный вход
# список игр футбольных команд с результатом матча и выводит
# на стандартный вывод сводную таблицу результатов всех матчей.
#
# За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
#
# Формат ввода следующий:
# В первой строке указано целое число 𝑛 — количество завершенных игр.
# После этого идет 𝑛 строк, в которых записаны результаты игры в следующем формате:
# Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой
#
# Вывод программы необходимо оформить следующим образом:
# Команда:Всего_игр Побед Ничьих Поражений Всего_очков
#
# Конкретный пример ввода-вывода приведён ниже.
#
# Порядок вывода команд произвольный.

games = int(input())


def best_function(command_name):
    count_games = 0
    count_wins = 0
    count_draw = 0
    count_lose = 0
    all_points = 0
    for i in range(games):
        if (a == command_name):
            count_games += 1
            if (b > d):
                count_wins += 1
                all_points += 3
            elif (b == d):
                count_draw += 1
                all_points += 1
            else:
                count_lose += 1
        elif (c == command_name):
            count_games += 1
            if (b < d):
                count_wins += 1
                all_points += 3
            elif (b == d):
                count_draw += 1
                all_points += 1
            else:
                count_lose += 1
    return print(
        command_name + " " + str(count_games) + " " + str(count_wins) + " " + str(count_draw) + " " + str(all_points))


for i in range(games):
    a, b, c, d = (x for x in input().split(';'))
best_function('Зенит')
best_function('Спартак')
best_function('ЦСКА')
