preco = float(input("Qual o preço do produto? "))
porcentagem = float(input("Qual a porcentagem do desconto? "))

desconto = float((preco*porcentagem)/100)
novopreco = float(preco-desconto)

print("O produto custava "+ str(preco) + " mas teve desconto de " + str(desconto) + " %, por isso agora está custando " + str(novopreco) + " reais." )
