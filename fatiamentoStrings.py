# ELIMINANDO ESPAÇOS EM BRANCO

curso = '       Python   ' # note que existem vários espaços dentro da variável.

print(curso.strip()) # Elimina os espaços laterais e centraliza o conteúdo.

print(curso.rstrip()) # Elimina os espaços da DIREITA do conteúdo.

print(curso.lstrip()) # Elimina os espaços da ESQUERDA do conteúdo.

#============================================================================================================

# JUNÇÕES E CENTRALIZAÇÃO DE STRINGS

linguagem = 'Python'

print(linguagem.center(10 , '#')) # resultado>>> ##Python##
# o parâmetro 10 é opcional, e mostra quantos caracteres terá no total.
# o caractere '#' é o que será colocado junto ao conteúdo para suprir a quantidade de caracteres desejados, no caso, 10.abs

print('.'.join(linguagem)) # resultado>>> P.y.t.h.o.n

# o join() junta o caractere desejado entre os caracteres da variável.
#=============================================================================================================

# FATIAMENTO DE STRINGS (SLICE)

# lembrando que o ZERO conta como prieira posição, por ser zero based.
nome = 'João Pedro Marcondes de Assis'

print(nome[0]) # Trás somente o primeiro caractére da variável, no caso o 'J'

print(nome[:5]) # Trás os caractéres ATÈ o caractere 6 que seria o espaço depois do 'Pedro'

print(nome[5:10]) # trás os caracteres A PARTIR DO caractere 5 ATÉ o 10, no caso, 'Pedro'

print(nome[5:]) # como não devinimos o último parâmetro, ele trás tudo A PARTIR do caractere 5, no caso, 'Pedro Marcondes de Assis'

print(nome[:]) # com o início e fim não definidos, ele irá trazer todo o conteúdo.

print(nome[::2]) # sem o parâmetro de início e fim, porém com o step definido em 2, irá trazer letra sim e letra não.

print(nome[::-1]) # trás todo o conteúdo porém de trás pra frente