# Función para imprimir la tabla de verdad de la compuerta AND
def tabla_verdad_and():
    print("A | B | A AND B")
    print("---------------")
    for A in [0, 1]:
        for B in [0, 1]:
            resultado = A and B
            print(f"{A} | {B} |   {resultado}")

# Llamar a la función
tabla_verdad_and()
