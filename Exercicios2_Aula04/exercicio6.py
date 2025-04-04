j = 0 
numero = 2  

while j < 10:
    primo = True
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            primo = False
            break

    if primo:
        print(numero)
        j += 1

    numero += 1
