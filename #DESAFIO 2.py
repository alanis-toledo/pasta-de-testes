#DESAFIO 2
#Escreva um programa que receba uma string e mostre quantas vezes cada vogal (a, e, i, o, u) aparece na frase.

frase = str(input("Insira sua frase aqui: "))

vogais = {'a':0 , 'e':0 , 'i':0 , 'o':0 , 'u':0}

for letra in frase.lower():
    if letra in vogais:
        vogais[letra] += 1

print(f"A frase digitada foi: {frase}, e a contagem de vogais é: {vogais}")