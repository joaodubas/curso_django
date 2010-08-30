#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# exercicio_01_tipo.py - Tipos do Python

"""
Demonstracao dos tipos disponiveis no Python
"""

print '- Numeros ------------------------------------------------------------------------'

print '--- Inteiros ---------------------------------------------------------------------'
print '------ Soma:\n%d + %d = %d' % (2, 2, 2+2)
print '------ Subtracao\n%d - %d = %d' % (4, 2, 4-2)
print '------ Divisao\n%d / %d = %d' % (8, 2, 8/2)
print '------ Multiplicacao\n%d * %d = %d' % (2, 4, 2*4)
print '------ Potenciacao\n%d ** %d = %d' % (2, 3, 2**3)
print '------ Ordem de execucao\n%d * %d / %d + %d = %d' % (2, 2, 4, 1, 2*2/4+1)
print '------ Resto\n%d %s %d = %d' % (5, '%', 2, 5%2)

print '--- Ponto flutuante --------------------------------------------------------------'
print '------ Divisao\n%f / %d = %f' % (3.0, 2, 3.0/2)
print '------ Divisao\n%d / %f = %f' % (3, 2.0, 3/2.0)
print '------ Divisao\n%f / %f = %f' % (3.0, 2.0, 3.0/2.0)
print '------ Divisao de inteiro\n%f // %f = %f' % (3.0, 2.0, 3.0//2.0)

print '--- Bitwise ----------------------------------------------------------------------'
print '------ & -------------------------------------------------------------------------'
print '%d & %d = %d' % (1, 1, 1&1)
print '%d & %d = %d' % (1, 0, 1&0)
print '%d & %d = %d' % (0, 1, 0&1)
print '%d & %d = %d' % (0, 0, 0&0)
print '------ | -------------------------------------------------------------------------'
print '%d | %d = %d' % (1, 1, 1|1)
print '%d | %d = %d' % (1, 0, 1|0)
print '%d | %d = %d' % (0, 1, 0|1)
print '%d | %d = %d' % (0, 0, 0|0)
print '------ ^ -------------------------------------------------------------------------'
print '%d ^ %d = %d' % (1, 1, 1^1)
print '%d ^ %d = %d' % (1, 0, 1^0)
print '%d ^ %d = %d' % (0, 1, 0^1)
print '%d ^ %d = %d' % (0, 0, 0^0)
print '------ ~ (complemento de 2) ------------------------------------------------------'
print '~%d = %d' % (1, ~1)
print '~%d = %d' % (0, ~0)
print '------ >> (deslocamento a direita) -----------------------------------------------'
print '%d >> %d = %d' % (32, 2, 32 >> 2)
print '------ << (deslocamento a esquerda) ----------------------------------------------'
print '%d << %d = %d' % (1, 2, 1 << 2)

print '- Booleano -----------------------------------------------------------------------'
print 'bool(%d > %d) = %s' % (3, 2, bool(3>2))
print 'True ou False'
print 'bool(0) = %s' % bool(0)
print 'bool([]) = %s' % bool([])
print 'bool(()) = %s' % bool(())
print 'bool({}) = %s' % bool({})
print 'bool("") = %s' % bool("")
print 'bool(set()) = %s' % bool(set())
print 'bool(None) = %s' % bool(None)
print '--- Operadores == , !=, >, >=, <, <=, is, is not, and, or, in, not in ------------'
