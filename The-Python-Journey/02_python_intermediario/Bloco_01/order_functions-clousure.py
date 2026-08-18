"""
======================================================================
Curso:  Python 3 do Zero ao Avançado (Udemy - Luiz Otávio Miranda)
Módulo: Python Intermediário
Tópico: Higher Order Functions e Closures
Arquivo: order_functions-clousure.py
Autor:  Stwarty J Camara
======================================================================

Descrição:
    Este arquivo demonstra o uso de funções de ordem superior e closures em Python.
    Ele inclui exemplos de funções que recebem outras funções como argumentos,
    e funções que retornam outras funções, permitindo a criação de closures.
"""

# Hier order function - Funções de primeira classe


def saudacao(msg, nome):
    """Função que retorna uma saudação."""
    return f"Olá, {msg}, {nome}!\n"


def executa(funcao, *args):
    """Função que executa outra função com os argumentos fornecidos."""
    return funcao(*args)


print(executa(saudacao, "Mundo", "Alice"))  # Saída: Olá, Mundo, Alice!
print(executa(saudacao, "Python", "Bob"))  # Saída: Olá, Python, Bob!

# Closure - Funções que retornam outras funções


def criar_saudacao(saudacao):
    """Função que cria uma saudação personalizada."""

    def saudacao_interna(nome):
        return f"Olá, {saudacao}, {nome}!\n"

    return saudacao_interna


saudacao1 = criar_saudacao("Bom dia")
saudacao2 = criar_saudacao("Boa noite")

for nome in ["Alice", "Bob", "Charlie"]:
    print(saudacao1(nome))
    print(saudacao2(nome))

print(saudacao1("Luiz"))  # Saída: Olá, Bom dia, Luiz!
print(saudacao2("Maria"))  # Saída: Olá, Boa noite, Maria!
