nome_cliente = input("Insira o seu nome: ")
valor_compra = float(input("Insira o valor da compra: "))

percent = 10 if valor_compra <= 200 else 15 if valor_compra <= 500 else 20

desconto = (percent/100)*valor_compra
total = valor_compra - desconto

print(f"\nCliente: {nome_cliente}\nCompra: {valor_compra:.2f}€ \nDesconto: {percent}%\nDesconto: {desconto:.2f}€\nTotal: {total:.2f}€")
