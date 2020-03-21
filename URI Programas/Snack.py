# coding: utf-8

x_str, y_str = input().split()

X = int(x_str)
Y = int(y_str)

if X == 1:     #Cachorro Quente
    X = 4
    
elif X == 2:     # X-Salada
    X = 4.50
    
elif X == 3:     # X-Bacon
    X = 5
    
elif X == 4:     # Torrada Simples
    X = 2
    
elif X == 5:     # Refrigerante
    X = 1.50
    
print("Total: R$ {:.2f}".format(X*Y))D