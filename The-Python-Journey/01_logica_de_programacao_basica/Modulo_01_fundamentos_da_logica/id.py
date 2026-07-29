f = 's'
g = 's'
print(id(f))  # Imprime o ID do objeto referenciado por f
print(id(g))  # Imprime o ID do objeto referenciado por g mesmo valor de f e g 
# Ambos apontam para o mesmo objeto na memória
h = 's1'
print(id(h))  # Imprime o ID do objeto referenciado por h diferente valor de f e g
# h aponta para um objeto diferente na memória
