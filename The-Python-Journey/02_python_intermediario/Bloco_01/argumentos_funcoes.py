"""
======================================================================
Curso:  Python 3 do Zero ao Avançado (Udemy - Luiz Otávio Miranda)
Módulo: Python Intermediário
Tópico: Argumentos e Funções
Arquivo: argumentos_funcoes.py
Autor:  Stwarty J Camara
======================================================================

Descrição:
    Para este arquivo, o objetivo é estudar e praticar os conceitos de parâmetros e argumentos de funções em Python,
    incluindo exemplos de funções com diferentes tipos de parâmetros e argumentos.
    O arquivo contém exemplos de funções com parâmetros posicionais, parâmetros nomeados, parâmetros padrão,
    parâmetros arbitrários e parâmetros de palavra-chave arbitrários, bem como exemplos de funções com retorno de valor
    e tratamento de exceções. Além disso, o arquivo também inclui exemplos 
    de funções com múltiplos parâmetros e valores padrão para parâmetros, demonstrando como utilizar esses conceitos em diferentes situações.
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
#Valores padrão para parâmetros:
def soma(x, y, z=0):
    if z:
        print(f"{x=} {y=} {z=}", '|', 'x + y + z =', x + y + z)
    else:
        print(f"{x=} {y=} {z=}", '|', 'x + y + z =', x + y + z)

soma(1, 2) # Chamando a função com dois argumentos, usando o valor padrão para o terceiro
soma(1, 2, 3) # Chamando a função com três

def soma2(x, y, z=None):
    if z is not None:
        print(f"{x=} {y=} {z=}", '|', 'x + y + z =', x + y + z)
    else:
        print(f"{x=} {y=} {z=}", '|', 'x + y + z =', x + y)
soma2(1, 2) # Chamando a função com dois argumentos
soma2(1, 2, 3) # Chamando a função com três

def soma3(x=0, y=0, z=0):
    return x + y + z
print(f'A soma é {soma3()}') # Chamando a função sem argumentos, usando os valores padrão
print(f'A soma é {soma3(1)}') # Chamando a função com um argumento, usando os valores padrão para os outros
print(f'A soma é {soma3(1, 2)}') # Chamando a função com dois argumentos, usando o valor padrão para o terceiro
print(f'A soma é {soma3(1, z=2, y=3)}') # Chamando a função com três argumentos, usando a ordem nomeada para os parâmetros
