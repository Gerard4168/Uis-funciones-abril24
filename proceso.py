print("--------------------------------")
print("----- Numero a multiplicar -----")
print("--------------------------------")

#Definición de la función
def multiplos(m):
    print("Tabla del ", m)
    for i in range(1,11):
        z=m*i
        print(m,"*", i,"=", z)

m=int(input("ingrese el numero a multiplicar: "))

multiplos(m)
#Procesamiento

