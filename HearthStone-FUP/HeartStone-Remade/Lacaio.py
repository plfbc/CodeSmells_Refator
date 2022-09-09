class Lacaio:
    def __init__(self,nome, pontos_de_vida, pontos_de_dano) -> None:
        self.nome = nome
        self.pontos_de_vida = int(pontos_de_vida)
        self.pontos_de_dano = int(pontos_de_dano)


    def levarDano(self, dano:int):
        if self.pontos_de_vida <= dano:
            self.pontos_de_vida = 0
        else:
            self.pontos_de_vida = self.pontos_de_vida - dano
    

    def causarDano(self, alvo):
        alvo.levarDano(self.dano)

    

    
            
