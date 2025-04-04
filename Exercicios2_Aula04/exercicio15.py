def eascii():
    i = 0
    while i <= 255:
        for j in range(i, i + 20):
            if j > 255:  
                break
            print(f"ASCII {j}: {chr(j)}")
        
        resposta = input("\nDeseja continuar? Se quiser clique 's': ")
        if resposta != 's':
            break
        i += 20

eascii()
