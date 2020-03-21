# coding: utf-8

value = int(input())

banknote_100 = value//100

banknote_50 = (value%100)//50

banknote_20 = ((value%100)%50)//20

banknote_10 = (((value%100)%50)%20)//10

banknote_5 = ((((value%100)%50)%20)%10)//5

banknote_2 = (((((value%100)%50)%20)%10)%5)//2

banknote_1 = ((((((value%100)%50)%20)%10)%5)%2)//1

print(value)
print(banknote_100, "nota(s) de R$ 100,00")
print(banknote_50, "nota(s) de R$ 50,00")
print(banknote_20, "nota(s) de R$ 20,00")
print(banknote_10, "nota(s) de R$ 10,00")
print(banknote_5, "nota(s) de R$ 5,00")
print(banknote_2, "nota(s) de R$ 2,00")
print(banknote_1, "nota(s) de R$ 1,00")