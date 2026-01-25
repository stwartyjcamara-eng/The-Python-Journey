"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero_int = input('Digite um número inteiro: ')
if numero_int.isdigit():
    numero_int = int(numero_int)
    if numero_int % 2 == 0:
        print(f'O número {numero_int} é par.')
    else:
        print(f'O número {numero_int} é ímpar.')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = input('Que horas são? (0-23): ')
if hora.isdigit():
    try:
        hora = int(hora)
        if 0 <= hora <= 11:
            print('Bom dia!')
        elif 12 <= hora <= 17:
            print('Boa tarde!')
        elif 18 <= hora <= 23:
            print('Boa noite!')
        else:
            print('Hora inválida! Por favor, digite um valor entre 0 e 23.')
    except ValueError:
        print('Por favor, digite um número inteiro válido para a hora.')
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('Digite seu primeiro nome: ')
tamanho_nome = len(nome)
if tamanho_nome <= 4:
    print('Seu nome é curto')
elif 5 <= tamanho_nome <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')