#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# exercicio_01.py - Primeiro programa

"""
Importa o módulo random e sorteia um número inteiro entre 1 e 100
"""

import random

numero = random.randint(1, 100) # numero sorteado aleatoriamente

escolha, tentativas = 0, 0  # definindo o numero de tentativas e a escolha do usuario

mensagem = "O numero %d e %s do que o numero sorteado"  # mensagem apresentada ao usuario

posicao_escolha = ""    # variavel a ser usada para definir se escolha > || < numero

while escolha != numero:
    escolha = input("Escolha um numero entre 1 e 100: ")
    tentativas += 1

    if escolha < numero:
        posicao_escolha = "menor"
    elif escolha > numero:
        posicao_escolha = "maior"
    
    print mensagem % (escolha, posicao_escolha)

print "Parabens! Voce acertou com %d tentativas." % tentativas
