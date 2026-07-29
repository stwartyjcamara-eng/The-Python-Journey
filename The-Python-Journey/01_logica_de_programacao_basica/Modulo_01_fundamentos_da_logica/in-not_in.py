# Operadores 'in' e 'not in' 
# Strings são iteráveis
# .0. 1. 2. 3. 4. 5. 6
# .S..T..W..A..R..T..Y
# -7 -6 -5 -4 -3 -2 -1 

nome = "STWARTY"
print(nome[2])  # W
print(nome[-5]) # W
print('S' in nome)      # True
print('s' in nome)      # False
print('A' in nome)      # True
print(10 * '-')

texto = "Python"
print('Python' in texto)       # True
print('java' in texto)         # False


nome = input('Digite seu nome: ')
encontrar_in_nome = input('Qual letra deseja encontrar no seu nome? ')
if encontrar_in_nome in nome:
    print(f'A letra "{encontrar_in_nome}" foi encontrada no seu nome "{nome}"')
else:
    print(f'A letra "{encontrar_in_nome}" não foi encontrada no seu nome "{nome}"')
