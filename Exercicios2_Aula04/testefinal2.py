class Cliente:
    contador = 1 

    def __init__(self, nome, morada, tel, nif, compra):
        self.numcli = Cliente.contador
        Cliente.contador += 1
        self.nome = nome
        self.morada = morada
        self.tel = tel
        self.nif = nif
        self.compra = compra
        self.divfin = self.calcular_divfin()

    def calcular_divfin(self):
        if 100 <= self.compra <= 200:
            desconto = 0.05
        elif 200 < self.compra < 500:
            desconto = 0.10
        elif self.compra >= 500:
            desconto = 0.15
        else:
            desconto = 0
        return self.compra * (1 - desconto)

    def mostrar(self):
        print(f"\nNúmero do Cliente: {self.numcli}")
        print(f"Nome: {self.nome}")
        print(f"Morada: {self.morada}")
        print(f"Telefone: {self.tel}")
        print(f"NIF: {self.nif}")
        print(f"Compra: €{self.compra:.2f}")
        print(f"Divida Final (com desconto): €{self.divfin:.2f}")


def validar_telefone(tel):
    return tel.isdigit() and len(tel) in (9, 10)


def validar_nif(nif):
    return nif.isdigit() and len(nif) == 9


def validar_compra(valor):
    try:
        valor = float(valor)
        return valor >= 0
    except ValueError:
        return False


def inserir_cliente(clientes):
    nome = input("Nome do cliente: ").strip()
    morada = input("Morada: ").strip()

    while True:
        tel = input("Telefone: ").strip()
        if validar_telefone(tel):
            break
        print("Telefone inválido. Deve conter 9 ou 10 dígitos.")

    while True:
        nif = input("NIF: ").strip()
        if validar_nif(nif):
            break
        print("NIF inválido. Deve conter 9 dígitos.")

    while True:
        compra = input("Valor da compra (€): ").strip()
        if validar_compra(compra):
            compra = float(compra)
            break
        print("Valor da compra inválido.")

    cliente = Cliente(nome, morada, tel, nif, compra)
    clientes.append(cliente)
    print("Cliente inserido com sucesso!")


def listar_clientes(clientes):
    if not clientes:
        print("Nenhum cliente registrado.")
        return
    for cliente in clientes:
        cliente.mostrar()
        input("Pressione Enter para ver o próximo cliente...")


def buscar_cliente(clientes):
    try:
        num = int(input("Digite o número do cliente (NumCli): "))
    except ValueError:
        print("Número inválido.")
        return

    for cliente in clientes:
        if cliente.numcli == num:
            cliente.mostrar()
            return
    print("Cliente não encontrado.")


def menu():
    clientes = []

    while True:
        print("\n=== MENU CLIENTES ===")
        print("1. Inserir novo cliente")
        print("2. Listar todos os clientes")
        print("3. Buscar cliente por número")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            inserir_cliente(clientes)
        elif opcao == "2":
            listar_clientes(clientes)
        elif opcao == "3":
            buscar_cliente(clientes)
        elif opcao == "4":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
