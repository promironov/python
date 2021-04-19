proceeds = float(input('Введите выручку'))
costs = float(input('Введите издежрки'))
profit = proceeds - costs
if profit > 0:
    print(f'Финансовый результат - прибыль {"%.2f" % profit}')
    if proceeds > 0:
        rentability = profit / proceeds
        print(f'Рентабельность выручки : {"%.2f" % (rentability * 100)}%')
    count = int(input('Введите численность сотрудников фирмы'))
    if count <= 0:
        print('Ввели неверное число')
    else:
        print(f'Прибыль в расчёте на одного сотрудика {"%.2f" % (profit/count)}')
elif profit == 0:
    print(f'Финансовый результат - {"%.2f" % profit}')
else:
    print(f'Финансовый результат - убыток {"%.2f" % -profit}')