idade = int(input("Qual sua idade? "))
nacionalidade = str(input("Qual sua nacionalidade? "))
genero = str(input("Qual gênero você se identifica? "))

if(idade == 18 and nacionalidade == "Brasileira" and genero == "Masculino"):
    print("Apto!")
else:
    print("Inapto!")