# try e except são usados para tratar exceções em Python.
# Quando um erro ocorre dentro do bloco try, a execução é desviada para o bloco except
# onde podemos lidar com o erro de forma controlada, evitando que o programa termine abruptamente.
try:
    # Código que pode gerar uma exceção
    numero = int(input('Digite um número inteiro: '))
    resultado = 10 / numero
    print(f'O resultado da divisão é: {resultado}')
except ValueError:
    # Tratamento para erro de valor inválido
    print('Erro: Você deve digitar um número inteiro válido.')
except ZeroDivisionError:
    # Tratamento para divisão por zero
    print('Erro: Divisão por zero não é permitida.')
except Exception as e:
    # Tratamento genérico para outras exceções
    print(f'Ocorreu um erro inesperado: {e}')
finally:
    # Bloco opcional que sempre será executado
    print('Execução do bloco try-except finalizada.')
# O bloco finally é opcional e será executado independentemente de uma exceção ter ocorrido ou não.
