# Whyle 
contador = 1
while contador <= 10:
    print(f'Contador: {contador}')
    contador += 1
print('Fim do loop')
print('---')
# While com break
contador = 1
while True:
    print(f'Contador: {contador}')
    contador += 1
    if contador > 10:
        break
print('Fim do loop')
print('---')
# While com continue
contador = 0
while contador < 10:
    contador += 1
    if contador % 2 == 0:
        continue
    print(f'Contador: {contador}')
print('Fim do loop')
print('---')
# While com else
contador = 1
while contador <= 10:
    print(f'Contador: {contador}')
    contador += 1
else:
    print('Fim do loop')
print('---')
# While com input
while True:
    entrada = input('Digite "sair" para encerrar o programa: ')
    if entrada.lower() == 'sair':
        print('Encerrando o programa...')
        break
    else:
        print(f'Você digitou: {entrada}')
print('---')
# While para validar entrada do usuário
while True:
    idade = input('Digite sua idade: ')
    if idade.isdigit():
        idade = int(idade)
        print(f'Sua idade é {idade} anos.')
        break
    else:
        print('Por favor, digite um número inteiro válido para a idade.')
print('---')
# While com while aninhados
linha = 1
while linha <= 3:
    coluna = 1
    while coluna <= 3:
        print(f'Linha {linha}, Coluna {coluna}')
        coluna += 1
    linha += 1
print('Fim dos loops aninhados')
print('---')