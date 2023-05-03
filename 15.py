#Exercício 15
musicas = ["PROXYCITY","P.Y.N.G.","DNSUEY!","SERVERS","HOST!","CRIPTONIZE","OFFLINE DAY","SALT","ANSWER!","RAR?","WIFI ANTENNAS"]

C = int(input())

for i in range(C):
    while True:
        X, Y = map(int, input("Insira os botões (0-5) para o caso {}: ".format(i+1)).split())
        if X < 0 or X > 5 or Y < 0 or Y > 5:
            print("Botão inválido. Digite novamente.")
        else:
            break
    soma = X + Y
    print(musicas[soma])