# Función para calcular la tabla de verdad de la implicación (p → q)
def calcular_tabla_verdad_implicacion():
    variables = [0, 1]
    encabezado = "p | q | p → q"
    print(encabezado)
    print("-" * len(encabezado))
    
    for p in variables:
        for q in variables:
            # p → q es equivalente a (not p) or q
            resultado = (not p) or q
            print(f"{p} | {q} |   {int(resultado)}")  # Convertimos el booleano a entero (0 o 1)

# Llamada para generar la tabla de verdad para la implicación p → q
calcular_tabla_verdad_implicacion()
