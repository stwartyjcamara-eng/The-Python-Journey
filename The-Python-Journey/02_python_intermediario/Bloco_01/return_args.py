"""
======================================================================
Curso:  Python 3 do Zero ao Avançado (Udemy - Luiz Otávio Miranda)
Módulo: Python Intermediário
Tópico: Return e args
Arquivo: return_args.py
Autor:  Stwarty J Camara
======================================================================

Descrição:
    Este arquivo demonstra o uso de funções com retorno de valor e argumentos em Python.
    Ele inclui exemplos de funções que retornam valores, funções com múltiplos argumentos,
    e funções que utilizam *args para receber um número variável de argumentos.
"""


def soma(a, b):
    """Função que retorna a soma de dois números."""
    return a + b


print(soma(10, 5))  # Saída: 15


def multiplica(a, b):
    """Função que retorna a multiplicação de dois números."""
    return a * b


print(multiplica(10, 5))  # Saída: 50


def operacoes(a, b):
    """Função que realiza operações de soma e multiplicação e retorna os resultados."""
    return soma(a, b), multiplica(a, b)


print(operacoes(10, 5))  # Saída: (15, 50)


def media(*args):
    """Função que calcula a média de um número variável de argumentos."""
    return sum(args) / len(args)


print(media(10, 20, 30))  # Saída: 20.0

x, y, *resto = [1, 2, 3, 4, 5]
print(x, y, resto)  # Saída: 1 2 [3, 4, 5]


def soma(*args):
    """Função que retorna a soma de um número variável de argumentos."""
    return sum(args)


print(soma(1, 2, 3, 4, 5))  # Saída: 15
soma1 = soma(1, 2, 3)
print(soma1)  # Saída: 6
soma2 = soma(4, 5, 6)
print(soma2)  # Saída: 15
numeros = 1, 2, 3, 4, 5
outra_soma = soma(*numeros)  # Usando a função sum() para somar os elementos da tupla
print(outra_soma)  # Saída: 15
print(sum((1, 2, 3, 4, 5)))  # Saída: 15
print(sum(numeros))  # Saída: 15

"""
# Teste
def n(n1):
    if n1 > 1:
        print("numero 1")
    else:
        print("numero 0")


n(int(input("Informe o numero: ")))
"""
