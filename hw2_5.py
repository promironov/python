my_list = [7, 5, 3, 3, 2]
new_rate = int(input('Введите позицию в рейтинге'))
if new_rate > my_list[0]:
    my_list.insert(0, new_rate)
else:
    my_list.reverse()
    for elem in my_list:
        if elem >= new_rate:
            idx_elem = my_list.index(elem)
            my_list.insert(idx_elem, new_rate)
            my_list.reverse()
            break
print(my_list)