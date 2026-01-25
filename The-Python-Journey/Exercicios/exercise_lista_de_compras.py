# Faça uma lista de compras que permita ao usuário adicionar, remover e listar valores da sua lista
lista_de_compras = []
while True:
    print("\nLista de Compras:")
    print("\nOpções:")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Listar itens")
    print("4. Sair")
    escolha = input("Escolha uma opção (1/2/3/4): ")
    
    if escolha == '1':
        item = input("Digite o item para adicionar: ")
        lista_de_compras.append(item)
        print(f"{item} adicionado à lista.")
    elif escolha == '2':
        indice = int(input("Digite o índice do item para remover: "))
        if 0 <= indice < len(lista_de_compras):
            item_removido = lista_de_compras.pop(indice)
            print(f"{item_removido} removido da lista.")
        else:
            print("Índice inválido.")
    elif escolha == '3':
        print("Itens na lista de compras:")
        for indice, item in enumerate(lista_de_compras):
            print(f"{indice}: {item}")
    elif escolha == '4':
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")
print("Lista final de compras:", lista_de_compras)