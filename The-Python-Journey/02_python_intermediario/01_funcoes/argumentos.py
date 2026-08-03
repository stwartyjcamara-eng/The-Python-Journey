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
soma(a=3, b=5)  # Chamando a função com argumentos nomeados
# Argumentos padrão
def saudacao(nome, mensagem='Olá'):
    print(f'{mensagem}, {nome}!')
saudacao('Alice')  # Usando o argumento padrão
saudacao('Bob', 'Oi')  # Sobrescrevendo o argumento padrão
# Argumentos arbitrários
def soma_numeros(*args):
    resultado = sum(args)
    print(f'Soma dos números {args} = {resultado}')
soma_numeros(1, 2, 3, 4, 5)  # Chamando a função com múltiplos argumentos arbitrários
# Argumentos de palavra-chave arbitrários
def imprimir_info(**kwargs):
    for chave, valor in kwargs.items():
        print(f'{chave}: {valor}')
imprimir_info(nome='Alice', idade=30, cidade='São Paulo')  # Chamando a função com múltiplos argumentos de palavra-chave arbitrários
# Exemplo de função com todos os tipos de argumentos
def exemplo_completo(a, b=2, *args, **kwargs):
    print(f'{a=} {b=}', '|', 'args =', args, '|', 'kwargs =', kwargs)
exemplo_completo(1, 3, 4, 5, nome='Alice', idade=30)  # Chamando a função com todos os tipos de argumentos
def numeros(a, b, c):
    print(f'{a=} {b=} {c=}')
numeros(1, 2, 3)  # Chamando a função com argumentos posicionais
numeros(1, b=2, c=3)  # Chamando a função com um argumento posicional e dois argumentos nomeados
# numeros(a=1, b=2, 3)  # Causará um erro, pois argumentos posicionais não podem seguir argumentos nomeados
