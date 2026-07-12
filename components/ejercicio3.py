#. Derivada Sucesiva (F. Cıclica):
def derivada_implicita_basica():
    print("\n--- Resolviendo Problema 3: Derivación Implícita Básica ---")
    print("Modelo original: x^2 + y^2 = 100")
    print("Fórmula analítica (dy/dx): -x / y")

    try:
        x = float(input("Ingrese el valor de la coordenada 'x': "))
        y = float(input("Ingrese el valor de la coordenada 'y': "))

        if y == 0:
            print(f"\n=> dy/dx = Indefinida (tangente vertical en y=0)")
        else:
            resultado = -x / y
            print(f"\n=> La pendiente (dy/dx) en el punto ({x}, {y}) es: {resultado:.4f}")

    except ValueError:
        print("\n[!] Error: Por favor ingrese un número decimal o entero válido.")
        
    print("-------------------------------------------------------------")