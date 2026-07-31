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

# Função com retorno de valor e tratamento de exceções:
def soma2(a, b):
    return a + b
while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = soma2(num1, num2) # Chamando a função e armazenando o resultado
        print(f"A soma de {num1} e {num2} é: {resultado}")
        break  # Sai do loop se a entrada for válida
    except ValueError:
        print("Por favor, digite apenas números válidos.")

# Função com múltiplos parâmetros:
def nomes(a, b, c):
    return f"Os nomes são: {a}, {b} e {c}"
print(nomes("Alice", "Bob", "Charlie"))  # Chamando a função com múltiplos argumentos
print(nomes('Stwarty', 'Camara', 'Junior'))  # Chamando a função com múltiplos argumentos

