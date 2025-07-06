#DESAFIO 5


def cal_desconto(valor):
    if valor <= 100:
        desconto = 0
    elif valor <= 300:
        desconto = 0.10
    elif valor <= 500:
        desconto = 0.15
    else:
        desconto = 0.20
    valor_final = valor - (valor * desconto)
   
    print(f"O valor final da compra com desconto é: R$ {valor_final:.2f}") 
    
valor = float(input("Digite o valor total da compra: R$ "))
cal_desconto(valor) 
