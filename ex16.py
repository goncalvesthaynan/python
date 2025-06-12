dinheiro = float(input("Quanto de dinheiro você tem na conta? "))
compras = float(input("Qual o valor das compras do mês? "))

if(dinheiro>=compras):
    print("Você tem saldo suficiente!")
else:
    print("Você não tem saldo suficiente!")