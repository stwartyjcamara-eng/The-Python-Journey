'''
Enumerate
'''
lista = ['Ana', 'Bruno', 'Carla']
lista.append('Daniel')
print(lista,'\n')

lista_enumerate = enumerate(lista)

for item in lista_enumerate:
    print(item)
print('pula')
for item in enumerate(lista):
    print(item)
print('\n')
for indice, nome in enumerate(lista): # for dentro de for desempacotando a tupla
    print(f'\tÍndice: {indice} Nome: {nome}') #\t tab space