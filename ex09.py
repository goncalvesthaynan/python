divida = float(input("Qual o valor da sua divida? "))
tempo = int(input("Há quanto tempo você tem essa dívida? "))
taxa = float(input("Qual a taxa de juros? "))

juros = float(divida*tempo*taxa)
total = float(divida+juros)

print("Os juros da sua dívida são de " + str(juros) + " e o valor total será de " + str(total))