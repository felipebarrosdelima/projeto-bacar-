
# EP - Design de Software 
# Equipe: Felipe Barros de Lima  e João Pedro de Souza Costa Ferreira
# Data: 14/10/2020
import random
q_jogadores=int(input('quantos jogadores tem no jogo '))


fj = (int(input('Digite quantas fichas você deseja colocar no jogo '))) #fj refere-se a variável que vai guardar quantas fichas o jogador vai colocar no jogo.

Cartas = ['A','A','A','A',2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,'J','J','J','J','Q','Q','Q','Q','K','K','K','K'] #Lista do baralho

Valores_cartas =[1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]*6 # Lista dos valores das Cartas 

count = 0 
Mão_jogador = []
Mão_Banca = []

while fj > 0: #Looping utilizado para fazer com que o jogador continue jogando até que suas fichas acabem
    aposta = (int(input('Digite quanto você deseja apostar '))) #aposta refere-se a variável que vai guardar o quanto o jogador quer apostar
    destino_aposta = input('Digite em quem você quer apostar? Opções: Banca, Empate, Jogador. ')
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
    if soma_jogador <=5 and soma_banca < 8 or soma_banca > 9: # Condição para distribuir a terceira carta
        Mão_jogador.append(random.choice(Valores_cartas))
        soma_jogador = sum(Mão_jogador)
    if soma_banca <=5 and soma_jogador < 8 or soma_jogador > 9 : # Condição para distribuir a terceira carta
        Mão_Banca.append(random.choice(Valores_cartas))
        soma_banca = sum(Mão_Banca)

    if soma_jogador >= 10: # Condição para falar que se por exemplo a soma der 12 então o valor real é 2 etc...
        soma_jogador -=10
    if soma_banca >= 10: # Condição para falar que se por exemplo a soma der 12 então o valor real é 2 etc...
        soma_banca -=10  
    
    if soma_banca == soma_jogador: # Verifica se deu empate
        print('Empate!')
        A = True
    else:
        A = False
    if soma_banca > soma_jogador: # Verifica se a banca venceu 
        print('A banca venceu')
        B = True
    else:
        B = False     
    if soma_jogador > soma_banca:  # Verifica se o Jogador venceu 
        print('O jogador venceu')
        C = True
    else:
        C = False


    if destino_aposta == 'Empate' and A == True: # Distribui os ganhos para caso o jogador menos a taxa do casino tenha apostado no empate e acertado
        fj  += aposta*8-((14.44/100)*aposta*8)
    if destino_aposta == 'Jogador' and C == True: # Distribui o lucro menos a taxa do casino para caso o jogador  tenha apostado no jogador e acertado
        fj += aposta*2-((1.24/100)*aposta*2)
    if destino_aposta =='Banca' and B == True: # Distribui o lucro para caso o jogador menos a taxa do casino tenha apostado na banca e acertado
        fj += aposta*1.95-((1.06/100)*aposta*1.95)
    
    
    print('Você está com ', fj , 'fichas')
    print(f'os valores das cartas do jogador são{Mão_jogador},os valores das cartas do banca são{Mão_Banca}')
    print(f'a soma do valor das cartas do jogador é {soma_jogador}, a soma do das cartas da banca é{soma_banca}')    
    list.clear(Mão_Banca)
    list.clear(Mão_jogador)   

        

  
    






