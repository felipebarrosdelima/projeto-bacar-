
# EP - Design de Software 
# Equipe: Felipe Barros de Lima  e João Pedro de Souza Costa Ferreira
# Data: 14/10/2020
import random

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

       

    if soma_banca != 6 and soma_banca < 6:#Se a soma das duas cartas do banco for igual a 6 ou mais, ele não recebe a terceira carta
        if soma_banca <=5 and soma_jogador < 8 or soma_jogador > 9 : # Condição para distribuir a terceira carta
            Mão_Banca.append(random.choice(Valores_cartas))
            soma_banca = sum(Mão_Banca)

    if soma_jogador <=5 and soma_banca < 8 or soma_banca > 9: # Condição para distribuir a terceira carta
        terceira_carta=random.choice(Valores_cartas)#valor da terceira carta
        Mão_jogador.append(terceira_carta)
        soma_jogador = sum(Mão_jogador)

        if soma_banca<=5: # condição para que se o jogador receber uma terceira carta e a soma das duas cartas do banco for menor ou igual a 5, o banco recebe a terceira carta de acordo com a condições abaixo
            if soma_banca==0:# condilção para se a soma da banca for igual a zero mais uma cata é distribuida independente da treceira carta do jogador
                Mão_Banca.append(random.choice(Valores_cartas))
            if soma_banca==1:#condilção para se a soma da banca for igual a 1 mais uma cata é distribuida independente da terceira carta do jogador
                Mão_Banca.append(random.choice(Valores_cartas))
            if soma_banca==2:#condilção para se a soma da banca for igual a 2 mais uma cata é distribuida independente da terceira carta do jogador
                Mão_Banca.append(random.choice(Valores_cartas))
            if soma_banca==3 and terceira_carta !=8:#condilção para se a soma da banca for igual a 3 mais uma cata é distribuida se a terceira carta do jogador for diferente de 8
                Mão_Banca.append(random.choice(Valores_cartas))
            if soma_banca==4 and terceira_carta>1 and terceira_carta<8:#condilção para se a soma da banca for igual a 4 mais uma cata é distribuida se a terceira carta do jogador não for 0, 1, 8, 9
                Mão_Banca.append(random.choice(Valores_cartas))
            if soma_banca==5 and terceira_carta>3 and terceira_carta<8: #condilção para se a soma da banca for igual a 5 mais uma cata é distribuida se a terceira carta do jogador não for 0, 1, 3, 8 e 9
                Mão_Banca.append(random.choice(Valores_cartas))
    else:
        if soma_banca<=5:#soma das duas cartas do banco for menor ou igual a 5, ele recebe a terceira carta;
            Mão_jogador.append(random.choice(Valores_cartas))
            soma_jogador = sum(Mão_jogador)



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

        

  
    





