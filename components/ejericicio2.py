import math

#. Derivada Sucesiva (F. Cıclica):
def derivada_ciclica():
    print("\n--- Resolviendo Problema 2: Derivada Sucesiva ---")
    print("Modelo original: y = sin(2x)")
    print("Fórmula analítica (y'''): -8 * cos(2x)")

    try:
        entrada = input("Ingrese el valor de x (en radianes): ")
        x = float(entrada)

        resultado = -8 * math.cos(2 * x)
        print(f"\n=> El valor numérico de la tercera derivada cuando x = {x} es: {resultado:.4f}")

        print("**"*20)
    except ValueError:
        print("\n[!] Error: Por favor ingrese un número decimal o entero válido.")
        
    print("-------------------------------------------------")    