nota1 = int(input("Digite a primeira nota! "))
nota2 = int(input("Digite a segunda nota! "))
nota3 = int(input("Digite a terceira nota! "))

soma = float(nota1+nota2+nota3)
media = float(soma/3)

print("A média desse aluno é " + str(media) + " pontos? ")

nota4 = int(input("Digite a quarta nota! "))

novasoma = float(soma+nota4)
novamedia = float(novasoma/4)

print("A nova média será de " + str(novamedia))