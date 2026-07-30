"""
======================================================================
Curso:  Python 3 do Zero ao Avançado (Udemy - Luiz Otávio Miranda)
Módulo: Python Intermediário
Tópico: Funções
Arquivo: funcoes.py
Autor:  Stwarty J Camara
======================================================================

Descrição:
    Introdução às funções em Python, incluindo exemplos de funções simples, funções com parâmetros, funções com retorno de valor e funções com múltiplos parâmetros.
"""

# Exemplo de função simples:
def minha_funcao():
    print("Olá, esta é a minha função!")
print(minha_funcao)  # Mostrando a referência da função
minha_funcao()  # Chamando a função

# outro exemplo de função com parâmetros:
def saudacao(nome):
    print(f"Olá, {nome}! Bem-vindo(a)!")
saudacao("Stwarty")  # Chamando a função com argumento

# Função com retorno de valor:
def soma(a, b):
    return a + b
resultado = soma(5, 3)  # Chamando a função e armazenando o resultado
print(f"A soma de 5 e 3 é: {resultado}")

# Função com múltiplos parâmetros:
def nomes(a, b, c):
    return f"Os nomes são: {a}, {b} e {c}"
print(nomes("Alice", "Bob", "Charlie"))  # Chamando a função com múltiplos argumentos
print(nomes('Stwarty', 'Camara', 'Junior'))  # Chamando a função com múltiplos argumentos

