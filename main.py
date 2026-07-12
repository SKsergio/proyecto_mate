from components import ejericicio2, ejercicio3, ejercicio5

print("Programa de evaluacion numéricamente las fórmulas analíticas ")
print("Integrantes: ")
print("1. Walter Ernesto Bazque Melara")
print("--"*16)
print("2. Sergio Emerson Quintanilla Flores(2026010545)")
print("--"*16)

def opciones_menu():
    print("====Seleccione una opción====")
    print("1. Derivada Sucesiva (F. Trascendental):")
    print("2. Derivada Sucesiva (F. Ciclica)")
    print("3. Derivacion Implicita Basica")
    print("4. Derivacion Implicita Trascendental:")
    print("5. Aplicacion a la Ciencia de Datos (Optimizacion):")


def main():
    while True:
        opciones_menu()
        opcion = input("Ingrese el número de la opción deseada (o 'salir' para terminar): ")
        
        match opcion:
            case "1":
                print("Llamarías a problema2.evaluar_problema()")

            case '2':
                ejericicio2.derivada_ciclica()

            case '3':
                ejercicio3.derivada_implicita_basica()

            case '4':
                print("Llamarías a problema4.evaluar_problema()")

            case '5':
                ejercicio5.desarrollo()
                
                break 
            case _:
                print("\n[!] Error: Opción no válida. Ingrese un número del 1 al 5.")
    

if __name__ == "__main__":
    main()