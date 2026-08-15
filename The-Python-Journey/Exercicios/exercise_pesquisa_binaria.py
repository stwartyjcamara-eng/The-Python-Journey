# Projeto pessoal de implementação do algoritmo de pesquisa binaria.


while True:
    inicio = 1
    lista = list(range(inicio, 101))
    final = len(lista)
    numero_escolhido = input("Escolha um número de 1 a 100: ")
    while True:  # Laco de repetição para verificar se o número é inteiro válido
        if numero_escolhido.isdigit():
            numero_escolhido = int(numero_escolhido)
            break
        else:
            numero_escolhido = input(
                "Por favor, digite um número inteiro válido, número de 1 a 100: "
            )

    chute = int((inicio + final) / 2)  # Encontra o meio do intervalo atual
    print(f"Meu chute é: {chute}")

    maior_menor_certo = input(
        "Meu chute foi [Maior], [Menor] ou [Certo] que o número escolhido? "
    ).lower()

    while True:  # Laco de repetição para opções de [Maior], [Menor] ou [Certo]
        if maior_menor_certo == "maior":
            final = chute
            lista = list(range(inicio, final))  # Atualiza a lista
            chute = int((inicio + final) / 2)
            print(f"Meu novo chute é: {chute}")
            maior_menor_certo = input(
                "Meu chute foi [Maior], [Menor] ou [Certo] que o número escolhido? "
            ).lower()
            continue
        if maior_menor_certo == "menor":
            inicio = chute
            lista = list(range(inicio + 1, final + 1))  # Atualiza a lista
            chute = int((inicio + final) / 2)
            print(f"Meu novo chute é: {chute}")
            maior_menor_certo = input(
                "Meu chute foi [Maior], [Menor] ou [Certo] que o número escolhido? "
            ).lower()
            continue
        if maior_menor_certo == "certo":
            print("Acertei")
            break
        if not maior_menor_certo.isdigit():  # Se for um int pede para digitar uma str
            print("Por favor informe somente: [Maior], [Menor] ou [Certo]!")
            maior_menor_certo = input(
                "Meu chute foi [Maior], [Menor] ou [Certo] que o número escolhido? "
            ).lower()

        else:
            print(
                "Por favor informe somente: [Maior], [Menor] ou [Certo]!"
            )  # Se for uma str diferente de [Maior], [Menor] ou [Certo]
            maior_menor_certo = input(
                "Meu chute foi [Maior], [Menor] ou [Certo] que o número escolhido? "
            ).lower()
    break  # Encerra o Programa
