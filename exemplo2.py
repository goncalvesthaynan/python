a = int(input("Digite um número!"))

if(a > 10):
    print("Deu certo!")
else:
    print("Deu errado!")

if(a > 10 and a < 20):
    print("Deu certo1!")
elif(a > 30 or a >50): #elif equivale a senão se
    print("Deu certo2!")
else:
    print("Deu errado!")
