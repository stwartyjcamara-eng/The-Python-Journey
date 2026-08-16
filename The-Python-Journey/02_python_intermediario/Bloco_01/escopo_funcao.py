"""
======================================================================
Curso:  Python 3 do Zero ao Avançado (Udemy - Luiz Otávio Miranda)
Módulo: Python Intermediário
Tópico: Escopo de Funções
Arquivo: escopo_funcao.py
Autor:  Stwarty J Camara
======================================================================

Descrição:
    Este arquivo demonstra o conceito de escopo de funções
    em Python, mostrando a diferença entre variáveis globais
    e locais.
"""

# Escopo significa a região do código onde uma variável é reconhecida.
# Existem dois tipos de escopo: global e local.
# Escopo global: Variáveis definidas fora de qualquer função, acessíveis em todo o código.
escopo_global = "Eu sou uma variável global"


def funcao():
    # Escopo local: Variáveis definidas dentro de uma função, acessíveis apenas dentro dessa função.
    escopo_local = "Eu sou uma variável local"
    print(escopo_global)  # Acessa a variável global
    print(escopo_local)  # Acessa a variável local


funcao()


def funcao2():
    x = "10"  # Variável local dentro da função funcao2
    print(
        f"Valor de x dentro da função: {int(x)}"
    )  # Converte a variável local x para inteiro e imprime


# print(f"Valor de x fora da função: {x}") Isso causará um erro, pois x não está definido no escopo global
funcao2()  # Chamando a função funcao2 para demonstrar o escopo local


def escopo():
    x = 10  # Variável local dentro da função escopo

    def escopo_interno():
        y = 5  # Variável local dentro da função escopo_interno
        print(
            f"Valor de x dentro da função escopo_interno: {x}"
        )  # Acessa a variável x do escopo externo
        print(
            f"Valor de y dentro da função escopo_interno: {y}"
        )  # Acessa a variável y do escopo interno

        def escopo_interno2():
            x = 20  # Variável local dentro da função escopo_interno2
            y = 15  # Variável local dentro da função escopo_interno2
            print(f"Valor de x dentro da função escopo_interno2: {x}")
            print(f"Valor de y dentro da função escopo_interno2: {y}")

        escopo_interno2()  # Chamando a função escopo_interno2 para demonstrar o escopo local

    escopo_interno()  # Chamando a função escopo_interno para demonstrar o escopo local
    # print(f"Valor de y fora da função escopo_interno: {y}") Isso causará um erro, pois y não está definido no escopo da função escopo


escopo()  # Chamando a função escopo


def escopo_global():
    x = 10  # Atribuindo um valor à variável global x
    print(
        f"Valor de x dentro da função escopo_global: {x}"
    )  # Acessa a variável global x

    def escopo_local():
        global x  # Declarando x como uma variável global dentro da função escopo_local
        x = 5  # Variável local dentro da função escopo_local
        print(
            f"Valor de x dentro da função escopo_local: {x}"
        )  # Acessa a variável local x

    escopo_local()  # Chamando a função escopo_local para demonstrar o escopo global


escopo_global()  # Chamando a função escopo_global para demonstrar o uso de a variável global
print(f"Valor de x fora das funções: {x}")  # Acessa a variável global x
# Sempre acessivel de dentro para fora, mas não o contrário. Variáveis locais só são acessíveis dentro da função onde foram definidas.

"""
Retorno de funções: Uma função pode retornar um valor usando a palavra-chave 
return. 
O valor retornado pode ser usado em outras partes do código.
"""


def soma(a, b):
    # print(a + b) # Imprime a soma de a e b # erro, pois a função soma não retorna nenhum valor, apenas imprime a soma
    return a + b  # Retorna a soma de a e b


soma1 = soma(5, 3)  # Chamando a função soma e armazenando o resultado em soma1
print(f"A soma de 5 e 3 é: {soma1}")  # Agora irá imprimir o resultado da soma
