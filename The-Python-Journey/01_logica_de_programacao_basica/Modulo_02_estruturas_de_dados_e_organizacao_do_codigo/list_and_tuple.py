'''
Empacotamento e desempacotamento de listas e tuplas
'''
# Empacotamento [Listas]
nomes = ["Ana", "Bruno", "Carla"]
print(nomes,'\n')
# Saída: ['Ana', 'Bruno', 'Carla']
nome1, *resto_nomes = ["Ana", "Bruno", "Carla", "Daniel"]
print(nome1, resto_nomes,'\n') # o * antes do resto_nomes indica que é uma lista
# Saída: Ana ['Bruno', 'Carla', 'Daniel']
nome2, nome3, *resto_nomes = ("Ana", "Bruno", "Carla", "Daniel", "Eduardo")
print(f'{nome2}, {nome3}, {resto_nomes}\n') #fstring
# Saída: Ana Bruno ['Carla', 'Daniel', 'Eduardo']
nome1, nome2, *_ = ["Ana", "Bruno", "Carla", "Daniel", "Eduardo"]
print(nome1, nome2, *_,'\n') # o _ sgnifica que o valor não será usado
# Saída: Ana Bruno Carla Daniel Eduardo
'''
tuplas = listas imutáveis
'''
nome = 'Ana', 'Bruno', 'Carla' # tupla sem parênteses
#nome[1] = 'Daniel'  # Isso causará um erro, pois tuplas são imutáveis
print(nome[0],'\n')  # Acesso por índice
print(nome)