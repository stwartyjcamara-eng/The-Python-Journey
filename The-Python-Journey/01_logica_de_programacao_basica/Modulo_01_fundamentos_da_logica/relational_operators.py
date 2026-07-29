# Operadores relacinais
# >, <, >=, <=, ==, !=
# > maior que
# < menor que
# >= maior ou igual a
# <= menor ou igual a
# == igual a
# != diferente de

input_idade = int(input('Qual sua idade? '))
if input_idade < 18:
    print('Você é menor de idade')
elif input_idade >= 18 and input_idade < 65:
    print('Você é adulto')
elif input_idade >= 65:
    print('Você é idoso')

#Exercicio operadores relacionais
# Crei um programa que verifique se um valor é 
# maior, menor ou igual ao outro

valor_1 = int(input('Digite o primeiro valor: '))
valor_2 = int(input('Digite o segundo valor: '))
if valor_1 > valor_2:
    print(f'O valor {valor_1} é maior que {valor_2}')
elif valor_1 < valor_2:
    print(f'O valor {valor_1} é menor que {valor_2}')
else:
    print(f'O valor {valor_1} é igual a {valor_2}')
    
