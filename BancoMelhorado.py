import textwrap

def menu(): 
    menu = '''\m
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]Nova conta
    [lc]Listar contas
    [nu]\tNovo usuário
    [q]\tSair
    => '''
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /): 
    if valor > 0: 
        saldo += valor 
        extrato += f'Depósito:\tR$ {valor:.2f}\n'
        print('Deposito realizado com sucesso') 
    else: 
        print('Falha na operação.')

    return saldo, extrato 

def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo 
    excedeu_limite = valor > limite 
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo: 
        print('Falha na operação')
    elif excedeu_limite: 
        print('Falha na operação')
    elif excedeu_saques: 
        print('Falha na operação')
    elif valor > 0: 
        saldo -= valor 
        extrato += f'Saque:\tR$ {valor:.2f}\n'
        numero_saques += 1 
        print('Saque realizado com sucesso')
    else: 
        print('Falha na operação')

    return saldo, extrato

def exibir_extrato(saldo, extrato): 
    print('\n======== EXTRATO ========')
    print(f'\nSaldo:\t\tR$ {saldo:.2f}')
    print('===========================')

def criar_usuario(usuarios): 
    cpf = input('Digite o seu CPF: ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario: 
        print('Já existe um usuário.')
        return
    
    nome = input('Digite o seu nome completo: ')
    data_nasc = input('Digite a sua data de nascimento: ')
    endereco = input('Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ')

    usuarios.append({'nome': nome, 'data_nasc': data_nasc, 'cpf': cpf, 'endereco': endereco})

    print('Usuário criada')

def filtrar_usuario(cpf, usuarios): 
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None 

def criar_conta(agencia, numero_conta, usuarios): 
    cpf = input('Digite o CPF do usuário: ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('Conta criada com suceso!')
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print('CPF não encontrado')

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


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
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()




