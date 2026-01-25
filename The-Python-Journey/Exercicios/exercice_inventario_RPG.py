'''
Exercício: O Gerenciador de Inventário de RPG
Imagine que você está desenvolvendo um jogo e precisa gerenciar a mochila do personagem. O objetivo é 
criar um script que permita adicionar itens, remover itens e visualizar o que o herói está carregando.

O Desafio
Escreva um programa que execute as seguintes tarefas:

Criação: Comece com uma lista chamada mochila contendo 3 itens iniciais (ex: "Espada", "Poção", "Escudo").

Adição: Peça para o usuário digitar um novo item encontrado e adicione-o ao final da lista.

Remoção: O herói usou a "Poção". Remova esse item específico da lista.

Acesso e Verificação:

Exiba quantos itens existem na mochila no total.

Verifique se o item "Mapa" está na lista. Se não estiver, imprima uma mensagem dizendo: "O herói está perdido!".

Ordenação: Organize a mochila em ordem alfabética e exiba a lista final.
'''
mochila = ["Espada", "Poção", "Escudo"] #criação Mochila
print(f'Itens da Mochila: {len(mochila)}: {mochila}')

print('Você encontrou um Baú contendo [MAPA]') 
while True: 
    novo_iten = input('deseja adicionar a mochila ? [S/N]: ').lower().strip() # Adição do novo iten [MAPA]
    if novo_iten in ['s', 'sim']:
        novo_iten = 'Mapa'
        mochila.append(novo_iten)
        break
    if novo_iten in ['n', 'não']: 
        break
    print("Resposta inválida! Por favor, digite apenas S ou N.")

print(f'Itens da Mochila: {len(mochila)}: {mochila}')
print('HP abaixo de 20%')
while True:
    opcao = input("Deseja usar a poção? [S/N]: ").lower().strip()
    # Se a resposta estiver na lista de aceitas, saímos do loop
    if opcao in ['s', 'sim', 'n', 'não']:
        break
    # Se o código chegar aqui, é porque a resposta NÃO era s, sim, n ou não
    print("Resposta inválida! Por favor, digite apenas S ou N.")

if opcao in ['s', 'sim']:
    mochila.remove("Poção")
    print("Você usou a poção!")

print(f'Itens da Mochila: {len(mochila)}: {mochila}')
# Verifique se o item "Mapa" está na lista. Se não estiver, imprima uma mensagem dizendo: "O herói está perdido!".
print('Verificação do local em andamento ...')
if not 'Mapa' in mochila:
    print('Mapa não localizado o herói está perdido!')
else:
    print('O herói se localizou!')
# Ordenação: Organize a mochila em ordem alfabética e exiba a lista final.
mochila.sort() #Não estudei o [.sort] por isso tive que pesquisar na hora !
print((f'Itens da Mochila: {len(mochila)}: {mochila}'))