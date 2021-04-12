sVar1 = 'simple string'
print(sVar1)
sVar2 = 'difficult "string'
print(sVar2)
bVar1 = True
bVar2 = bVar1 == sVar1
print(bVar2)

age = int(input('Введите ваш возраст'))
weight = int(input('Введите ваш вес'))
name = input('Введите ваше имя')
middle_name = input('Введите ваше отчество')

print(f'Привет, {name} {middle_name}, мне тут птичка на хвостике принесла, что ты в свои {age} лет весишь {weight} кг')

