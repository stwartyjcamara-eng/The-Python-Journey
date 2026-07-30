"""
Introdução às funções em Python
Funções são blocos de código que podem ser reutilizados em diferentes partes do programa. Elas ajudam a organizar o código, tornando-o mais legível e fácil de manter. 
Em Python, funções são definidas usando a palavra-chave `def` seguida pelo nome da função e parênteses.
Por padrão, funçoes retornam None, mas podem retornar valores usando a palavra-chave `return`.
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

