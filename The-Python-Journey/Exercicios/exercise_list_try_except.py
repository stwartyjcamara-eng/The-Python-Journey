import os

lista = []

while True:
    print("Selecione uma opção:")
    opção = input("[i]nserir, [r]emover, [l]istar, [s]air: ").lower()
    if opção == "i":
        os.system("cls")
        valor = input("Valor: ")
        lista.append(valor)
    elif opção == "r":
        os.system("cls")
        try:
            indice = int(input("Índice para remover: "))
            lista.pop(indice)
        except IndexError:
            print("Índice inválido.")
        except ValueError:
            print("Por favor, insira um número inteiro válido para o índice.")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
    elif opção == "l":
        os.system("cls")
        for i, v in enumerate(lista):
            print(i, v)
    elif opção == "s":
        break
os.system("cls")
print("Lista final:", lista)
