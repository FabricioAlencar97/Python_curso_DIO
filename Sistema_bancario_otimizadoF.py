import textwrap


def menu():
    menu = """\n
    ===================menu===================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tLista contas
    [nu]\tNovo usuário
    [q]\tSair
    =>"""
    
    return input(textwrap.dedent(menu))

def depositar(saldo,valor,extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}n"
        print("\n=== Depósito realizado com sucesso!===")
    else: 
        print("\nxxx Operção falhou! o valor informado não é valido. tente novamente xxx")
    
    return saldo , extrato

def sacar(*, saldo , valor, extrato,limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques 
    
    if excedeu_saldo:
        print("\nxxx Operação falhou! você não tem saldo sulficiente. xxx")
        
    elif excedeu_limite:
        print("\nxxx Operação falhou! o valor maximo de saque excede o limite diario. xxx")
   
    elif excedeu_saques:
        print("\n xxx operação falhou! numero maximo de saque excedido xxx ")
        
    elif valor > 0:
        saldo -= valor
        extrato += f"saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n ===Saque realizado com sucesso!===")
     
    else:
        print("\n Operação falhou!. ")
        
    return saldo,extrato
    
def exibir_extrato(saldo, /,*,extrato):
    print("n==================extrato==================")
    print ( "não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("=============================================")
        
        
def criar_usuario(usuarios):
    cpf=input("informe o cpf (somente numeros):")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
      print("\nxxx Ja existe usuario com esse CPF! xxx")        
      return

    nome = input ("informe  o nome completo:")
    data_nascimento = input("informe a data de nascimento (dd-mm-aaaa) :")
    endereço = input("informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
     
    usuarios.append({"nome":nome, "data_nascimento": data_nascimento,"cpf":cpf ,"endereço":endereço})
     
    print("===usuario criado com sucesso===")
     
     
def filtrar_usuario (cpf,usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf']==cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("informe o cpf do usuarios:")
    usuario = filtrar_usuario(cpf,usuarios)
    
    if usuario:
        print("\n=== conta criada com sucesso===")
        return {"agencia": agencia, "numero_conta":numero_conta, "usuario": usuario}
    
    print("\nxxx Usuario não encontrado, fluxo de criação de conta encerrado!xxx")
    
    
def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            agencia:\t{conta["agencia"]}
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
    extrato=""           
    numero_saques = 0
    usuarios= []
    contas = []
    
    while True :
        opcao = menu()
        if opcao =="d":
           valor=float(input("informe o valor do deposito:"))
           saldo , extrato = depositar(saldo, valor, extrato)
        elif opcao =="s":
           valor=float(input("informe o valor do saque:"))
        
           saldo,extrato =sacar(
            saldo = saldo,
            valor = valor,
            extrato = extrato,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES,
        )
        
        elif opcao == "e":
            exibir_extrato (saldo,extrato=extrato)
        
        elif opcao == "nu":
             criar_usuario(usuarios)
    
        elif opcao == "nc":   
            numero_conta = len(contas) +1
            conta = criar_conta(AGENCIA, numero_conta , usuarios)
    
        if conta:
           contas.append(conta)
    
        elif opcao == "lc":
            listar_contas(contas)
        
        elif opcao == "q":
           break

        else: 
            print("operação invalida,por favor selecione novamente a operação desejada!") 
        
        
main()             
        
        
        