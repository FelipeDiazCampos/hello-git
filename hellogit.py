#Cuenta palabras
#pro

while True:
    palabra = input("Ingresa una palabra (o presiona 'q' para salir): ")
    
    if palabra == 'q':
        break
    
    cantidad_letras = len(palabra.replace(" ", ""))
    print(f"La palabra '{palabra}' tiene {cantidad_letras} letras.")
