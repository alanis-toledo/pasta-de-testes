
import random

numero_rand = random.randint(1, 100)
tentativas = 0
while True:
    tentativas += 1
    numero = int(input("Digite um número entre 1 e 100: "))
    
    if numero < numero_rand:
        print("O número é maior.")
    elif numero > numero_rand:
        print("O número é menor.")
    else:
        print(f"Parabéns! Você acertou o número {numero_rand} em {tentativas} tentativas.")