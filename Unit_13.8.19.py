try:
    tiket = int(input("Введиет колличество билетов:\n"))
    age = [int(input("Укажите возраст:\t")) for i in range(tiket)]
    S = 0
    for i in age:
        if i <= 0 or i > 100:
            print("Возраст не может быть больше 100 или меньше 0")
            raise ValueError("Неверно указан возраст")
        elif i in range(0,18):
            S += 0
        elif i in range(18,26):
            S += 990
        elif i in range(26,100):
            S += 1390
    if tiket >= 3 and S > 0:
        S = S*0.9
        print("Скидка 10% активирована")
    print(f"Колличество билетов к заказу: {tiket}")
    print(f"Сумма заказа: {S}")
except ValueError as e:
    print("Неверное значение")
except NameError as e:
    print()