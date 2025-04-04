alunos = 1
notas = []

while alunos < 11:
    notinhas = int(input(f"Insira a nota do(a) {alunos}º aluno(a): "))
    notas.append(notinhas)
    alunos += 1

media = sum(notas) / 10
print(f"\nA média da turma é: {media:.2f}")
