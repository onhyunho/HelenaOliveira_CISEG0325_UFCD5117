def primos(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def divisores(num):
    divisores_lista = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisores_lista.append(i)
    return len(divisores_lista), divisores_lista

def numper(num):
    soma = 0
    for i in range(1, num):
        if num % i == 0:
            soma += i
    return soma == num

def calculadora():
    operacao = input("Qual operação deseja realizar? (+, -, *, /): ")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    match operacao:
        case "+":
            print(f"O resultado da operação é: {num1 + num2}")
        case "-":
            print(f"O resultado da operação é: {num1 - num2}")
        case "/":
            if num2 != 0:
                print(f"O resultado da operação é: {num1 / num2}")
            else:
                print("Não é possível realizar divisão por zero!")
        case "*":
            print(f"O resultado da operação é: {num1 * num2}")
        case _:
            print("Operação inválida!")

def tabuada():
    numero = int(input("Digite o número para a tabuada: "))
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

def analisar_numero():
    numero = int(input("Digite um número para análise: "))
    if numero < 1:
        print("Número inválido. Digite um número positivo.")
        return

    print(f"Número {numero}:")
    print(f"Primo: {primos(numero)}")
    quantidade_divisores, lista_divisores = divisores(numero)
    print(f"Quantidade de divisores: {quantidade_divisores}")
    print(f"Divisores: {lista_divisores}")
    print(f"Número perfeito: {numper(numero)}")

def menu():
    while True:
        print("\nEscolha uma opção:")
        print("1. Analisar número")
        print("2. Calculadora")
        print("3. Tabuada")
        print("4. Sair")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            analisar_numero()
        elif opcao == "2":
            calculadora()
        elif opcao == "3":
            tabuada()
        elif opcao == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()