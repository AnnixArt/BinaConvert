A = float(input("veuillez saisir le premiere nombre: "))
oper = input("veuillez selectionner un operateur: ")
B = float(input("veuillez sasir la deuxieme noombre: "))

if oper == "+":
    print(A+B)
if oper == "X":
    print(A*B)
if oper == "-":
        print(A - B)
if oper == "/":

    print(A/B)

if oper == "%":
    print(A%B)
    print("voulez vous continuer ?")
else:
    print("l'operateur n'existe pas:")