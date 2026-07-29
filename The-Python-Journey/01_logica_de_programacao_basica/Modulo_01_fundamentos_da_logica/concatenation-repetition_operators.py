# Operadores Aritméticos
# +, -, *, /, //, **, % 
# Ordem de precedência: (), **, *, /, //, %, +, -, -
print('Operadores Aritméticos\n')
adicao = 10 + 10 
print('Adição', adicao) 
subtracao = 10 - 5
print('Subtração', subtracao)
multiplicacao = 10 * 10
print('Multiplicação', multiplicacao)
divisao = 10 / 3  # float
print('Divisão', divisao)
divisao_inteira = 10 // 3
print('Divisão inteira', divisao_inteira)
exponenciacao = 2 ** 10
print('Exponenciação', exponenciacao)
modulo = 55 % 2  # resto da divisão
print('Módulo', modulo)
print(10 % 8 == 0)
print(10 % 2 == 0)
print(11 % 2 == 0)
print(10 + 10 * 2)  # Ordem de precedência
print((10 + 10) * 2)  # Ordem de precedência
print('\n')

# Operadores de atribuição
print('Operadores de Atribuição\n')
x = 10  # atribuição    
print('x =', x)
x += 2  # x = x + 2
print('x += 2 ->', x)
x -= 2  # x = x - 2
print('x -= 2 ->', x)
x *= 2  # x = x * 2
print('x *= 2 ->', x)
x /= 2  # x = x / 2
print('x /= 2 ->', x)
x //= 2  # x = x // 2
print('x //= 2 ->', x)
x **= 2  # x = x ** 2
print('x **= 2 ->', x)
x %= 2  # x = x % 2
print('x %= 2 ->', x)
print('\n')

# Concatenação de strings
print('Concatenação de strings\n')  
nome = 'Stwarty'
sobrenome = "Camara" 
nome_completo = nome + ' ' + sobrenome # concatenação
print('Nome completo:', nome_completo) # menos comum
print('Nome completo:', nome + ' ' + sobrenome) # mais comum
print('Nome completo:', nome, sobrenome) # mais simples
print('\n') 

# Repetição de strings
print('Repetição de strings\n')
print('Stwarty' * 5) # cuidado com o espaço
print('Stwarty ' * 5) # cuidado com o espaço
print(5 * 'Stwarty ') 
print(int("5") * ' Stwarty') #type casting + repetição
print('\n')

#Exercício IMC
print('Exercício IMC\n')
nome = 'Stwarty'
sobrenome = 'Camara'
altura = 1.75 
peso = 80 
imc = peso / altura ** 2 
'''
print -> Stwarty tem 1.75 de altura, pesa 80 kg e seu IMC é 26.12
'''
print(nome, sobrenome, 'tem', altura, 'de altura, pesa', peso, 'kg e seu IMC é', imc)
print("\n")
print(f'{nome} {sobrenome} tem {altura} de altura, pesa {peso} kg e seu IMC é {imc:.2f}') # f-string


