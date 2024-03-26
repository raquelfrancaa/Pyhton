def menu():
    menu = """
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [u]\tCadastrar Usuário
    [c]\tCadastrar Conta Bancária
    [l]\tListar Contas
    [q]\tSair
    => """
    return input(menu)

def depositar(saldo, valor, extrato, /):

    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def sacar(*, saldo, extrato, numero_saques, limite, LIMITE_SAQUES):
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saques:
        print("Operação falhou! Limite diário de saques excedido.")
    else:
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite

        if valor > 0:
            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")
            elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite.")
            else:
                saldo -= valor
                extrato += f"Saque:\t\tR$ {valor:.2f}\n"
                numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques
    
def exibir_extrato(extrato,/,*, saldo):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def encontrar_usuario(usuarios, cpf):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None

def cadastrar_usuario(usuarios):
    numero = input("Digite o cpf: ").strip()
    cpf = ""

    for i in numero:
        if i.isnumeric():
            cpf += i 

    usuario = encontrar_usuario(usuarios, cpf)
    
    if usuario is not None:
        print("Já existe usuário com esse cpf!")
    else:
        novo_usuario = {}
        novo_usuario["nome"] = input("Informe o nome completo: ")
        novo_usuario["cpf"] = cpf
        novo_usuario["data_nasc"] = input("Informe a data de nascimento (dd-mm-aaaa): ")
        novo_usuario["endereco"] = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

        usuarios.append(novo_usuario)
        print("Novo usuário cadastrado com sucesso!")

    return usuarios

def cadastrar_conta(contas, AGENCIA, usuarios):
    print("Cadastrar conta bancária")
    numero = input("Digite o cpf do usuário para o qual deseja cadastrar a conta: ").strip()
    cpf = ""

    for i in numero:
        if i.isnumeric():
            cpf += i

    usuario = encontrar_usuario(usuarios, cpf)

    if usuario:
        nova_conta = {}
        nova_conta["agencia"] = AGENCIA
        nova_conta["numero_conta"] = len(contas) + 1
        nova_conta["cpf_usuario"] = cpf
        nova_conta["nome_usuario"] = usuario["nome"]
        contas.append(nova_conta)
        print("Conta cadastrada com sucesso!")
    else:
        print("Usuário não encontrado, fluxo de criação de conta encerrado!")
    
    return contas

def listar_contas(contas):
    linha = ""
    for conta in contas:
        linha = f"""
    Agência:\t{conta["agencia"]}
    C/C:\t{conta["numero_conta"]}
    Títular:\t{conta["nome_usuario"]}
    """
        print("=" * 100)
        print(linha)
        

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":

            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)  

        elif opcao == "s":
            
            saldo, extrato, numero_saques = sacar(saldo=saldo, extrato=extrato, numero_saques=numero_saques, limite=limite, LIMITE_SAQUES=LIMITE_SAQUES)

        elif opcao == "e":

            exibir_extrato(extrato, saldo=saldo)

        elif opcao == "u":

            usuarios = cadastrar_usuario(usuarios)

        elif opcao == "c":
            
            contas = cadastrar_conta(contas, AGENCIA, usuarios)
        
        elif opcao == "l":
            
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()