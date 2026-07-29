'''
# Docstring
Python = Linguagem de programação
Tipo de tipagem = Dinâmica / Forte
'''
'''Comentario'''
# comentario cima
print('\nComentario\n') # comentarios frente
#comentario baixo    

# "\n" -> quebra de linha
print('Hello World!\n')

# Tipos de dados (Data types)

# str -> string -> texto
# Strings são textos que estão dentro de aspas "texto"

print('int -> Número inteiro', 11, -11,"\n")
# Tipos int e float
# int -> Número inteiro
# O tipo int representa qualquer número
# positivo ou negativo. int sem sinal é considerado
# positivo.

print("float -> Número com ponto flutuante",1.1, 10.11, -1.5,"\n")
# O tipo float representa qualquer número
# positivo ou negativo com ponto flutuante.
# float sem sinal é considerado positivo.

# Tipo de dado bool (boolean)
# Ao questionar algo em um programa,
# só existem duas respostas possíveis:
# sim (True) ou não (False).
# Existem vários operadores para "questionar".
# Dentre eles o ==, que é um operador lógico que
# questiona se um valor é igual a outro
print('bool -> booleano (lógico)',True, False)
print(10 == 10)  # Sim => True (Verdadeiro)
print(10 == 11)  # Não => False (Falso)
print(type(True))
print(type(False))
print(type(10 == 10))
print(type(10 == 11),"\n")

# Type()
# Podemos descobrir o tipo de dado de uma variável  ou valor com a função type()
print(type('texto'))   # str
print(type(11))        # int
print(type(1.1))      # float
print(type(10 == 11)) # bool
print(type(True))     # bool
print(type(False),"\n")    # bool

# Conversão de tipos (type casting)
# Podemos converter um tipo de dado em outro        
print("Conversão de tipos (type casting)")
print(type(int("11")))      # str -> int
print(type(float("1.1")))   # str -> float
print(type(int(1.1)))       # float -> int
print(type(float(11)))      # int -> float
print(type(str(11)))        # int -> str
print(type(str(1.1)))      # float -> str
print(type(bool(1)))       # int -> bool
print(type(bool(-11)))     # int -> bool
print(type(bool("")))      # str -> bool
print(type(bool("texto"))) # str -> bool
print(type(bool(" ")))     # str -> bool
print(type(bool("0")))     # str -> bool
print(type(bool("False"))) # str -> bool
print(type(bool("True")))  # str -> bool
print(str(11) + "b") # int -> str
print(int("11") + 1) # str -> int
print(float("1.1") + 1.0) # str -> float
print(int(1.9) + 1) # float -> int
print(float(11) + 1.1) # int -> float
print(str(1.1) + "b\n") # float -> str

# Regras de conversão
# str -> int : Somente se o texto for um número inteiro
# str -> float : Somente se o texto for um número com ponto flutuante
# float -> int : O número é arredondado para baixo (floor)  
# int -> float : Sem problemas, o número vira um float com .0
# int -> str : Sem problemas, o número vira um texto
# float -> str : Sem problemas, o número vira um texto
# int -> bool : 0 é False, qualquer outro número é True
# float -> bool : 0.0 é False, qualquer outro número é True
# str -> bool : String vazia "" é False, qualquer outro texto é True