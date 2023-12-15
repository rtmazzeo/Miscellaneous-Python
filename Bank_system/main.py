saldo = 0
saques_diarios = 3
depositos = []
saques = []

def extrato():
    global saldo
    if not depositos and not saques:
        print("Não foram realizadas movimentações.")
        print(f"Saldo disponível: R$ {saldo:.2f}\n")
    else:
        print("\nExtrato:\n")
        for deposito in depositos:
            print(f"Depósito: R$ {deposito:.2f}.\n")
        for saque in saques:
            print(f"Saque: R$ {saque:.2f}.")
        print(f"\nSaldo disponível: R$ {saldo:.2f}.\n")

def depositar(valor):
  global saldo
  
  from rich import print as rprint
  from rich.panel import Panel
  
  if valor <=0:
    rprint(Panel("O valor para depósito deve ser maior que zero.",width = 60))
  else:
    saldo += valor
    depositos.append(valor)
    rprint(Panel(f"Deposito de R$ {valor:.2f} realizado com sucesso.",width = 60))
    return

def sacar(valor):
  global saldo, saques_diarios

  limite_saque_diario = 500
  
  if valor <=0:
    print("O valor para saque deve ser maior que zero.\n")
  elif saques_diarios == 0:
    print("Limite diário de saques atingido. Tente novamente amanhã.\n")
  elif valor > saldo or valor > limite_saque_diario:
    print("Valor de saque inválido. Verifique seu saldo ou seu limite diário.\n")
  else:
    saldo -= valor
    saques_diarios -= 1
    limite_saque_diario -= valor
    saques.append(valor)
    print(f"Saque de R$ {valor:.2f} realizado com sucesso.\n")

def main():
    
    while True:

        from rich import print as rprint
        from rich.panel import Panel

        rprint(Panel("[ 0 ] Extrato\n[ 1 ] Depositar\n[ 2 ] Sacar\n[ q ] Sair", title="Menu",width = 20))

        opcao = input("\nQual a opção desejada?")

        if opcao == '0':
            extrato()
        elif opcao == '1':
            valor = float(input("Digite o valor a ser depositado: "))
            depositar(valor)
        elif opcao == '2':
            valor = float(input("Digite o valor a ser sacado: "))
            sacar(valor)
        elif opcao.lower() == 'q':
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")

main()