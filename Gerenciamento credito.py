saldo = 10000.0
credito = float(input("Digite o valor para ser creditado"))
if credito <= 0 :
    print("Valor Invalido")
else :
    saldo += credito
    print (f"Saldo final e {saldo}")


