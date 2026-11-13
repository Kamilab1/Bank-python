saldo = 10000.0
debito = float(input("digite o valor para ser debitado"))
if debito <= 0 :
    print("Valor invalido")
elif debito > saldo :
    print ("Saldo insuficiente")
else :
#isso e igual ao de baixo    saldo = saldo - debito
    saldo -= debito
    print (f"Saldo final e {saldo}")
