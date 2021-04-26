list_seasons = ['Зима', 1, 2, 12, 'Весна',3,4,5,'Лето', 6,7,8,'Осень', 9,10,11]
dict_seasons = {1:'Зима', 2:'Зима', 12:'Зима', 3:'Весна', 4:'Весна', 5:'Весна', 6:'Лето', 7:'Лето', 8:'Лето', 9:'Осень', 10:'Осень', 11:'Осень'}

month = int(input('Введите номер месяца'))

if month < 1 or month > 12:
    print('Введено неверное число')
    exit()
else:
    idx = (list_seasons.index(month)) // 4
    print('Результат решения через List: ', list_seasons[idx * 4])
    print('Результат решения через Dict: ', dict_seasons[month])