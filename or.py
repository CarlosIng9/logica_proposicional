# Función genérica para calcular la tabla de verdad de una compuerta lógica con 2 entradas
def calcular_tabla_verdad_or():
    variables = [0, 1]
    encabezado = "A | B | A OR B"
    print(encabezado)
    print("-" * len(encabezado))
    
    for A in variables:
        for B in variables:
            resultado = A or B
            print(f"{A} | {B} |   {resultado}")

# Llamada para generar la tabla de verdad para la compuerta OR
calcular_tabla_verdad_or()
