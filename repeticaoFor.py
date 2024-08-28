# Estrutura de repetiçao utilizando o FOR

texto = str(input('Digite algum texto: '))

VOGAIS = 'AEIOU'

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end='')
        
else:
    print() # adiciona uma quebra de linha
    
    
# Usando a função de repetição IN RANGE
#Utilizamos 3 parâmetros no range, sendo o primeiro, obrigatório, e os 2 demais, opcionais.
# O primeiro é onde a contagem vai iniciar (0).
# O segundo é onde a contagem vai parar (20).
# O terceiro é os steps, de quanto em quanto será a contagem, no caso, (2).

for numero in range (0, 20, 2): # iniciamos no zero, vamos até 20 de 2 em 2, porém o 20 é ignorado.
    print(numero, end='')
    
# Exemplo com a tabuada do 5 no range    
for numero in range (0, 51, 5):
    print(numero, end=" ")
    
    
