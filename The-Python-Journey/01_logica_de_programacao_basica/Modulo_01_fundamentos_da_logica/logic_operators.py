#Operadores logicos
# and -> e | todas as condições devem ser verdadeiras
# or -> ou | uma ou mais condições devem ser verdadeiras
# not -> não | inverte o valor booleano

entrada = input('Você quer "[E]ntrar" ou "[S]air"? ')
senha_digitada = input('Digite sua senha: ')

senha_permitida = '123456'
if entrada == 'E' or entrada == 'e' and senha_digitada == senha_permitida: #adicionei o comando or para aceitar maiusculo e minusculo
    print('Você entrou no sistema!')
elif entrada == 'E' or entrada == 'e' and senha_digitada != senha_permitida:
    print('Senha incorreta! Você não pode entrar no sistema!')
elif entrada == 'S' or entrada == 's' and senha_digitada == senha_permitida:
    print('Você saiu do sistema!')
elif entrada == 'S' or entrada == 's' and senha_digitada != senha_permitida:
    print('Senha incorreta! Você não pode sair do sistema!')
else:
    print('Comando inválido!')

# Operador not inverte o valor booleano
# not True -> False
# not False -> True