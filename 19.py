#Exercício 19
n, m = input().split()
n = int(n)
m = int(m)
if n < 1 or n > 100 or m < 1 or m > 100:
    print("Imput inválido (1 <= n, m <= 100)")
else:
    result = n ** m
    num_digits = len(str(result))
    print(num_digits)