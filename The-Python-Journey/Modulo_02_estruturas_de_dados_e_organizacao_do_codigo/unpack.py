'''
Empacotamento e desempacotamento de listas e tuplas
'''
nome1, *resto_nomes = ["Ana", "Bruno", "Carla", "Daniel"]
print(nome1, resto_nomes)
# Saída: Ana ['Bruno', 'Carla', 'Daniel']
nome2, nome3, *resto_nomes = ("Ana", "Bruno", "Carla", "Daniel", "Eduardo")