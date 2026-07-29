entrada = input('Você quer "entrar" ou "sair"? ')

if entrada == 'entrar':
    print('Você entrou no sistema!')
elif entrada == 'sair':
    print('Você saiu do sistema!')
else:
    print('Comando inválido!')  
# Exemplo com if, elif e else
# O Python lê o código de cima para baixo.
# Se uma condição for verdadeira, o Python
# executa o bloco de código daquela condição
# e ignora o restante.
# Se nenhuma condição for verdadeira, o Python
# executa o bloco do else.