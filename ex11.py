peso = int(input("Qual o seu peso? "))
sand = int(input("Quantos sanduíches você comeu? "))

engordou = float(sand*0.100)
novopeso = float(peso+engordou)

gasto = float(sand*8.50)

print("O seu novo peso é de " + str(novopeso))
print("Você gastou em média " + str(gasto) + " reais com sanduíches!")