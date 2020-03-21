# coding: utf-8
spine = input()
group = input()
nutrition = input()



if spine == 'vertebrado' and group == 'ave' and nutrition == 'carnivoro':
    animal = "aguia"
    
elif spine == 'vertebrado' and group == 'ave' and nutrition == 'onivoro':
    animal = "pomba"
    
elif spine == 'vertebrado' and group == 'mamifero' and nutrition == 'onivoro':
    animal = "homem"
    
elif spine == 'vertebrado' and group == 'mamifero' and nutrition == 'herbivoro':
    animal = "vaca"
    
elif spine == 'invertebrado' and group == 'inseto' and nutrition == 'hematofogo':
    animal = "pulga"
    
elif spine == 'invertebrado' and group == 'inseto' and nutrition == 'herbivoro':
    animal = "lagarta"
    
elif spine == 'invertebrado' and group == 'anelideo' and nutrition == 'hematofogo':
    animal = "sanguessuga"
    
elif spine == 'invertebrado' and group == 'anelideo' and nutrition == 'onivoro':
    animal = "minhoca"
    
print(animal)
