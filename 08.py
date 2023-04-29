#Exercício 8
a, b, c = map(float, input().split())

delta = (b*b) - (4*a*c)

if delta <= 0.0:
    R1 = ( (-b) + ((delta)**0.5) ) / (2*a)
    R2 = ( (-b) - ((delta)**0.5) ) / (2*a)
    print(round(R1,5))
    print(round(R2,5))
else: print("Impossivel calcular")
