products = []
id = 0
while True:
    more_str = ''
    if id > 0:
        more_str = 'ещё один '
    answer = input(f'Ввести {more_str}товар? (да/нет)')
    if answer != 'да':
        break
    id += 1
    name = input('Введите название товара:')
    price = input('Введите цену товара:')
    quantity = input('Введите количество товара:')
    base = input('Введите единицу измерения товара:')
    products.append( (id, {"Название": name, "цена": price, "количество": quantity, "ед": base}) )

properties_dict = dict()

for product in products:
    properties = product[1]
    for key in properties.keys():
        if properties_dict.get(key) is None:
            properties_dict[key] = {properties[key]}
        else:
            properties_dict[key].add(properties[key])
for key in properties_dict.keys():
    properties_dict[key] = list(properties_dict[key])
print(properties_dict)

