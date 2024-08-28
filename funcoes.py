# EXISTEM ALGUMAS FORMAS DE SE CRIAR E CHAMAR UMA FUNÇÃO EM PYTHON:

# Exemplo 1

def exibir_mensagem():
    print('Olá mundo!')
    
exibir_mensagem()

# Exemplo 2 =====================================================================================================================

def exibir_mensagem2(nome): # não declaramos a variável na função
    print(f'Seja bem vindo {nome}.')

exibir_mensagem2(nome = 'João Pedro') # mas na hora de chamarmos a função, obrigatoriamente a variável nome deve ser definida


# Exemplo 3 ======================================================================================================================

def exibir_mensagem3(nome = 'João Pedro'): # definimos o valor da variável dentro da própria função
    print(f'Seja bem vindo {nome}.')
    
exibir_mensagem3() # como já definimos o valor da variável acima, não precisamos repetir na hora de chamar a função

# Exemplo 4 ======================================================================================================================

def exibir_mensagem3(nome = 'João Pedro'): # definimos o valor da variável dentro da própria função
    print(f'Seja bem vindo {nome}.')
    
exibir_mensagem3(nome = 'Pedro') # Porém, é possível mudar o valor da variável nome na hora de chamarmos a função, mas não seria o ideal, apenas se necessário.

#=================================================================================================================================

# O USO DO RETURN NAS FUNÇÕES

def calcular_soma(numeros):
    return sum(numeros) # Basicamente o return funciona como o print(), porém, sem mostrar nada no terminal, o return apenas armazena o resultado da função dentro dele

resultado = calcular_soma([10, 10, 10, 10, 5]) # Aqui, colocamos os valores a serem somados na nossa função, em forma de lista
print(resultado) # Printamos o resultado que já estava armazenado no return.

#==================================================================================================================================

# OUTROS EXEMPLOS DE OPERAÇÕES COM FUNÇÃO

def somar(a , b):
    return a + b

print(somar(10, 10))


def subtrair(a , b):
    return a - b

print(subtrair(100, 5))