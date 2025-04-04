i = 0
soma = 0

while i < 30:
    num = int(input("Insira um número entre 1 e 50(par): "))  
    
    
    if 1 <= num <= 50 and num % 2 == 0:
        soma += num  
        i += 1 
    else:
        print("Número inválido!")

media = soma / 30
print(f"Média: {media}")
