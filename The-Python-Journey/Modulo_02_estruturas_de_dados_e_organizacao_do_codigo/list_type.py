# Listas em Phyton
idades = [25, 30, 35, 40]
print(idades)
print(type(idades))
print(len(idades))  # Tamanho da lista
print(idades[0])    # Acessando o primeiro elemento
print(idades[-1])   # Acessando o último elemento
idades[0] = 26     # Modificando o primeiro elemento
print(idades)
# Metodos uteis de listas: append, insert, remove, pop, clear, index, count, sort, reverse
idades.append(45)  # Adiciona um elemento no final da lista
print(idades)
idades.insert(1, 28)  # Adiciona um elemento na posição especificada
print(idades)
idades.remove(35)  # Remove o primeiro elemento com o valor especificado
print(idades)
idade_removida = idades.pop()  # Remove e retorna o último elemento
print(idades)
print(f'Idade removida: {idade_removida}')
idades.clear()  # Remove todos os elementos da lista
print(idades)
idades = [25, 30, 35, 40]
print(idades.index(30))  # Retorna o índice do primeiro elemento com o valor especificado
print(idades.count(30))  # Conta quantas vezes o valor especificado aparece na lista
idades.sort()  # Ordena a lista em ordem crescente
print(idades)
idades.reverse()  # Inverte a ordem dos elementos na lista
print(idades)
# Suporta vários tipos de dados
# indices:     0      1        2       3        4
lista_mista = [25, 'Python', 3.14, True, [0, 1, 2]]
print(lista_mista)
print(type(lista_mista))