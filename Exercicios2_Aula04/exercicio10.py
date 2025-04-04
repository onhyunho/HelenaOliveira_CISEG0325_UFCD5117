num = int(input("Escreva um número: "))
i = 0

for j in range(1, num + 1):
    if num % j == 0:
        i += 1

print(f"{num}: {i} divisores.")
