#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# exercicio_02_comandos.py - Comandos de fluxo do Python

"""
Aprensetacao dos comandos de controle de fluxo do Python
"""

print '- if/elif/else -------------------------------------------------------------------'
a = input('a: ')
b = input('b: ')
mensagem = 'A e %s B'
condicao_list =['menor do que', 'maior do que', 'igual a']
condicao = ''

if a > b:
    condicao = condicao_list[1]
elif a > b:
    condicao = condicao_list[0]
else:
    condicao = condicao_list[2]

print mensagem % condicao

c = ('a>0' if a > 0 else 'a<=0')    # operador ternario

print 'c = %s' % c

print '- while --------------------------------------------------------------------------'
import sys
import time

d = raw_input('Despertar em (hh:mm): ')
while time.strftime('%H:%M') != d:
    try:
        print '\b\b\b\btick'
        sys.stdout.flush()
        print '\b\b\b\btack'
        sys.stdout.flush()
        time.sleep(0.5)
    except KeyboardInterrupt:
        break
else:
    print '\n\nTRIM!\a\a\a'
    sys.exit(0)
print '\n\nInterrompido!'

print '- for ----------------------------------------------------------------------------'
e = [ ('chave1', 'valor1'), ('chave2', 'valor2'), ('chave3', 'valor3')]
for k, v in e:
    print 'chave: %s \t valor: %s' % (k, v)

f = ['spam', 'eggs', 'foo', 'bar', 'qoox']
for idx, elm in enumerate(f):
    print '%d \t %s' % (idx, elm)

print '- exec ---------------------------------------------------------------------------'
print '--- exec "a = 1"'
exec 'a = 1'
print ' a = %d' % a
