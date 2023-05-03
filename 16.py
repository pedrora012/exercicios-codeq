#Exercício 16
C, P, F = map(int, input().split())

if 1 <= C <= 1000 and 1 <= P <= 1000 and 1 <= F <= 1000:
    if P/F >= C:
        print("S")
    else:
        print("N")
else:
    print("Valores inválidos")