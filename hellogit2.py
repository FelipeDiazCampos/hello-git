while True:
    palabra = input("Ingresa una palabra: ")
    cantidad_letras = len(palabra.replace(" ", ""))
    
    resultado = ', '.join([palabra] * cantidad_letras)
    
    print(resultado)
    
    continuar = input("¿Quieres ingresar otra palabra? (s/n): ")
    if continuar.lower() != 's':
        break