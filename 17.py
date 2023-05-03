#Exercício 17
p, j1, j2, r, a = map(int, input().split())

soma = j1 + j2
if p == 1:
    if soma % 2 == 0:
        vencedor = 1
    else:
        vencedor = 2
else:
    if soma % 2 != 0:
        vencedor = 1
    else:
        vencedor = 2

if r == 1:
    vencedor = 1
if a == 1:
    if r == 0:
        vencedor = 1
    else:
        vencedor = 2

if vencedor == 1:
    print("Jogador 1 ganha!")
else:
    print("Jogador 2 ganha!")
