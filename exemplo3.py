print("O que você prefere?")
print("[1] Pastel de Carne")
print("[2] Pastel de Queijo")
print("[3] Pastel de Frango")
r = int(input(""))

match r:
    case 1:
        print("Você gosta de Carne!")
    case 2:
        print("Você gosta de Queijo!")
    case 3:
        print("Você gosta de Frango!")
    case _:
        print("Opção Inválida!")

#escolha (r){
#   caso 1:
#       escreva("Gosta de Carne")
#       pare
#   caso 2:
#       escreva("Gosta de Queijo")
#       pare
#   caso contrario{
#       escreva("Opção Inválida")
#   }
#}

print("O que você prefere?")
print("[1] Pastel de Carne")
print("[2] Pastel de Queijo")
print("[3] Pastel de Frango")
r = str(input(""))

match r:
    case "carne":
        print("Você gosta de Carne!")
    case "queijo":
        print("Você gosta de Queijo!")
    case "frango":
        print("Você gosta de Frango!")
    case _:
        print("Opção Inválida!")
