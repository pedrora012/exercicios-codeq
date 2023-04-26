ida = int(input()) #Idade em dias

ano = int(ida/365)
print(ano,"ano (s)") #Anos inteiros

meses = int((ida%365)/30)
print(meses, "mes (es)") #Meses inteiros

dias = int((ida%365)%30) #Dias que sobram
print(dias,"dia (s)")