per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
rate = [per_cent['ТКБ'], per_cent['СКБ'], per_cent['ВТБ'], per_cent['СБЕР']]

rate1 = [dict.values(per_cent)]
D = 365
money = int(input("Введите сумму которую планируете положить под проценты"))
deposit = [(money*rate[0]*D/D)/100, (money*rate[1]*D/D)/100, (money*rate[2]*D/D)/100, (money*rate[3]*D/D)/100]

print(list(map(round, deposit)))
print("Максимальная сумма, которую вы можете заработать —", max(map(round, deposit)))

 