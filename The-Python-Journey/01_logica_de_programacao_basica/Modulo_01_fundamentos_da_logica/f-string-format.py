# f-string
nome = 'Stwarty'
print(f'Meu nome é {nome}') 
idade = 33
altura = 1.75
print(f'Meu nome é {nome} ,tenho {idade} anos e '\
'minha altura é {altura}') 
# formatação de strings com metodo format
print('Meu nome é {0} ,tenho {1} anos e ' \
'minha altura é {2:.3f}'.format(nome, idade, altura))
# {:.3f} -> 3 casas decimais
print('Meu nome é {1} ,tenho {0} anos e ' \
'minha altura é {2:.2f}'.format(nome, idade, altura))
# utilizando indices na ordem que quiser, 
# atenção com os indices repetidos ou tipo de dado
print('Meu nome é {n} ,tenho {i} anos e ' \
'minha altura é {a:.1f}'.format(n=nome, i=idade, a=altura))
# utilizando parametros nomeados
print('Meu nome é {n} ,tenho {i} anos e ' \
'minha altura é {a:.0f}'.format(n=nome, i=idade, a=altura))
# {:.0f} -> 0 casas decimais

# Formatação básica de strings
# s - string
# d - int
# f - float
# .<número de dígitos>f
# x ou X - Hexadecimal
# (Caractere)(><^)(quantidade)
# > - Esquerda
# < - Direita
# ^ - Centro
print (f'{nome:>10}.') # Alinha a direita
print (f'{nome:<10}.') # Alinha a esquerda
print (f'{nome:^10}.') # Alinha ao centro
print (f'{nome:.^20}.') # Preenche com pontos
print (f'{idade:0<10}.') # Preenche com zeros
print (f'{altura:0>10.2f}.') # Preenche com zeros e 2 casas decimais
print (f'{1000.48765:0<20,.2f}.') # Preenche com zeros, 2 casas decimais e separador de milhar
# = - Força o número a aparecer antes dos zeros
print (f'{1000.48765:=^20,.2f}.') # Força o número a aparecer antes dos zeros, 2 casas decimais e separador de milhar
# + - Sempre mostra o sinal
# Sinal - + ou -
# Ex.: 0>-100,.1f
print (f'{1000.48765:+>100,.1f}.') # Sempre mostra o sinal, 2 casas decimais e separador de milhar
# Conversion flags - !r !s !a 


