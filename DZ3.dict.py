dictseasons = {1 : "зима", 2 : "весна", 3 : "лето", 4 : "осень"}
month = int (input ("Введите номер месяца: "))
if month == 12 or month == 1 or month == 2:
    print (dictseasons.get(1))
elif month == 3 or month == 4 or month == 5:
    print (dictseasons.get(2))
elif month == 6 or month == 7 or month == 8:
    print (dictseasons.get(3))
elif month == 9 or month == 10 or month ==11:
    print (dictseasons.get(4))
else:
    print("Ошибка! Введен неверный номер месяца!")