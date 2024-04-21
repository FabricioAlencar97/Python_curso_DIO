menu = """


[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """


saldo= 0
limite= 500
extrato= ""
numero_saques=0
LIMITE_SAQUES= 3
Sair="q"

while True:
    opção = input(menu)
    
    if opção =="d":
        valor = float(input("informe o valor do deposito: "))
        
        if valor >0:
            saldo += valor
            extrato += f"deposito: R$ {valor:.2f}\n"
            
        else:
            print("operação falhou! O valor informado é invalido.")
            
    
    elif opção == "s" :
        valor = float(input("informe o valor do saque: "))
        
        excedeu_saldo  = valor > saldo
        
        excedeu_limite = valor > limite 
        
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Operação falhou! Voce não tem saldo sulficiente.")
            
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite")
            
        elif excedeu_saques:
            print("Operação falhou! Numero maximo de saques excedido")
            
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            
            
        else:
            print("Operação falhou! O valor informado é invalido.")
            
    elif opção == "e" :
        print ("\n===============EXTRATO===============")
        print ("não foram realizados movimentaçoes." if not extrato else extrato)
        print (f"\n Saldo: R$ {saldo:.2f}")
        print ("==========================================")
        
    elif opção == "q":
        print("obrigado por ser nosso cliente!")
        break
    
    else:
        print("operação invalida, por favor selecione novamente a operação desejada")

                
    