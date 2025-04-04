notas = []

cont = 1
while cont <= 10:
    nota = float(input(f"Digite a {cont}ª nota(0-20): "))
    if 0 <= nota <= 20:
        notas.append(nota)
        cont += 1
    else: 
        print("Nota inválida.")

soma = sum(notas)
media = soma / 10

ac_media = 0
for nota in notas:
    if nota >= media:
        ac_media += 1

print(f"\nMédia turma: {media:.2f}")
print(f"Quantidade de notas acima da média: {ac_media}")