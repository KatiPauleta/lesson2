new_number = int(input("Введите новый элемент рейтинга: "))
my_list = [13, 11, 7, 5, 3, 2, 1]
a = my_list.count(new_number)
for el in my_list:
    if a > 0:
        i = my_list.index(new_number)
        my_list.insert(i+a, new_number)
        break
    else:
        if new_number > el:
            b = my_list.index(el)
            my_list.insert(b, new_number)
            break
        elif new_number < my_list[len(my_list) - 1]:
            my_list.append(new_number)
print(my_list)

