string_dz4 = input ("Введите несколько слов через пробел: ")
words = string_dz4.split(' ')
number = 1
for ind, el in enumerate (words , 1 ):
 print(ind , el [0:10])
