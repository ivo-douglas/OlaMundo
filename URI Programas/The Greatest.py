# coding: utf-8

a, b, c = map(int, input().split())


maiorab = int(((a+b)+abs(a-b))/2)

maior = int(((c+maiorab)+abs(c-maiorab))/2)

print(maior,"eh o maior")