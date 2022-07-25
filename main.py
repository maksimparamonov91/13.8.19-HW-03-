ticket = int(input("Введите количество билетов, планируемые к покупке (money):"))
full_price = 0
for i in range(1, ticket+1):
     age = int(input(f"Введите возраст для билета {i}, :"))
     if 0 < age < 18:
         price = 0
         full_price += price
     elif 18 <= age < 25:
         price = 990
         full_price += price
     else:
         price = 1390
         full_price += price
if ticket > 3:
    full_price *= 0.9
    print("Применена скидка 10%, Ваша итоговая сумма к оплате:",full_price)
else:
    print("Ваша итоговая сумма к оплате:", full_price)
