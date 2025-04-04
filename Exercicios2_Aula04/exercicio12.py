num = int(input("Insira um número: "))
i = 0
resultados = []

for j in range(1, num):
    soma = num + j
    sub = num - j
    div = num / j if j != 0 else "Indefinido" 
    mult = num * j

    i += 4  

    resultados.append(f"Com {j}:")
    resultados.append(f"Soma: {soma}")
    resultados.append(f"Subtração: {sub}")
    resultados.append(f"Divisão: {div}")
    resultados.append(f"Multiplicação: {mult}")
    resultados.append("-----------")

print("\n".join(resultados))

print(f"\nTotal de operações realizadas: {i}")
