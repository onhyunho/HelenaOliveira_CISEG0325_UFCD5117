saldo = float(input("Insira o saldo da conta: "))
cheque = float(input("Insira o valor do cheque: "))

if cheque <= saldo:
    saldo -= cheque
    print(f"O valor do cheque é válido. Saldo atual: {saldo}")
else:
    print("Saldo insuficiente. O valor do cheque é inválido.")