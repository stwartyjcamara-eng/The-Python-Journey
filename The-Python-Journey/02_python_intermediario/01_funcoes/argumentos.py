"""
======================================================================
Curso:  Python 3 do Zero ao Avançado (Udemy - Luiz Otávio Miranda)
Módulo: Python Intermediário
Tópico: Argumentos de Funções
Arquivo: argumentos.py
Autor:  Stwarty J Camara
======================================================================

Descrição:
    Arquivo de estudo sobre argumentos de funções em Python, incluindo exemplos de funções com argumentos posicionais, 
    argumentos nomeados, argumentos padrão, argumentos arbitrários e argumentos de palavra-chave arbitrários.
"""
def soma(a, b):
    print(f'{a=} {b=}', '|', 'a + b =', a + b)
soma(5, 3)  # Chamando a função com argumentos posicionais
soma(b=3, a=5)  # Chamando a função com argumentos nomeados
