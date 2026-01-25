""" Calculadora com while """
while True:
    num1 = input('Digite o primeiro número: ')
    num2 = input('Digite o segundo número: ')
    operador = input('Digite o operador (+-*/): ')

    if not num1.isnumeric() or not num2.isnumeric():
        print('Você precisa digitar números válidos.')
        continue

    num1 = float(num1)
    num2 = float(num2)

    if operador == '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    elif operador == '-':
        print(f'{num1} - {num2} = {num1 - num2}')
    elif operador == '*':
        print(f'{num1} * {num2} = {num1 * num2}')
    elif operador == '/':
        if num2 == 0:
            print('Não é possível dividir por zero.')
            continue
        print(f'{num1} / {num2} = {num1 / num2}')
    else:
        print('Operador inválido.')
        continue

    sair = input('Deseja sair? (s/n): ')
    if sair.lower() == 's':
        break