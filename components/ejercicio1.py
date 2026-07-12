import math

# 1. Derivada Sucesiva (F. Trascendental):
def derivada_trascendental():
    print("\n--- Resolviendo Problema 1: Derivada Sucesiva (F. Trascendental) ---")
    print("Modelo original: f(x) = x^2 * e^x")
    print("Fórmula analítica (f''): e^x * (x^2 + 4x + 2)")

    try:
        entrada = input("Ingrese el valor de x: ")
        x = float(entrada)

        resultado = math.exp(x) * (x**2 + 4*x + 2)
        print(f"\n=> El valor numérico de la segunda derivada cuando x = {x} es: {resultado:.4f}")

        print("**"*20)
    except ValueError:
        print("\n[!] Error: Por favor ingrese un número decimal o entero válido.")

    print("-------------------------------------------------")