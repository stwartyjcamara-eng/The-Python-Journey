"""
======================================================================
Exercício: escopo e Argumentos em Funções
Tópico:    Python Intermediário - Funções
Origem:    Curso Udemy / LeetCode / HackerRank
Arquivo:   exercise_escopo_e_argumentos.py
Autor:     Stwarty J Camara
======================================================================
"""

"""
Exercício 1: Calculadora de Desconto com Argumentos Opcionais
Foco: Parâmetros posicionais, parâmetros nomeados e valores padrão (default).

Enunciado:
Crie uma função chamada calcular_preco_final que recebe:

valor_base (obrigatório, numérico)


taxa_entrega (padrão 12.0)

cupom (opcional, padrão None)

Regras:

Se cupom for "PROMO10", adicione um desconto extra fixo de R$ 10,00.

A função deve calcular: (valor_base - desconto - extra_cupom) + taxa_entrega.

Retorne o valor final formatado ou numérico.
"""


def calcular_preco_final(valor_base, taxa_entrega=12.0, cupom=None):
    desconto = 0
    extra_cupom = 0

    if cupom == "PROMO10":
        extra_cupom = 10.0

    preco_final = (valor_base - desconto - extra_cupom) + taxa_entrega
    return preco_final


print(calcular_preco_final(100))  # Sem cupom, taxa de entrega padrão
print(calcular_preco_final(100, cupom="PROMO10"))  # Com cupom, taxa de entrega padrão
print(
    calcular_preco_final(100, taxa_entrega=15.0, cupom="PROMO10")
)  # Com cupom e taxa de entrega personalizada


"""
Exercício 1: Escopo Local vs. Global & global
Objetivo: Compreender como funções acessam e modificam variáveis fora do seu bloco.

Enunciado:
Crie um programa que gerencie um saldo inicial de 100.0 em uma variável global chamada saldo_total.

Escreva uma função consultar_saldo() que apenas imprima o saldo atual sem alterá-lo.

Escreva uma função depositar(valor) que receba um valor e modifique a variável global saldo_total.

Escreva uma função saque(valor) que receba um valor e subtraia do saldo_total, mas apenas se o saldo for suficiente. Caso contrário, imprima uma mensagem de erro.

"""
saldo_total = 100.0  # Variável global para o saldo total


def consultar_saldo():
    print(f"Saldo atual: R$ {saldo_total:.2f}")  # Acessa a variável global saldo_total

    def depositar(valor):
        global saldo_total
        saldo_total += valor

        def saque(valor):
            global saldo_total
            if valor <= saldo_total:
                saldo_total -= valor
            else:
                print("Saldo insuficiente para saque.")

        saque(500)  # Chamando a função saque para subtrair do saldo_total

    depositar(1000)  # Chamando a função depositar para adicionar ao saldo_total


consultar_saldo()  # Chamando a função consultar_saldo para verificar o saldo atualizado
