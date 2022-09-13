class Lacaio:
    def __init__(self,nome, pontos_de_vida, pontos_de_dano) -> None:
        self.nome = nome
        self.pontos_de_vida = int(pontos_de_vida)
        self.pontos_de_dano = int(pontos_de_dano)
    
    def getNome(self) -> str:
        return self.nome

    def setNome(self,nome) -> None:
        self.nome = nome


    def getPontos_de_vida(self)-> int:
        return self.pontos_de_vida

    def getPontos_de_dano(self) -> int:
        return self.pontos_de_dano


    def levarDano(self, dano:int):
        if self.pontos_de_vida <= dano:
            self.pontos_de_vida = 0
        else:
            self.pontos_de_vida = self.pontos_de_vida - dano
    

    def causarDano(self, alvo):
        alvo.levarDano(self.getPontos_de_dano())
        if isinstance(alvo,Lacaio):
            self.levarDano(alvo.getPontos_de_dano())

    def __str__(self) -> str:
        return (f"Lacaio: {self.nome} Vida: {self.pontos_de_vida} Dano:{self.pontos_de_dano}")
    

    
            
