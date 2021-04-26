list = list(input('Введите список значений через запятую').split(','))
cnt = list.index(list[-1]) + 1
iterations_count = cnt // 2
idx = 0
while idx < iterations_count:
    list.insert(idx * 2, list[idx * 2 + 1])
    list.pop(idx * 2 + 2)
    idx += 1
print(list)