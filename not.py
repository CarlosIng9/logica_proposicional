# Función para calcular la tabla de verdad de la compuerta NOT
def calcular_tabla_verdad_not():
    variables = [0, 1]
    encabezado = "A | NOT A"
    print(encabezado)
    print("-" * len(encabezado))
    
    for A in variables:
        resultado = not A
        print(f"{A} |   {int(resultado)}")  # Se convierte el booleano a entero para mostrar 0 o 1

# Llamada para generar la tabla de verdad para la compuerta NOT
calcular_tabla_verdad_not()
