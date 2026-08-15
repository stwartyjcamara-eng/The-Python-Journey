"""
Exercício: O Sistema de Pontuação do Torneio
Você está organizando um torneio de e-sports. Você tem uma lista com as pontuações de 5 rodadas de um jogador.
Seu objetivo é processar esses dados.

O Desafio
Escreva um programa que execute as seguintes tarefas:

A Lista: Crie uma lista chamada pontuacoes com estes valores: [120, 250, 80, 420, 190].

O Bônus (Loop for): O organizador decidiu dar um bônus de 10 pontos para cada rodada.
Use um loop for para criar uma nova lista chamada pontuacoes_atualizadas onde cada valor
seja a pontuação original + 10.

Filtragem (IF dentro do FOR): Durante o torneio, apenas rodadas acima de 200 pontos são consideradas "Nível Profissional".
Use um loop para contar quantas rodadas atingiram esse nível.

Cálculo Total: Use a função sum() do Python para mostrar a pontuação total acumulada pelo jogador.

O Ranking: Mostre a maior pontuação (max()) e a menor pontuação (min()).
"""

pontuacoes = [120, 250, 80, 420, 190]
print(f"Pontuação original: {pontuacoes}")
pontuacoes_atualizadas = []  # lista vazia para começar
contador = 0
for p in pontuacoes:
    novo_valor = p + 10
    pontuacoes_atualizadas.append(novo_valor)
    if novo_valor >= 200:
        contador += 1
total = sum(pontuacoes_atualizadas)
maior = max(pontuacoes_atualizadas)
menor = min(pontuacoes_atualizadas)
print(
    f"Nova pontuação: {pontuacoes_atualizadas}\n"
    f"Pontuação total: {total}\n"
    f"O Ranking, Maior pontuação: {maior} e Menor pontuação: {menor}\n"
    f"Rodadas nível Profissional: {contador}\n"
)
