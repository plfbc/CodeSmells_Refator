'''
Paulo Victor Alves Fabrício
511013

//sonarqube 
FUP
Trabalho individual 1 - "HeartStone: Ataque de Lacaio"

'''
print("_____________________________"
      "| BEM VINDOS A HEARTSTONE   |"
      "____________________________")
'''
primeiramente, tenho que declarar as variáveis  para os 2 herois e para os 2 lacaios de cada
e pedir o valor dessas para o usuário, tendo as limitações de cada variável
'''
Hero_Aliado = str(input('Escolha Seu Heroi: ')) # entrada do heroi aliado,
HA_Vida = str(input(f'Quanto de vida tem {Hero_Aliado} ? '))


'''
para o nome do heroi não há tanta difereça na entrada de alfanumericos, 
porem nos pontos de vida e ataque geram graves problemas.
então devo fazer o tratamento de erro para a string que não seja numerica
'''
while not HA_Vida.isnumeric(): #<--- na primeira parte criei um loop para o valor não numerico
    print('O Heroi não possui pontos de vida válidos (1 - 30)')
    HA_Vida = str(input(f'Quanto de vida tem {Hero_Aliado}? '))

HA_Vida = int(HA_Vida)#formatar a string numerica para inteiro para o proximo passo do tratamento

# após isso faço a condicional da vida do heroi, que deve ser maior que 0 e menor que 30
while HA_Vida > 30 or HA_Vida <= 0:
    print('O Heroi não possui pontos de vida válidos (1 - 30)')
    HA_Vida = str(input(f'Quanto de vida tem {Hero_Aliado}? '))
    while not HA_Vida.isnumeric():
        print('O Heroi não possui pontos de vida válidos (1 - 30)')
        HA_Vida = str(input(f'Quanto de vida tem seu Heroi? '))
    # " uso de str de novo" durante os testes desse tratamento de erro,
    # percebi que ainda podia forçar erro caso usasse algo que não fosse um número

    HA_Vida = int(HA_Vida) #após o tratamento a valor volta a ser inteiro


# para as próximas variáveis o tratamento de erro é igual, utilizando de loop para os erros ,
# tendo uma pequena variação para os lacaios

Lac_Aliado1 = str(input(f'Qual o primeiro lacaio seu que está no campo? '))

LA1_Vida = str(input(f'Quanto de vida tem {Lac_Aliado1}? '))

while not LA1_Vida.isnumeric():
    print('O lacaio não possui pontos de vida validos (1 - 10)')
    LA1_Vida = str(input(f'Quanto de vida tem {Lac_Aliado1}? '))

LA1_Vida = int(LA1_Vida)

while LA1_Vida > 10 or LA1_Vida <= 0:  #<---- para os lacaios, a vida não pode variar mais que 10 e deve ser maior que zero.(-)
    print('O lacaio não possui pontos de vida válidos (1 - 10)')
    LA1_Vida = str(input(f'Quanto de vida tem {Lac_Aliado1}? '))
    while not LA1_Vida.isnumeric():
        print('O lacaio não possui pontos de vida válidos (1 - 10)')
        LA1_Vida = str(input(f'Quanto de vida tem {Lac_Aliado1}? '))

    LA1_Vida = int(LA1_Vida)

LA1_Dano = str(input(f'Quanto de dano causa {Lac_Aliado1}? '))

while not LA1_Dano.isnumeric():
    print('O lacaio não possui pontos de ataque validos (0 - 10)') #<---- (-) Mas, o dano sim pode ser zero, uma vez que o lacaio pode não dar dano, então deve ser menor que 10 e maior ou igual a 0
    LA1_Dano = str(input(f'Quanto de dano causa {Lac_Aliado1}? '))

LA1_Dano = int(LA1_Dano)

while LA1_Dano > 10 or 0 > LA1_Dano: #<---- 
    print('O lacaio não possui pontos de ataque válidos (0 - 10)')
    LA1_Dano = str(input(f'Quanto de vida tem {Lac_Aliado1} '))
    while not LA1_Dano.isnumeric():
        print('O lacaio não possui pontos de ataque válidos (0 - 10)')
        LA1_Dano = str(input(f'Quanto de dano causa {Lac_Aliado1}? '))

    LA1_Dano = int(LA1_Dano)

Lac_Aliado2 = str(input('Qual é o seu outro Lacaio que está na Mesa? '))
LA2_Vida = str(input(f'Quanto de vida tem {Lac_Aliado2}? '))
while not LA2_Vida.isnumeric():
    print('O lacaio não possui pontos de vida validos (1 - 10)')
    LA2_Vida = str(input(f'Quanto de vida tem {Lac_Aliado2}? '))

LA2_Vida = int(LA2_Vida)

while LA2_Vida > 10 or LA2_Vida <= 0:
    print('O lacaio não possui pontos de vida válidos (1 - 10)')
    LA2_Vida = str(input(f'Quanto de vida tem {Lac_Aliado2} '))
    while not LA2_Vida.isnumeric():
        print('O lacaio não possui pontos de vida válidos (1 - 10)')
        LA2_Vida = str(input(f'Quanto de vida tem {Lac_Aliado2}? '))
    LA2_Vida = int(LA2_Vida)

LA2_Dano = str(input(f'Quanto de dano causa {Lac_Aliado2}? '))
while not LA2_Dano.isnumeric():
    print('O lacaio não possui pontos de ataque validos (0 - 10)')
    LA2_Dano = str(input(f'Quanto de dano causa {Lac_Aliado2}? '))

LA2_Dano = int(LA2_Dano)

while LA2_Dano > 10 or 0 > LA2_Dano:
    print('O lacaio não possui pontos de ataque válidos (0 - 10)')
    LA2_Dano = str(input(f'Quanto de dano causa {Lac_Aliado2}? '))
    while not LA2_Dano.isnumeric():
        print('O lacaio não possui pontos de ataque válidos (0 - 10)')
        LA2_Dano = str(input(f'Quanto de dano causa {Lac_Aliado2}? '))

    LA2_Dano = int(LA2_Dano)
'''
apos declarado a lado aliado,
fiz um pequeno print para mostrar ao usuario quais lacaios ele colocou.
(um pouco estilizado demais para parecer uma arena)

'''
print('---------------------------------------------------------------------------')
print(f'                   Seu heroi é {Hero_Aliado},                             ')
print(f'                   seus lacaios em campo são: ')
print(f'   {Lac_Aliado1}                                    {Lac_Aliado2}')
print('---------------------------------------------------------------------------')

"""
para o lado inimigo segui utilizando a mesma ideia que o lado aliado,
uma vez que o lado inimigo segue as mesmas limitações e regras sobre as variáveis
"""
Hero_Inimigo = str(input('Escolha Seu Oponente: '))
HI_Vida = str(input(f'Quanto de vida tem {Hero_Inimigo}? '))
while not HI_Vida.isnumeric():
    print('O Heroi não possui pontos de vida válidos (1 - 30')
    HI_Vida = str(input(f'Quanto de vida tem {Hero_Inimigo}? '))

HI_Vida = int(HI_Vida)

while HI_Vida > 30 or HI_Vida <= 0:
    print('O Heroi não possui pontos de vida válidos (1 - 30)')
    HI_Vida = str(input(f'Quanto de vida tem {Hero_Inimigo}? '))
    while not HI_Vida.isnumeric():
        print('O Heroi não possui pontos de vida válidos (1 - 30)')
        HI_Vida = str(input(f'Quanto de vida tem {Hero_Inimigo}? '))

    HI_Vida = int(HI_Vida)

Lac_Inimigo1 = str(input('Qual lacaio seu adversário colocou primeiro? '))
LI1_Vida = str(input(f'Quanto de vida tem {Lac_Inimigo1}? '))
while not LI1_Vida.isnumeric():
    print('O lacaio não possui pontos de vida validos (1 - 10)')
    LI1_Vida = str(input(f'Quanto de vida tem {Lac_Inimigo1}? '))

LI1_Vida = int(LI1_Vida)

while LI1_Vida > 10 or LI1_Vida <= 0:
    print('O lacaio não possui pontos de vida válidos (1 - 10)')
    LI1_Vida = str(input(f'Quanto de vida tem {Lac_Inimigo1}? '))
    while not LI1_Vida.isnumeric():
        print('O lacaio não possui pontos de vida válidos (1 - 10)')
        LI1_Vida = str(input(f'Quanto de vida tem {Lac_Inimigo1}? '))

    LI1_Vida = int(LI1_Vida)
LI1_Dano = str(input(f'Quanto de dano causa {Lac_Inimigo1}?'))
while not LI1_Dano.isnumeric():
    print('O lacaio não possui pontos de ataque validos (0 - 10)')
    LI1_Dano = str(input(f'Quanto de dano causa {Lac_Inimigo1}? '))

LI1_Dano = int(LI1_Dano)

while LI1_Dano > 10 or 0 > LI1_Dano:
    print('O lacaio não possui pontos de ataque válidos (0 - 10)')
    LI1_Dano = str(input(f'Quanto de vida tem {Lac_Inimigo1}? '))
    while not LI1_Dano.isnumeric():
        print('O lacaio não possui pontos de ataque válidos (0 - 10)')
        LI1_Dano = str(input(f'Quanto de dano causa {Lac_Inimigo1}? '))

    LI1_Dano = int(LI1_Dano)
Lac_Inimigo2 = str(input('Qual lacaio seu adversário colocou depois?'))
LI2_Vida = str(input(f'Quanto de vida tem {Lac_Inimigo2}? '))

while not LI2_Vida.isnumeric():
    print('O lacaio não possui pontos de vida validos (1 - 10)')
    LI2_Vida = str(input(f'Quanto de vida tem {Lac_Inimigo2}? '))

LI2_Vida = int(LI2_Vida)

while LI2_Vida > 10 or LI2_Vida <= 0:
    print('O lacaio não possui pontos de vida válidos (1 - 10)')
    LI2_Vida = str(input(f'Quanto de vida tem {Lac_Inimigo2}? '))
    while not LI2_Vida.isnumeric():
        print('O lacaio não possui pontos de vida válidos (1 - 10)')
        LI2_Vida = str(input(f'Quanto de vida tem {Lac_Inimigo2}? '))

    LI2_Vida = int(LI2_Vida)
LI2_Dano = str(input(f'Quanto de dano causa {Lac_Inimigo2}? '))
while not LI2_Dano.isnumeric():
    print('O lacaio não possui pontos de ataque validos (0 - 10)')
    LI2_Dano = str(input(f'Quanto de dano causa {Lac_Inimigo2}? '))

LI2_Dano = int(LI2_Dano)

while LI2_Dano > 10 or 0 > LI2_Dano:
    print('O lacaio não possui pontos de ataque válidos (0 - 10)')
    LI2_Dano = str(input(f'Quanto de vida tem {Lac_Inimigo2}? '))
    while not LI2_Dano.isnumeric():
        print('O lacaio não possui pontos de ataque válidos (0 - 10)')
        LI2_Dano = str(input(f'Quanto de dano causa {Lac_Inimigo2}? '))

    LI2_Dano = int(LI2_Dano)

print('-------------------------------------------------------------------------------------')# <---- mesmo estilo de demonstração
print(f'                         Seu openente é {Hero_Inimigo},                             ')
print(f'                          seus lacaios em campo são                                 ')
print(f'                      {Lac_Inimigo1}          {Lac_Inimigo2}                        ')

print(f'----------------------------------|Hora da Batalha|---------------------------------')
print(f'                     {Hero_Aliado}    Versus   {Hero_Inimigo}') 
print('Seu turno:') #<--- esteticamente, utilizei o heroi 1 como se fosse de controle do usuario, utilizando termos direcionados a voz direta
print(f'Seus lacaios são {Lac_Aliado1}({LA1_Vida}|{LA1_Dano}) e {Lac_Aliado2}({LA2_Vida}|{LA2_Dano})') #aqui peço para o programa já adiantar as escolhar que podem ser feitas, mostrando elas para o usuário
Escolha_Ali = str(input('Qual lacaio você que usar? '))
'''
apos a escolha, é feito um laço para caso o usuario entre com um valor que, 
ou não esteja no programa, ou não seja de controle do seu heroi
'''
while not ((Escolha_Ali.upper() == Lac_Aliado1.upper()) or (Lac_Aliado2.upper() == Escolha_Ali.upper())): #<--- aqui utilizei do n.upper() para igualar a entrada, caso fosse utilizado letras captalizadas e etc.
    print(f'o lacaio que você escolheu não é valido (escolha entre {Lac_Aliado1, Lac_Aliado2})')
    Escolha_Ali = str(input('Qual lacaio você que usar? '))

print(f' possíveis alvos: {Hero_Inimigo}({HI_Vida}), {Lac_Inimigo1}({LI1_Vida}|{LI1_Dano}) e {Lac_Inimigo2}({LI2_Vida}|{LI2_Dano})')#<---  mostrando os possíveis alvos de escolha, para facilitar para o usuario escolher
Escolha_Ing = str(input(f'Qual inimigo você quer que {Escolha_Ali} ataque? '))
'''
O laço do controle de dano do alvo tem uma diferença do aliado,
os possiveis alvos são 3, sendo eles o lacaio 1, o lacaio 2 e o proprio heroi
para o ultimo, tem-se uma caracteristica em específico: o heroi não tem pontos de dano.
'''
while not ((Escolha_Ing.upper() == Hero_Inimigo.upper()) or (Escolha_Ing.upper() == Lac_Inimigo1.upper()) or (Escolha_Ing.upper() == Lac_Inimigo2.upper())):
    print(f'o inimigo escolhido não é valido ( escolha entre {Hero_Inimigo, Lac_Inimigo1, Lac_Inimigo2})')
    Escolha_Ing = str(input(f'Qual inimigo você quer que {Escolha_Ali} ataque? '))

print('ataque feito!')
'''
Aqui começa o processo para o cálculo do dano, sendo essa primeira pante 
uma estrutura de possibilidades e condicionais.
'''
if Escolha_Ali.upper() == Lac_Aliado1.upper():
    Ali_Vida = LA1_Vida #<--- para cada escolha, tem uma deficinição para a variavel de dano e de vida do lacaio
    Ali_Dano = LA1_Dano #<--- uma vez que esses vão ser utilizados para o calculo do dano.
    '''
    Apos a declaração das variaveis, criei mais duas:
    Quando se escolhe um lacaio, ja é certeza que um deles não vai sofrer nada, no caso do lacaio aliado 1 (-)
    '''
    Ali_ctz = Lac_Aliado2 #<---- (-) o lacaio que com certeza não vai levar dano, é o lacaio aliado 2
    CtzA_vida = LA2_Vida
    CtzA_dano = LA2_Dano

else: #a unica opição alem do lacio aliado 1, é o dois então coloquei apenas a condição else
    Ali_Vida = LA2_Vida
    Ali_Dano = LA2_Dano
    Ali_ctz = Lac_Aliado1#<---- Lacaio aliado 1 para o lacaio aliado 2
    CtzA_vida = LA1_Vida
    CtzA_dano = LA1_Dano

if Escolha_Ing.upper() == Lac_Inimigo1.upper():
    Ing_Vida = LI1_Vida
    Ing_Dano = LI1_Dano
    Ing_ctz = f'{Lac_Inimigo2} com {LI2_Vida} de Vida' #<--- para o inimigo eu juntei a vida e o nome do lacaio que com certeza 
    CtzI_dano= f'| {LI2_Dano} de Dano'                                                   #     não vai levar dano, alem de formatar em uma string, por causa da escolha do heroi(-)

elif Escolha_Ing.upper() == Lac_Inimigo2.upper():
    Ing_Vida = LI2_Vida
    Ing_Dano = LI2_Dano
    Ing_ctz = f'{Lac_Inimigo1} com {LI1_Vida} de Vida'
    CtzI_dano= f'|{LI2_Dano} de Dano'

else:
    Ing_Vida = HI_Vida
    Ing_Dano = 0 #<---- como dito antes, o heroi não causa dano, a variavel sempre sera zero para o calculo
    Ing_ctz = f'{Lac_Inimigo1} com {LI1_Vida} de vida | {LI1_Dano} de dano   {Lac_Inimigo2} com {LI2_Vida} de vida | {LI2_Dano} de dano' #<---- (-) para o heroi, os lacaios não vão levar dano, isso de certeza, então coloquei os dois em uma só variavel formatada
    CtzI_dano = str()
'''
após fazer as 5 possibilidades de ataques, é feito finalmente o calculo do dano, sendo sempre vida - dano.
'''
result_Ali = Ali_Vida - Ing_Dano
result_Ing = Ing_Vida - Ali_Dano
#apos feito o calculo do ataque devesse declarar o resultado dela,
#  ou seja quanto de vida foi perdido ou quais lacaios morreram ou se o heroi inimigo morreu ao ser alvejado.
if result_Ali <= 0:
    print(f'{Escolha_Ali} não resistiu!')
    result_Ali = str('-MORTO-')
    Ali_DanoF = str()
else:
    result_Ali = str(f'com {result_Ali} de vida')
    Ali_DanoF = str(f'| {Ali_Dano} de Dano')

if result_Ing <= 0:
    print(f'{Escolha_Ing} não resistiu!')#***
    result_Ing = str('-MORTO- ')
    Ing_Dano = str()

else:
    result_Ing = str(f'com {result_Ing} de vida')
    Ing_Dano = str(f'| {Ing_Dano} de Dano')

'''
mas para a condição do heroi tive que declarar uma nova variável,
a variável propria dos estatus do heroi, uma vez que o ataque direcionado
a ele modifica toda a saida do resultado
'''
Stts = f'com {HI_Vida} de vida' #<--- aqui a declaração caso o ataque não seja no heroi inimigo em si

if Escolha_Ing.upper() == Hero_Inimigo.upper():
    Stts = HI_Vida - Ali_Dano #<--- mas, uma vez que o ataque foi feito no heroi inimigo devesse calcular o dano que ele tomou
    if Stts <= 0: # e caso o ataque deferido seje fatal, a declaração deste como morto
        Stts = str('-MORTO-')
    else:
        Stts = f'com {Stts} de vida'
    Escolha_Ing = str()# Outra é a avaliação para o resultado, uma vez que não devesse repetir o heroi e/ou
    result_Ing = str()# a vida dele.   ***(preferi não colocar essa parte durante as condicionais para poder mostrar que o heroi foi morto)
    Ing_Dano = str()

print('Resultado do ataque: ') # aqui tem a estilização do resultado final da arena.
print('---------------------------------------------------------------------------------------------------------------')
print('no lado aliado:')
print(f'                              {Hero_Aliado}                                                                   ')
print(f'                            com {HA_Vida} de vida                                                             ')
print('')
print(f'{Escolha_Ali} {result_Ali} {Ali_DanoF}                 {Ali_ctz} com {CtzA_vida} de vida | {CtzA_dano} de dano ')
print('---------------------------------------------------------------------------------------------------------------')

print('No lado inimigo:')
print(f'                               {Hero_Inimigo}                                        ')
print(f'                             {Stts}                                                  ')
print('')
print(f'{Escolha_Ing} {result_Ing}{Ing_Dano}           {Ing_ctz} {CtzI_dano}                 ')
print('---------------------------------------------------------------------------------------------------------------')

#e caso os pontos de vida do heroi inimigo zerem, a declaranção do vencedor.
end = HI_Vida - Ali_Dano
if end <= 0:
    print(f'Fim De Jogo! {Hero_Aliado} Venceu!')
else:
    pass