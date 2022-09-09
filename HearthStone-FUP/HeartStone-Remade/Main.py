from Heroi import Heroi
from Lacaio import Lacaio

def inicio():
    print("_____________________________"
      "| BEM VINDOS A HEARTSTONE   |"
      "____________________________")

def validaVida(entrada, tipo_de_alvo)-> bool:
    if  entrada.isnumeric():
        entrada = int(entrada)
        validacao_de_cada_tipo = (tipo_de_alvo == "lacaio" and 0 < entrada <= 10) or \
            (tipo_de_alvo == "heroi" and 0 < entrada <= 30)

        if validacao_de_cada_tipo:
            return True
        
    return False

def validaDano(entrada) -> bool:
    if  entrada.isnumeric():
        entrada = int(entrada)
        validacao_de_dano = (0 < entrada <= 10) 

        if validacao_de_dano:
            return True
        
    return False

def criarHeroi() -> Heroi:
    nome = input("Qual o nome do herói? ")
    vida = "naoNumerico"
    while not validaVida(vida, "heroi"):
        vida = input(f"Qual a vida de {nome} (entre 1 e 30)? ")
        if not validaVida(vida,"heroi"):
            print("Entrada inválida")
    heroi = Heroi(nome, int(vida))
    return heroi

def criarLacaio(heroi):
    nome_do_lacaio = input("Qual o nome do lacaio? ")
    pontos_de_vida = "naoNumerico"
    pontos_de_dano = "naoNumerico"

    while not validaVida(pontos_de_vida, "lacaio"):
        pontos_de_vida = input(f"Qual a vida de {nome_do_lacaio} (entre 1 e 10)? ")
        if not validaVida(pontos_de_vida, "lacaio"):
            print("Entrada inválida")

    while not validaDano(pontos_de_dano):
        pontos_de_dano = input(f"Qauntos pontos de dano causa {nome_do_lacaio}")
        if not validaDano(pontos_de_dano):
            print("Entrada inválida")

    lacaio =  Lacaio(nome_do_lacaio, int(pontos_de_vida),int(pontos_de_dano))
    
    lacaios = heroi.getLacaios()
    lacaios.append(lacaio)
    heroi.setLacaios(lacaios)


teste = criarHeroi()
print(teste.getNome())