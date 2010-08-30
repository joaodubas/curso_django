#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# exercicio_01_identificadores.py - Identificadores ou variaveis no Python

"""
Como sao atribuidos valores a identificadores, como estes devem ser nomeadores e etc.
"""

print '- Identificadores ----------------------------------------------------------------'
print '--- Nomes devem comecao com qualquer caracter ou "_" -----------------------------'
print '--- nao podem ser nomes reservados, caso seja necessario termine com "_" (ex: in_)'
print '--- Atribuicao -------------------------------------------------------------------'
print '------ Simples (= ) --------------------------------------------------------------'
a = 0
print 'a = 0'
print '------ Aumentada (augmented) -----------------------------------------------------'
a += 5
print 'a += 5 (%d)' % a
a -= 1
print 'a -= 1 (%d)' % a
a *= 2
print 'a *= 2 (%d)' % a
a /= 4
print 'a /= 4 (%d)' % a
a **= 2
print 'a **= 2 (%d)' % a
print '------ Por tupla -----------------------------------------------------------------'
b,c = a**2, a**1/2
print 'b,c = a**2, a**1/2\n(b = %d, c = %d)' % (b, c)