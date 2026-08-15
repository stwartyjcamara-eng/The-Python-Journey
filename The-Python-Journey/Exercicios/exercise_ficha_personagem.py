"""
Exercício: Ficha de Personagem (Dicionários)Imagine que agora você precisa armazenar não apenas a pontuação,
mas os detalhes do herói que alcançou esses pontos.
O DesafioEscreva um programa que execute os seguintes passos:
Criação: Crie um dicionário chamado personagem com as seguintes chaves e valores iniciais:
"nome": "Aragorn"
"classe": "Guerreiro"
"nivel": 10
Exibição Simples: Imprima o nome e o nível do personagem acessando as chaves do dicionário.
Atualização: O personagem ganhou experiência!
Atualize o valor da chave "nivel" para 11.
Adição de Dados: Adicione uma nova chave chamada "habilidade" com o valor "Corte Preciso".
Verificação: Use um if para verificar se a chave "arma" existe no dicionário.
Se não existir, adicione-a com o valor "Espada de Aço".
Impressão Final:
Mostre o dicionário completo no final.
Guia de Referência RápidaAçãoComandoExplicaçãoCriardic = {"chave": "valor"}Usa chaves { } e dois pontos :
Acessarprint(dic["chave"])Usa o nome da chave entre colchetesAdicionar/Mudardic["chave"] = novo_valor
Se a chave existe, muda; se não, criaVerificarif "chave" in dic:Verifica se a chave existe no dicionário
Exemplo de início:
Pythonpersonagem = {
    "nome": "Aragorn",
    "classe": "Guerreiro",
    "nivel": 10
}

# Para acessar o nome:
print(f"Herói: {personagem['nome']}")
Dica de Ouro: Ao usar F-strings com dicionários, se você usou aspas duplas por fora f"...", use aspas simples por dentro personagem['nome'] para não "quebrar" o código.
"""

personagem = {"nome": "Aragorn", "classe": "Guerreiro", "nivel": 10}
# Para acessar o nome:
print(f"Herói: {personagem['nome']}, nivel: {personagem['nivel']}")
print("Atualização: O personagem ganhou experiência! ")
personagem["nivel"] = 11
print(f"Herói: {personagem['nome']}, nivel: {personagem['nivel']}")

# Ainda não estudei dicionarios ... por isso vou estudar e voltar para completar o exercicio !
