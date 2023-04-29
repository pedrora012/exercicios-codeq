nf = int(input()) #Número do funcionário
nh = int(input()) #Número de horas trabalhadas
vph = float(input()) #Valor por hora trabalhada

sal = nh * vph #Salário

print("NUMBER = %.0f\nSALARY = U$ %0.2f "% (nf, sal,))
