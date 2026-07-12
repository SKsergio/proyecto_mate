import math

# 4. Derivación Implícita Trascendental:
def derivada_implicita_trascendental():
    print("\n--- Resolviendo Problema 4: Derivación Implícita Trascendental ---")
    print("Modelo original: e^y + x * y = 4")
    print("Fórmula analítica (dy/dx): -y / (e^y + x)")
    
    try:
        # Se solicitan los valores de ambas variables requeridas en el resultado
        entrada_x = input("Ingrese el valor de x: ")
        x = float(entrada_x)
        
        entrada_y = input("Ingrese el valor de y: ")
        y = float(entrada_y)
        
        # Validación matemática para evitar una división entre cero
        denominador = math.exp(y) + x
        if denominador == 0:
            print("\n[!] Error matemático: La combinación de valores genera una división entre cero.")
            return

        # Cálculo de la derivada evaluada en los puntos ingresados
        resultado = -y / denominador
        print(f"\n=> El valor numérico de la derivada dy/dx cuando x = {x} y y = {y} es: {resultado:.4f}")
        
        print("*" * 20)
    except ValueError:
        print("\n[!] Error: Por favor ingrese un número decimal o entero válido.")

    print("-------------------------------------------------------------")

# Llamada de prueba a la función
derivada_implicita_trascendental()
