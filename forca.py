# -*- coding: utf-8 -*-
"""
Created on Wed May 20 12:20:05 2020

@author: mayco
"""


from funcoes.desenho import forca, telainicial
from dicas.palavras import sorteiap

continuar = 'S'
partidas=vitorias=derrotas = 0 #cria variaves para armazenar nro de partidas, vitorios e derrotas e inseri 0 como default

print('\n'*20) # limpa a tela
telainicial()
jogador = input(str('Digite o Nome do Jogador: ')) #Solicita e guarda nome do Jogador



while continuar in 'Ss': 
    
    erros=0
    partidas +=1 #Incrementa o nro de partidas em +1
    
    #SORTEIA PALAVRA E DICA INICIAL 
    
    lletras = list()
    dadospalavra = list() #cria lista que vai receber os dados da palavra sorteada
    listasorteio = sorteiap() #roda função que gera a palavra e dica aleatória
    vlistap = listasorteio.split('|') #explode string recebida
    dadospalavra.append(vlistap) #joga string em uma lista para resgatar os dados

    for x in range(0,len(dadospalavra)):    
        word = dadospalavra[x][0] #resgata palavra
        dicauser = dadospalavra[x][1] #resgata dica

    temp=[]

    for letra in word:
        temp.append('_')
 
    while True:
        
        
        print('\n'*20) # limpa a tela
        forca(erros, jogador) # imprime desenho da forca

        #Imprime a Dica
        print(f'Dica: {dicauser}')
    
        #imprime a adivinhacao
        print('\n\nAdivinhe: ', end='')

        for let in temp:
            print(let, end=' ')
        print('\n'*2)

        #Verifica se perdeu
        if erros==6:
            derrotas +=1 #Incrementa o nro de derrotas em +1
            print(f'\n LAMENTO {jogador}, VOCÊ PERDEU!!!')
            print('')
            print(f'Total Partidas: {partidas}')
            print(f'Total Vitórias: {vitorias}')
            print(f'Total Derrotas: {derrotas}')
            print('\n'*2)
            continuar = str(input('Deseja Jogar Novamente? S/N : ')).upper().strip()[0]
            break #sai do jogo (sai do while)
            

        #Verificar se o jogador ganhou
        ganhouJogo=True
        for let in temp:
            if let=='_':
                ganhouJogo=False
    
        if ganhouJogo:
            vitorias +=1 #Incrementa o nro de vitorias em +1
            print(f'\n PARABÉNS {jogador}, VOCE ACERTOU!!!')
            print('')
            print(f'Total Partidas: {partidas}')
            print(f'Total Vitórias: {vitorias}')
            print(f'Total Derrotas: {derrotas}')
            print('\n'*2)
            continuar = str(input('Deseja Jogar Novamente? S/N : ')).upper().strip()[0]
            
            break

        #captura a letra do usuario
        print(f'LETRAS JÁ DIGITADAS:')
        print(lletras)
        letraDig=input("Informe uma letra: ")
        letraDig = letraDig.upper() #transforma a letra em caixa alta
        lletras.append(letraDig)
        
        
        #verifica se acertou alguma letra
        errouLetra=True
        for i, let in enumerate(word):
            if word[i]==letraDig:
                temp[i]=word[i]
                errouLetra=False
        if errouLetra:
            erros=erros+1
                
        
