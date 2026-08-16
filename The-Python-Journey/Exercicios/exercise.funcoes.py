"""
======================================================================
Exercício: Exercicio do curso Python Intermediário - Funções
Tópico:    Python Intermediário - Funções
Origem:    Curso Udemy / LeetCode / HackerRank
Arquivo:   exercise.funcoes.py
Autor:     Stwarty J Camara
======================================================================

Enunciado:
Escreva uma função que multiplique todos os argumentos não nomeados recebidos e retorne o total para uma variavel e mostre o valor da variavel.
Escreva uma função que receba um número inteiro e retorne se ele é par ou ímpar.

"""

total = 1


def mutiplica(*args):
    global total
    total = 1
    for numero in args:
        total *= numero
    return total


mutiplica(2, 3, 4)
print(f"O resultado é: {total}")  # Resultado esperado 24


def par_impar(numero):
    if numero % 2 == 0:
        print(f"O número {numero} é par")
    else:
        print(f"O número {numero} é ímpar")


par_impar(3)
par_impar(4)

# Bonus: Função que recebe múltiplos números e verifica se são pares ou ímpares


def par_impar2(*numero):
    for n in numero:
        if n % 2 == 0:
            print(f"O número {n} é par")
        else:
            print(f"O número {n} é ímpar")


par_impar2(3, 4, 5, 6, 7)  # Resultado esperado: ímpar, par, ímpar, par, ímpar
