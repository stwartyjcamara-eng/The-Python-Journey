"""
Operadores de atribuição
= += -= *= /= //= **= %=
"""
# Atribuição simples
x = 10
print(f'Valor inicial de x: {x}')
# Atribuição com adição
x += 5  # Equivalente a x = x + 5
print(f'Após x += 5: {x}')
# Atribuição com subtração
x -= 3  # Equivalente a x = x - 3
print(f'Após x -= 3: {x}')
# Atribuição com concatenação de strings
nome = "João"
print(f'Nome inicial: {nome}')
nome += " Silva"  # Equivalente a nome = nome + " Silva"
print(f'Após nome += " Silva": {nome}')
# Atribuição com concatenação de strings e inteiros
idade = 25
print(f'Idade inicial: {idade}')
idade_str = " anos"
idade_str += str(idade)  # Convertendo inteiro para string antes da concatenação
print(f'Após idade_str += str(idade): {idade_str}')
# Atribuição com concatenação de strings numeros
numero_str = "2"
numero = 10  
numero_str *= numero # Equivalente a numero_str = numero_str * numero
print(f'Após numero_str += numero: {numero_str}')

