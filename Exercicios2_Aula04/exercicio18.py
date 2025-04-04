def numper(num):
    soma = 0
    for i in range(1, num):
        if num % i == 0:  
            soma += i
    
    return soma == num

num = int(input("Insira um número: "))  
i = 0  

for numero in range(1, num + 1):
    if numper(numero):
        i += 1  

print(f"Existem {i} números perfeitos até {num}.")
