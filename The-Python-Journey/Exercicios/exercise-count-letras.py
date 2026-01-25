frase = 'O Python é uma linguagem de programação incrível'

# contar quais letras aparecem mais vezes na frase
i = 0
letra = ''
maior = 0   
while i < len(frase):
    letra_atual = frase[i]
    quantidade = frase.count(letra_atual)
    if letra_atual == ' ': # ignorar espaços
        i += 1
        continue 
    if quantidade > maior:
        maior = quantidade
        letra = letra_atual
    i += 1
print(f'A letra que apareceu mais vezes foi o {letra} que apareceu {maior} vezes.')








