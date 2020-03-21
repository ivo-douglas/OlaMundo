# Coding: utf-8

A, B, C = map(float, input().split())


if A < B:
    Aux=A
    A=B
    B=Aux

if A < C:
    Aux=A
    A=C
    C=Aux
    
if B < C:
    Aux=B
    B=C
    C=Aux


if A >= B + C:
    print("NAO FORMA TRIANGULO")
        
elif A**2 == B**2 + C**2:
    print("TRIANGULO RETANGULO")

else:
    if  A**2 > B**2 + C**2:
        print("TRIANGULO OBTUSANGULO")

    if A**2 < B**2 + C**2:
        print("TRIANGULO ACUTANGULO")
    
    if A == B and A == C and B == C:
        print("TRIANGULO EQUILATERO")

    if (A == B and A != C and B != C) or (A == C and A != B and C!=B) or (C == B and B != A and C != A):
        print("TRIANGULO ISOSCELES")