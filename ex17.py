valor1 = int(input("Digite um número inteiro! "))
valor2 = int(input("Digite outro número inteiro! "))
valor3 = int(input("Digite mais um número inteiro! "))

contador = int(0)

if(valor1 > 25):
    contador = contador + 1
if(valor2 > 25):
    contador = contador + 1
if(valor3 > 25):
    contador = contador + 1

print("Encontramos " + str(contador) + " número(s) maior(es) do que 25!")