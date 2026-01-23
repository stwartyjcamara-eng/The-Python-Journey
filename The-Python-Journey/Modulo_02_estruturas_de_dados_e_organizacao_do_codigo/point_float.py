#importando a biblioteca decimal para maior precisão em operações de ponto flutuante !!!!

# Exemplo de problema com ponto flutuante
numero1 = 0.1
numero2 = 0.7
soma = numero1 + numero2
print(f'Soma: {soma}')  # Saída esperada: 0.8
# Saída real pode ser: 0.7999999999999999 devido à representação interna de números de ponto flutuante
# Solução usando round para limitar a precisão
print(f'Soma: {soma:.2f}')  # Saída formatada: 0.802f}')
soma_arredondada = round(soma, 2)
print(f'Soma arredondada: {soma_arredondada}')  # Saída: 0.8
