#Exercício 10
ng = 0 #numero de grenais
intgan = 0 #Vitórias Inter
gregan = 0 #Vitórias Gremio
emp = 0 #Empates
novo = 1 #Novo grenal? (1-sim 2-nao)
while novo == 1:
    ng = ng + 1
    placar = input().split()
    i = float(placar[0])
    g = float(placar[1])

    if i > g: intgan = intgan + 1
    if g > i: gregan = gregan + 1
    if i == g: emp = emp + 1 
    novo = int(input('Novo grenal? (1-sim 2-nao)'))
else:
    print(ng,"grenais")
    print("Inter: ",intgan)
    print("Gremio: ",gregan)
    print("Empates: ", emp)
if gregan == intgan:
        print("Nao houve vencedor")
elif intgan > gregan:
     print( "Inter venceu mais")
else:
     print("Gremio venceu mais")