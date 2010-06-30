#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# exercicio_01.py - Primeiro programa
'''
Importa o módulo random e sorteia um número inteiro entre 1 e 100
'''
import random
numero = random.randint(1, 100)

escolha, tentativas = 0, 0

while escolha != numero:
    escolha = input("Escolha um numero entre 1 e 100: ")
    tentativas += 1

    if escolha < numero:
        print "O numero %d e menor do que o numero sorteado." % escolha
    elif escolha > numero:
        print "O numero %d e maior do que o numero sorteado." % escolha

print "Parabens! Voce acertou com %d tentativas." % tentativas
