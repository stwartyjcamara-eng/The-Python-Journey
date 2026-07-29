# interpolação basica de strings

nome = 'Stwarty'
idade = 31
altura = 1.7581561 # numero grande de casas decimais
print('Meu nome é %s, tenho %d anos e' 
      'minha altura é %.2f' % (nome, idade, altura)
      )
# %.2f -> 2 casas decimais
# hexadecimal %x ou %X
print('o valor hexadecimal de %d é %04x' % (1500, 1500))
print('o valor hexadecimal de %d é %04X' % (1500, 1500))