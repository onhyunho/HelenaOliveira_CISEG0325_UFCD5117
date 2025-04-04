segundos = int(input("Digite a quantidade de segundos: "))

horas = segundos // 3600
segundos = segundos % 3600
minutos = segundos // 60
segundos = segundos % 60

print(f"{horas} horas, {minutos} minutos e {segundos} segundos")