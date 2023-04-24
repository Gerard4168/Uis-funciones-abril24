

def multiplos(m):
    if m %10 == 4:
        print("---------------------")
        print("Su ultimo digito es 4")
        print("---------------------")
    else:
        print("------------------------")
        print("Su ultimo digito no es 4")
        print("------------------------")
m=int(input("ingrese un numero de 4 digitos: "))
multiplos(m)
