#Exercício 11
linha1 = input().split()
p = int(linha1[0]) #altura dos pulos
n = int(linha1[1]) #número de canos

a = input().split() #altura dos canos
for i in range(len(a)):
    a[i] = int(a[i])

def pulo(c1,c2,p): #função do pulo
    if abs(c1-c2) > p:
        return False
    else:
        return True
    
for i in range(n-1):
        x = pulo(a[i],a[i+1],p)
        if x == False:
            print('GAME OVER')
else: print('YOU WIN')
