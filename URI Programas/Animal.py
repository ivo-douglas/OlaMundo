# coding: utf-8
spine = input()
group = input()
nutrition = input()

#a == coluna
#b == grupo

if spine == 'vertebrado':
    if group == 'ave':
        if nutrition == 'onivoro':
            print('pomba')
        elif nutrition == 'carnivoro':
            print('aguia')
    else:
        if group == 'mamifero':
            if nutrition == 'onivoro':
                print('homem')
            elif nutrition == 'herbivoro':
                print('vaca')

else:
    if spine == 'invertebrado':
        if group == 'inseto':
            if nutrition == 'hematofago':
                print("pulga")
            elif nutrition == 'herbivoro':
                print("lagarta")
        else:
            if group == 'anelideo':
                if nutrition == 'hematofago':
                    print("sanguessuga")
                elif nutrition == 'onivoro':
                    print("minhoca")