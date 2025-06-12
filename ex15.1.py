km = int(input("Qual a quantidade de quilômetros percorridos pelo carro alugado? "))
dias = int(input("Por quantos dias ele foi alugado? "))

precodia = float(dias*60.00)
precokm = float(km*0.15)

precototal = float(precodia+precokm)

print("O valor a pagar pelo aluguel do carro é de "+ str(precototal) + " reais")