# coding: utf-8
a, b, c = map(int, input().split())

old_a = a
old_b = b
old_c = c

if a>b:
    aux=a
    a=b
    b=aux
    
if a>c:
    aux=a
    a=c
    c=aux

if b>c:
    aux=b
    b=c
    c=aux
    
print(a)
print(b)
print(c)
print()
print(old_a)
print(old_b)
print(old_c)