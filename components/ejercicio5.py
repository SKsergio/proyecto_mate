#Ejercicio 5

def calcular_pendiente(x, y):
    return -x/y

print("//////////////////////////////////////////////")
print("----- EJERCICIO 5 - DERIVACION IMPLICITA -----")
print("//////////////////////////////////////////////")

x = float(input("Ingrese el valor de x: "))
y = float(input("Ingrese el valor de y: "))

if y == 0:
    print("\n Error, la variable y no puede tener un valor 0")
else:
    pendiende = calcular_pendiente(x,y)

    print("\n El resultado es: ")
    print("//////////////////////////////")
    print(f"x = {x}")
    print(f"y = {y}")
    print(f"dy/dx = {pendiende}")

    if x == 6 and y == 8:
        print("Pendiente exacta: -3/4 (-0.75)")
    else:
        print("No hay pendiente exacta para el ejercicio 3")