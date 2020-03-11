""" Nome: Douglas Ivo Martins de Moraes
1. a) Sabe Programar: Não, ja experimentei algumas coisas de scripting structure nas minhas horas de lazer / hobbie, mas formalmente nunca programei ou aprendi uma linguagem de programação
b) Ja trabalha na aréa de computação? : Não
c) Ja estudou ou fez algum outro curso na área de computação? : Ja fiz um curso de informatica básica mas nada nunca avançado como programação. Coisas simples como gerenciamento de arquivo, como utilizar o word/excel/powerpoint."""

#===============================================================================================


P1 = float(input("Entre a nota da sua Prova 1, se decimal, utilizar ponto em vez de virgula: ")) #aqui o usuário entrará o resultado da p1

P2 = float(input("Entre a nota da sua Prova 2, se decimal, utilizar ponto em vez de virgula: "))  #aqui o usuário entrará o resultado da p2

P3 = float(input("Entre a notada sua Prova 3, se decimal, utilizar ponto em vez de virgula: "))  #aqui o usuário entrará o resultado da p3

MP = (P1 + P2 + P3)/3   #A média arítimetica de prova sera calculada

print("Media de prova: ", MP) #A nível de curiosidade a média de prova sera mostrada na tela


#===============================================================================================

E1 = float(input("Entre a nota do seu Teste 1, se decimal, utilizar ponto em vez de virgula: ")) # Aqui o usuário entrará o resultado do Teste 1

E2 = float(input("Entre a nota do seu Teste 2, se decimal, utilizar ponto em vez de virgula: ")) # Aqui o usuário entrará o resultado do Teste 2

ME = (E1 + E2)/2 # Aqui a média arítimetica dos testes será calculada

print("Média de teste: ", ME) # A nível de curiosidade a média do teste sera mostrada na tela


#===============================================================================================

T = float(input("Entre a nota do seu Trabalho, se decimal, utilizar ponto em vez de virgula: ")) # Aqui o usuário entrará o resultado do Trabalho

#===============================================================================================

MAo = (0.7*MP) + (0.2*ME) + (0.1*T) # Aqui serão aplicados os pesos em cada média, e no final, a soma de todos eles

MAf = int(MAo*10)/10 # Aqui o resultado de MAo será multiplicado por 10 como numero inteiro e posteriormente divido por 10 para ser mostrado apena uma unica casa decimal

print("A sua média total sera: ", MAf) # Aqui o resultado da média final será mostrado na tela
