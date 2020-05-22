# -*- coding: utf-8 -*-
"""
Created on Wed May 20 13:17:37 2020

@author: mayco
"""

import random



def sorteiap():
    '''
    ->Gera um nro randômico e procura no arquivo dicas/pd.txt qual palavra e 
    dica que corresponde a nro gerado

    Returns
    -------
    vretorno : TYPE STR
        DESCRIPTION. RETORNA STRING NO FORMATO 'PALAVRA|DICA' COM A PALAVRA E 
        DICA ENCONTRADA NO TXT

    '''
    
    #gera nro randômico
    nrodica = random.randrange(1,38)
    arquivo = open('dicas/pd.txt','r')
    dados = list()
    
    #procura nro randômico gerado no arquivo da variável 'arquivo'
    for linha in arquivo:
        vlista = linha.split('|')
        dados.append(vlista)
            
        for x in range(0,len(dados)):    
            vnrdica = int(dados[x][0])
            if vnrdica == nrodica:
                vpalavra = dados[x][1]
                vdica = dados[x][2]
    #fecha arquivo
    arquivo.close()
    
    #joga palavra e dica encontrada no txt para a variavel vretorno
    vretorno = vpalavra+'|'+vdica
    
    return  vretorno