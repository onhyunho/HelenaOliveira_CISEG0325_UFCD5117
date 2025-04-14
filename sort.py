def validar_nome(nome):
    partes = nome.split()
    if len(partes) != 2:
        return False
    primeiro_nome, ultimo_nome = partes
    return primeiro_nome.istitle() and ultimo_nome.istitle()

def adicionar_nome(lista, nome, idade):
    if validar_nome(nome):
        lista.append((nome, idade))
    else:
        print("Nome inválido. O nome deve ter o formato 'Primeiro Último'.")

def remover_nome(lista, nome):
    for i in range(len(lista)):
        if lista[i][0] == nome:
            del lista[i]
            return
    print(f"Nome '{nome}' não encontrado na lista.")

def ordenar_nomes(lista, por='primeiro'):
    def comparar_nomes(item1, item2):
        nome1, _ = item1
        nome2, _ = item2
        
        if por == 'primeiro':
            return nome1 < nome2
        else: 
            ultimo_nome1 = nome1.split()[1]
            ultimo_nome2 = nome2.split()[1]
            return ultimo_nome1 < ultimo_nome2

    for i in range(len(lista)):
        for j in range(0, len(lista) - i - 1):
            if not comparar_nomes(lista[j], lista[j + 1]):
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

def listar_nomes(lista, por='primeiro'):
    ordenar_nomes(lista, por)
    for nome, idade in lista:
        print(f"{nome} - Idade: {idade}")

def main():
    lista_nomes = []
    
    while True:
        acao = input("Deseja adicionar um nome (a), remover um nome (r), listar nomes (l) ou sair (s)? ").lower()
        
        if acao == 'a':
            nome = input("Digite o nome (Primeiro Último): ")
            idade = input("Digite a idade: ")
            adicionar_nome(lista_nomes, nome, idade)
        
        elif acao == 'r':
            nome = input("Digite o nome a remover (Primeiro Último): ")
            remover_nome(lista_nomes, nome)
        
        elif acao == 'l':
            tipo_listagem = input("Listar por primeiro nome (p) ou último nome (u)? ").lower()
            if tipo_listagem == 'p':
                listar_nomes(lista_nomes, por='primeiro')
            elif tipo_listagem == 'u':
                listar_nomes(lista_nomes, por='ultimo')
            else:
                print("Opção inválida.")
        
        elif acao == 's':
            print("Saindo do programa.")
            break
        
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()