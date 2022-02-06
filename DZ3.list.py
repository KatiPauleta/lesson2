listseasons = ["зима", "весна", "лето", "осень"]
month = int (input ("Введите номер месяца: "))
if month == 12 or month == 1 or month == 2:
    print (listseasons [0])
elif month == 3 or month == 4 or month == 5:
    print(listseasons[1])
elif month == 6 or month == 7 or month == 8:
    print(listseasons[2])
elif month == 9 or month == 10 or month ==11:
    print(listseasons[3])
else:
    print("Ошибка! Введен неверный номер месяца!")
