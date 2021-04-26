list = []
list.append('str')
list.append(1.01)
list.append(7)
list.append(True)
list.insert(2, False)
for element in list:
    print(type(element))