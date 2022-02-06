list_dz2 = input ("Заполните элементы списка через пробел: ").split()
for i in range (0, len (list_dz2) -1, 2):
    list_dz2[i], list_dz2[i + 1] = list_dz2[i + 1], list_dz2[i]
    print (list_dz2)
