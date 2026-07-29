# input -> Entrada de dados
'''
nome = input('Informe o seu nome: ')
print(f'Seu nome é {nome}')
idade = input('Informe a sua idade: ')
print(f'Sua idade é {idade}') # idade é str
ano_nascimento = 2025 - int(idade) # type casting
print(f'Seu ano de nascimento é {ano_nascimento}')
'''

# Exercício
# Some a idade de duas pessoas

idade1 = int(input('Informe a idade da primeira pessoa: '))
idade2 = int(input('Informe a idade da segunda pessoa: '))
soma_idade = idade1 + idade2 
# Uma segunda forma de fazer a soma das idades
# idade1 = input('Informe a idade da primeira pessoa: ')
# idade2 = input('Informe a idade da segunda pessoa: ')
# soma_idade = int(idade1) + int(idade2)
print(f'A soma da idade das duas pessoas é {soma_idade}')
