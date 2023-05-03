#Exercício 14
votes = []
while True:
    try:
        n = input()
    except EOFError: #( Ctrl + Z + Enter)
        break
        
    votes += list(map(int, n.split()))

favor = sum(votes)
if favor >= 2 * len(votes) / 3:
    print("impeachment")
else:
    print("acusacao arquivada")
