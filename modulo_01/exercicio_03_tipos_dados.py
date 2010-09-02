#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# exercicio_03_tipos_dados.py - Estudo dos tipos de dados built-in do Python

import sys
"""
Estudo dos tipos de dados built-in do Python, sua classificacao como mutavel ou imutavel
"""

#- Tipos numerico ------------------------------------------------------------------------
print 'Maior inteiro setado no sistema %d' % sys.maxint
print 'O numero %d e do tipo %s' % (1, type(1))
print 'O numero %X e do tipo %s' % (0xFF, type(0xFF))   # Hexadecimal
print 'O numero %o e do tipo %s' % (034, type(034)) # Octal
print 'O numero %d e do tipo %s' % (50L, type(50L))
print 'O numero %d e do tipo %s' % (0xFFFFFFFFFF, type(0xFFFFFFFFFF))   # Hexadecimal
print '%d + %d = %d (do tipo %s)' % (sys.maxint, 1, sys.maxint + 1, type(sys.maxint + 1))
print '%s para inteiro int("%s", <opcional> base)' % ('123', '123')
print 'O numero %g e do tipo %s' % (1.5, type(1.5))
print 'O numero %g e do tipo %s' % (1e-10, type(1e-10))
print 'O numero %g e do tipo %s (mesmo para numero positivos)' % (1e10, type(1e10))
"""
Lembre-se de utilizar a biblioteca decimal em casos onde trabalho com pontos flutuantes
envolver aplicacoes financeiras ou cientificas, uma vez que a biblioteca padrao possui
precisao relativa e nao absoluta
"""