# Función para calcular la tabla de verdad de la bicondicional (p ↔ q)
def calcular_tabla_verdad_bicondicional():
    variables = [0, 1]
    encabezado = "p | q | p ↔ q"
    print(encabezado)
    print("-" * len(encabezado))
    
    for p in variables:
        for q in variables:
            # p ↔ q es equivalente a (p and q) or (not p and not q)
            resultado = (p and q) or (not p and not q)
            print(f"{p} | {q} |   {int(resultado)}")  # Convertimos el booleano a entero (0 o 1)

# Llamada para generar la tabla de verdad para la bicondicional
calcular_tabla_verdad_bicondicional()
