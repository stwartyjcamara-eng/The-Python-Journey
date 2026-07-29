# Fatiamento de Strings (String Slicing)
# [inicio:fim:passo]    
# Se omitir o inicio, começa do indice 0
# Se omitir o fim, vai até o final da string
# Se omitir o passo, o padrão é 1
# Passo -1, inverte a string
# Strings são imutáveis
# Exemplos
nome = 'Stwarty'
print(nome[0:1]) # 0,1,2
print(nome[3:6]) # 3,4,5
print(nome[0:6:2]) # 0,2,4
print(nome[:6]) # 0,1,2,3,4,5
print(nome[0:]) # 0,1,2,3,4,5,6
print(nome[::2]) # 0,2,4,6
print(nome[::-1]) # Inverte a string
print(nome[::-2]) # Inverte a string, pulando de 2 em 2
print(nome[5:0:-1]) # 5,4,3,2,1
print(nome[5::-1]) # 5,4,3,2,1,
print(nome[-1]) # Ultimo caractere
print(nome[-6:-1]) # -6,-5,-4,-3,-2
print(nome[-1:-6:-1]) # -1,-2,-3,-4,-5
print(nome[-1:-7:-1]) # -1,-2,-3,-4,-
print(nome[-7::-1]) # -7,-6,-5,-4,-3,-2,-1
print(nome[-7:]) # -7,-6,-5,-4,-3,-2,-1
print(nome[:-1]) # -7,-6,-5,-4,-3,-2
print(nome[:-3]) # -7,-6,-5,-4
print(nome[-3:]) # -3,-2,-1
print(nome[:]) # -7,-6,-5,-4,-3,-2,-1
print(nome[::]) # -7,-6,-5,-4,-3,-2,-
print(nome[::-1]) # -1,-2,-3,-4,-5,-6,-7
print(nome[::-2]) # -1,-3,-5,-7
print(nome[1::2]) # 1,3,5
print(nome[1:6:2]) # 1,3,5  
print(nome[1:6:3]) # 1,4
# nome[0] = 'S' # Erro, strings são imutáveis
# nome[7] = 'y' # Erro, strings são imutáveis
nova_string = nome[0:6] + 'y' # Concatenação
print(nova_string)
print(nome) # Original permanece inalterada
print(nome[0:6] + 'y') # Concatenação
print(nome) # Original permanece inalterada
print(nome[:]) # Cópia da string    
print(nome[:]) # Cópia da string
print(nome[::]) # Cópia da string
# Função len() - Retorna o tamanho da string
# 0123456
# Stwarty
#-7654321
print(len(nome)) # 7
print(len(nova_string)) # 7
print(nome[0:len(nome):3]) # 0,3,6
print(nome[0:len(nome):-2]) # Vazio, pois o passo é negativo
print(nome[len(nome)-1::-1]) # Inverte a string
