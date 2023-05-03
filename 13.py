#Exercício 13
N = int(input())

if not 1 <= N <= 100:
    print("Número inválido de medidas (1 <= N <= 100)")
    exit()

Hi = list(map(int, input().split()))

if len(Hi) != N or not all(-10000 <= h <= 10000 for h in Hi):
    print("Valores ínvalidos para altura (-10000 <= Hi <= 10000)")
    exit()

padrao = True
for i in range(1, N):
    if (Hi[i] > Hi[i-1] and Hi[i] > Hi[(i+1)%N]) or (Hi[i] < Hi[i-1] and Hi[i] < Hi[(i+1)%N]):
        continue
    else:
        padrao = False
        break

if padrao:
    print("1")
else:
    print("0")








