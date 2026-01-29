"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
while True:
    cpf = input('Informe o CPF: ').lower().replace(".","").replace("-","").strip()
    print(cpf)
    if cpf.isdigit():
        break
    else:
        cpf = input('Por favor, digite números válido, Informe o CPF: ').lower().replace(".","").replace("-","").strip()

nove_digitos = cpf[:9]
contador_regressivo = 10

soma = 0
for digito in nove_digitos:
    soma +=  int(digito) * contador_regressivo
    contador_regressivo -= 1
digito1 = ((soma * 10) % 11) 
digito1 = digito1 if digito1 <= 9 else 0
print(digito1)

dez_digitos = nove_digitos + str(digito1)
contador_regressivo = 11

soma = 0
for digito2 in dez_digitos:
    soma +=  int(digito2) * contador_regressivo
    contador_regressivo -= 1
digito2 = ((soma * 10) % 11) 
digito2 = digito2 if digito2 <= 9 else 0
print(digito2)
print(nove_digitos + str(digito1) + str(digito2))



