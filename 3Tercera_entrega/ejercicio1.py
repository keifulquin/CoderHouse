



primernum = int(input("Elija el primer número: "))
segundonum = int(input("Elija el segundo número: "))

print("________________________________________________________________________")

opcion1 = print("1- Mostrar una suma de los dos números.")
opcion2 = print("2- Mostrar una resta de los dos números (el primero menos el segundo)")
opcion3 = print("3- Mostrar una multiplicación de los dos números.")
opcion4 = print("4- Si elige esta opción se interrumpirá la impresión de menú y el programa finalizará.")
opcion5 = print("5- En caso de no introducir una opción válida, el programa informará de que no es correcta.")


suma = primernum + segundonum 
resta = primernum - segundonum
multiplicacion = primernum * segundonum

print("________________________________________________________________________")

opcion = input("Elija una opción: ")

print("________________________________________________________________________")

while opcion <= "4": 
    if opcion == "1":
        print ("El resultado es: ", suma)
        break 
    elif opcion == "2":
        print ("El resultado es: ", resta)
        break
    elif opcion == "3":
        print ("El resultado es: ", multiplicacion)
        break
    elif opcion == "4":
        print ("Finalizo el programa")
        break
else:
    print ("La opcion no es correcta")

print("________________________________________________________________________")