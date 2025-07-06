
P1 = int(input('Insira a primeira nota a ser computada: ' ))

P2 = int(input('Insira a segunda nota a ser computada: ' ))

P3 = int(input('Insira a terceira nota a ser computada: ' ))

def calcular_media(P1, P2, P3): 
    media = (P1 + P2 + P3) / 3
    if media >= 9:
        conceito = 'A'
    elif media >= 7:
        conceito = 'B'
    elif media >= 6:
        conceito = 'C'
    else:
        conceito = 'D'
    return media, conceito


media, conceito = calcular_media(P1, P2, P3)

print(f'A sua média é {media} e o conceito é {conceito}!')