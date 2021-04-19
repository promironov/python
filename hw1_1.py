s_var1 = 'simple string'
print(s_var1)
s_var2 = 'difficult "string'
print(s_var2)
b_var1 = True
b_var2 = b_var1 == s_var1
print(b_var2)

age = int(input('Введите ваш возраст'))
weight = int(input('Введите ваш вес'))
name = input('Введите ваше имя')
middle_name = input('Введите ваше отчество')

print(f'Привет, {name} {middle_name}, мне тут птичка на хвостике принесла, что ты в свои {age} лет весишь {weight} кг')

