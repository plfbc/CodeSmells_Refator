

class Heroi:

    
    def __init__(self,nome,pontos_de_vida):
     self.nome = nome
     self.pontos_de_vida = int(pontos_de_vida)


    def setPontos_de_vida(self,pontos_de_vida) -> None:
        self.pontos_de_vida = pontos_de_vida
    def getPontos_de_vida(self)-> int:
        return self.pontos_de_vida

    def setNome(self,nome) -> None:
        self.nome = nome
        
    def getNome(self) -> str:
        return self.nome

    def getLacaios(self) -> list:
        return self.lacaios

    def setLacaios(self, lacaios) -> None:
        self.lacaios = lacaios

    def levarDano(self, dano:int):
        if self.pontos_de_vida <= dano:
            self.pontos_de_vida = 0
        else:
            self.pontos_de_vida = self.pontos_de_vida - dano       

    def __str__(self) -> str:
        return (f"Heroi: {self.nome} Vida: {self.pontos_de_vida}")