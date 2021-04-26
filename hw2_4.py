str = input('Введите строку из нескольких слов, разделённых пробелами')
list = str.split(' ')
for elem in list:
    print(elem[:10])