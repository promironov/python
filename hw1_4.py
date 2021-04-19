max_digit = 0
val = int(input('Введите целое положительное число'))
if val < 0:
    print('Введено ошибочное число')
    exit()
while val > 0 and max_digit < 9:
    current_digit = val % 10
    if max_digit < current_digit:
        max_digit = current_digit
    val = val // 10
print(f'Максимальная цифра в числе {max_digit}')