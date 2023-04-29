#Exercício 18
B = int(input()) #qtd bolinhas
G = int(input()) #qtd galhos

if G%2 > 0: G=G-1 #arredondar pra baixo valor ímpar
P = G/2

faltam = int(P - B)

if faltam > 0:
        print('Faltam', faltam, 'bolinha(s)')
elif faltam == 0:
        print('Amelia tem todas bolinhas!')
