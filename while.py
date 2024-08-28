opcao = -1

while opcao != 0:
    opcao = int(input('[1] Sacar \n[2] Extrato \n[3] Sair \n'))
    
    if opcao == 1:
        print('Efetuando o saque...')
        
    elif opcao == 2:
        print('Carregando o extrato...')
        
    elif opcao == 3:
        print('Saindo...')
        
else:
    print('Obrigado por utilizar nosso sistema bancário, volte sempre!')
        
    