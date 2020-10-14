# EP - Design de Software 
# Equipe: Felipe Barros de Lima  e João Pedro de Souza Costa Ferreira
# Data: 14/10/2020
import random
fj = (int(input('Digite quantas fichas você deseja colocar no jogo '))) #fj refere-se a variável que vai guardar quantas fichas o jogador vai colocar no jogo.

Cartas = ['A','A','A','A',2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,'J','J','J','J','Q','Q','Q','Q','K','K','K','K'] #Lista do baralho

Valores_cartas =[1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] # Lista dos valores das Cartas 
count = 0 
Mão_jogador = []
Mão_Banca = []

while fj > 0: #Looping utilizado para fazer com que o jogador continue jogando até que suas fichas acabem
    aposta = (int(input('Digite quanto você deseja apostar '))) #aposta refere-se a variável que vai guardar o quanto o jogador quer apostar
    destino_aposta = input('Digite em quem você quer apostar? Opções: Banca, Empate, Jogador ')
    if aposta <=fj: #Condição que valida a aposta do jogador, e se for valida ja subtrai-se tal valor da variável fj
        fj -= aposta
    else: 
        print('Você não possui esse valor para apostar ')
    while count <=1: #Preenche a lista Mão_jogador Mão_Banca
        carta_jogador = random.choice(Valores_cartas)
        carta_banca = random.choice(Valores_cartas)
        Mão_jogador.append(carta_jogador)
        Mão_Banca.append(carta_banca)
        count +=1
    count = 0 
    soma_jogador = sum(Mão_jogador) #Variável para guardar a soma da lista Mão_jogador
    soma_banca = sum(Mão_Banca) #Variável para guardar a soma da lista Mão_Banca
    
    if soma_jogador >= 10: # Condição para falar que se por exemplo a soma der 12 então o valor real é 2 etc...
        soma_jogador -= 10 
    if soma_banca >= 10: # Condição para falar que se por exemplo a soma der 12 então o valor real é 2 etc...
        soma_banca -=10       
    
    if soma_jogador <=5: # Condição para distribuir a terceira carta
        Mão_jogador.append(random.choice(Valores_cartas))
        soma_jogador = sum(Mão_jogador)
    if soma_banca <=5: # Condição para distribuir a terceira carta
        Mão_Banca.append(random.choice(Valores_cartas))
        soma_banca = sum(Mão_Banca)

        

        

  
    





