i = 0
num = []

while i < 10:
    num2 = int(input("Insira um número: "))
    num.append(num2)
    i += 1

for n in num:
    if n % 2 == 0:
        print(f"{n} é par")
    else:
        print(f"{n} é ímpar")
