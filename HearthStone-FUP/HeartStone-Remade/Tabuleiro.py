

class Tabuleiro:
    
    def __init__(self,heroi_aliado,lacaio_aliado_1,lacaio_aliado_2,heroi_inimigo,lacaio_inimigo_1,lacaio_inimigo_2):

        print(lacaio_inimigo_1)
        self.heroi_aliado = heroi_aliado
        self.heroi_inimigo = heroi_inimigo
        
        self.lacaio_aliado_1 = lacaio_aliado_1
        self.lacaio_aliado_2 = lacaio_aliado_2
        self.lacaio_inimigo_1 = lacaio_inimigo_1
        self.lacaio_inimigo_2 = lacaio_inimigo_2
  
    def getHeroi_aliado(self):
        return self.heroi_aliado
    
    def getHeroi_inimigo(self):
        return self.heroi_inimigo
 
    def getLacaio_aliado_1(self):
        return self.lacaio_aliado_1
    
    def getLacaio_aliado_2(self):
        return self.lacaio_aliado_2
    
    def getLacaio_inimigo_1(self):
        return self.lacaio_inimigo_1
    
    def getLacaio_inimigo_2(self):
        return self.lacaio_inimigo_2
    
    def escolhe_lacaio(self):
    
        escolhe = False
        while(not escolhe):
            lacaio_escolhido = input(f"escolha qual lacaio aliado irá atacar: \n\n[1] {self.lacaio_aliado_1} \n[2] {self.lacaio_aliado_2}\n ")
            if lacaio_escolhido == '1':
                lacaio_escolhido =self.lacaio_aliado_1
                break
            elif lacaio_escolhido == '2':
                lacaio_escolhido = self.lacaio_aliado_2
                break
            else:
                print("Entrada Invalida") 
                continue
        return lacaio_escolhido

    def escolhe_alvo(self) :
        
        escolhe = False
        while(not escolhe):
            alvo_escolhido      = input(f"qual alvo quer atacar? \n\n[1]{self.heroi_inimigo}\n[2]{self.lacaio_inimigo_1}\n[3]{self.lacaio_inimigo_2}\n")
            
            
            if alvo_escolhido == '1':
                alvo_escolhido = self.heroi_inimigo
                break
            elif alvo_escolhido == '2':
                alvo_escolhido = self.lacaio_inimigo_1
                break
            elif alvo_escolhido == '3':
                alvo_escolhido = self.lacaio_inimigo_2
            else:
                print("Entrada Invalida") 
                continue

        return alvo_escolhido

    def realizar_ataque(self)-> None:
        lacaio_escolhido = self.escolhe_lacaio()
        alvo_escolhido   = self.escolhe_alvo()
        lacaio_escolhido.causarDano(alvo_escolhido)
 
    def printar_tabuleiro(self):
        print('Resultado do ataque: ') # aqui tem a estilização do resultado final da arena.
        print('---------------------------------------------------------------------------------------------------------------')
        print('no lado aliado:')
        print(f'                              Herói: {self.heroi_aliado.getNome()}                                                                   ')
        print(f'                            com {self.heroi_aliado.getPontos_de_vida()} de vida                                                             ')
        print('')
        print(f'{self.lacaio_aliado_1.getNome()} com {self.lacaio_aliado_1.getPontos_de_vida()} de vida | {self.lacaio_aliado_1.getPontos_de_dano()} de dano                 {self.lacaio_aliado_2.getNome()} com {self.lacaio_aliado_2.getPontos_de_vida()} de vida | {self.lacaio_aliado_2.getPontos_de_dano()} de dano ')
        print('---------------------------------------------------------------------------------------------------------------')

        print('No lado inimigo:')
        print(f'                              Inimigo: {self.heroi_inimigo.getNome()}                                       ')
        print(f'                            com {self.heroi_inimigo.getPontos_de_vida()} de vida                                                  ')
        print('')
        print(f'{self.lacaio_inimigo_1.getNome()} com {self.lacaio_inimigo_1.getPontos_de_vida()} de vida | {self.lacaio_inimigo_1.getPontos_de_dano()} de dano           {self.lacaio_inimigo_2.getNome()} com {self.lacaio_inimigo_2.getPontos_de_vida()} de vida | {self.lacaio_inimigo_2.getPontos_de_dano()} de dano')

