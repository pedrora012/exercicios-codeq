#Exercício 4
A, B, C = map(float, input().split()) #Ler entradas e transformar em float
pi = 3.14159
tri = (A*C)/2
cir = pi*C**2
tra = ((A+B)*C)/2
quad= B*B
ret = A*B

#print(A,B,C)
#print("TRIANGULO:", round(tri,3))
#print("CIRCULO:", round(cir,3))
#print("TRAPEZIO:", round(tra,3))
#print("QUADRADO:", round(quad,3))
#print("RETANGULO:", round(ret,3))

print("TRIANGULO: %0.3f\nCIRCULO: %0.3f\nTRAPEZIO: %0.3f\nQUADRADO: %0.3f\nRETANGULO: %0.3f" % (tri, cir, tra, quad, ret))