num  = int(input("Insira um número de 1 a 10: "))
i = 0

for i in range(1, 11):
    tab = num * i
    print(f"{num} * {i} = {tab}")