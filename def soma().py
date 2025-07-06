def soma(N1,N2):
    Resultado = N1 + N2

    print(f'A soma de {N1} + {N2} é igual a {Resultado}')

def subtracao(N1,N2):
    Resultado = N1 - N2

    print(f'A subtração de {N1} - {N2} é igual a {Resultado}')

def multiplicacao(N1,N2):
    Resultado = N1 * N2

    print(f'A multiplicação de {N1} * {N2} é igual a {Resultado}')

def divisao(N1,N2):
    if N2 != 0:
        Resultado = N1 / N2
        print(f'A divisão de {N1} / {N2} é igual a {Resultado}')
    else:
        print("Divisão por zero não é permitida.")


N1 = int(input('selecione um numero ' ))
N2 = int(input('selecione um novo numero ' ))

soma(N1,N2)
subtracao(N1,N2)
multiplicacao(N1,N2)
divisao(N1,N2)

'''file = 'arquivo.txt'

arquivo_leitura = open(file, 'w')
arquivo_leitura.write("Arquivo criado com sucesso!")'''


file = 'arquivo.txt'
arquivo_leitura = open(file, 'w')
arquivo_leitura.write("Arquivo criado com sucesso!")
arquivo_leitura.close()
