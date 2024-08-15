def menu():    
    menu = """

    [1] - Depositar
    [2] - Sacar
    [3] - Extrato
    [4] - Criar Usuário
    [5] - Criar Conta
    [6] - Lista Conta
    [7] - Sair

    """
    return input(menu)

def Depositar(saldo, valor, extrato, /):

    if valor > 0:
        saldo+=valor
        extrato += f"Depósito R$ {valor:.2f}\n"

    else:
            print("A operação falhou")

    return saldo, extrato

def Saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("O saldo foi excedido")

    elif excedeu_limite:
        print("O limite foi excedido")
            
    elif excedeu_saques:
        print("O limite de saques foi excedido")

    elif valor > 0:
        saldo -= valor
        extrato += f"Seu saldo é de {valor:.2f}\n"
        numero_saques += 1

    else:
        print("Valor inválido")

    return saldo, extrato, numero_saques

def Extrato(saldo,/,*,extrato):

    print("<----------Extrato---------->")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("<--------------------------->")

def Criar_Usuario(usuarios):

    nome = input("Digite seu nome completo: ")
    cpf = input("Digite seu cpf: ")
    data_nasc = input("Digite sua data de nascimento(D/M/A): ")
    endereço = input("Digite seu endereço: (estado/cidade/local/numero): ")

    usuarios.append({"nome": nome, "cpf": cpf, "data_nascimento": data_nasc, "endereço": endereço})

    print("Seu usuário foi criado")

def Filtrar_Usuarios(cpf, usuarios):

    usuarios_filtrados = [usuario for usuario in usuarios if usuario ["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def Criar_Conta(AGENCIA, numero_conta, usuarios):

    cpf = input("Digite seu cpf: ")
    usuario = Filtrar_Usuarios(cpf, usuarios)

    if usuario:
        print("\nSua conta foi criada")
        return {"agência": AGENCIA, "conta": numero_conta, "usuario": usuario}
    else:
        print("Usuário não encontrado, não foi possível criar a conta")
        return None
    
def Listar_Conta(contas):

        for conta in contas:

            print(f"\nAgência: {conta['agência']}")

            print(f"\nConta: {conta['conta']}")

            print(f"\nUsuário: {conta["usuario"]['nome']}")

            print("-" * 55)

def main():

    AGENCIA = "0001"
    LIMITE_SAQUE = 3
    extrato = ""
    limite = 500
    saldo = 0
    numero_saques = 0
    usuarios = []
    contas = []


    while True:
        
        opcao = menu()

        if opcao == "1":

            valor = float(input("Digite o valor que deseja Depositar: "))

            saldo, extrato = Depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Digite o valor que deseja Sacar: "))

            saldo, extrato, numero_saques = Saque(

                saldo=saldo, 
                valor=valor, 
                extrato=extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUE
                
                )

        elif opcao == "3":
            
            Extrato(saldo, extrato=extrato)

        elif opcao == "4":

            Criar_Usuario(usuarios)

        elif opcao == "5":

            numero_conta = len(contas) +1
            conta = Criar_Conta(AGENCIA, numero_conta, usuarios)

            if conta:
                
                contas.append(conta)

        elif opcao == "6":

            Listar_Conta(contas)

        elif opcao == "7":
            break

        else:
            print("Operação inválida")


main()