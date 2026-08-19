"""
======================================================================
Curso:  Python 3 do Zero ao Avançado (Udemy - Luiz Otávio Miranda)
Módulo: Python Intermediário
Tópico: Higher Order Functions e Closures
Arquivo: order_functions-clousure.py
Autor:  Stwarty J Camara
======================================================================

Descrição:
    Este arquivo demonstra o conceito de funções de ordem superior (Higher Order Functions) e closures em Python,
    mostrando como funções podem ser passadas como argumentos e retornadas como valores.
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


# Exercício
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.


def multiplicador(multiplicado):

    def multiplicar(numero):
        return numero * multiplicado

    return multiplicar


duplicar = multiplicador(2)
triplicar = multiplicador(3)
quadruplicar = multiplicador(4)

print(f"O dobro de 5 é: {duplicar(5)}")  # Saída: 10
print(f"O triplo de 5 é: {triplicar(5)}")  # Saída: 15
print(f"O quadruplo de 5 é: {quadruplicar(5)}")  # Saída: 20

# extra
for i in [1, 2, 3, 4, 5]:
    print(f"O dobro de {i} é: {multiplicador(2)(i)}")  # Saída: 2, 4, 6, 8, 10
    print(f"O triplo de {i} é: {multiplicador(3)(i)}")  # Saída: 3, 6, 9, 12, 15
    print(f"O quadruplo de {i} é: {multiplicador(4)(i)}")  # Saída: 4, 8, 12, 16, 20
