# CodeSmells_Refator

## Refatoramento do código do trabalho do primeiro semestre para o curso de *CodeSmells?* 

>Uma única jogada de HeartStone

## **HeartStone**: o que é?
  ![exemplo do jogo](https://imag.malavida.com/mvimgbig/download-fs/hearthstone-15581-4.jpg)

### de forma resumida, HeartStone é um jogo de cartas onde cada jogador pode escolher um heroi e um deck de cartas possuindo lacaios e magias. 

#### Nesse exemplo serão postos no tabuleiro: 2 Herois (Aliado e Inimigo) e 2 Lacaios para cada heroi

Regras:
>- Cada heroi pode começar com até no mínimo *1* e no máximo *30* pontos de vida.
>- Cada Lacaio pode começar com no mínimo *1* e no máximo *10* pontos de vida.
>- Lacaios são utilizados para o ataque nesse código, onde podem ter no mínimo *0* e no máximo *10* pontos de dano.
>- Lacaios podem atacar tanto um dos lacaios inimigos como o heroi inimigo.
>- Quando um Lacaio bate em outro, ambos são diminuidos de seus pontos de vida, os pontos de dano do lacaio oponente.
>- Se um lacaio chegar a *0* de pontos de vida ele é morto, se um heroi chegar a *0* de vida, seu oponente vence.
