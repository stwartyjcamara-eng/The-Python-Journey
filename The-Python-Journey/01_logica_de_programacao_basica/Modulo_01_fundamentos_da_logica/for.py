# Iterando sobre uma string com for

texto = 'Python'
novo_texto = ''
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto + '*')

# range(start, stop, step)
for numero in range(1, 10, 2): # 1, 3, 5, 7, 9
    print(numero)

for numero in range(10, 1, -1): # 10, 9, 8, ..., 2
    print(numero)
for numero in range(10): # 0, 1, 2, ..., 9
    print(numero)

for i in range(10):
    if i == 2:
        print('Encontrado o número 2!')
        continue
    # if i == 8:
    #     print('Número 8 encontrado, saindo...')
    #     break
    for j in range(1, 3):
        print(f'[{i}, {j}]')
else:
    print('Cheguei ao else do for')
print('Fim do programa.')