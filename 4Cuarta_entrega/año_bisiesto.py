#Consigna: Realizar una función llamada año_bisiesto:

#Recibirá un año por parámetro. Imprimirá “El año año es bisiesto” si el año es bisiesto.

#Imprimirá “El año año no es bisiesto” si el año no es bisiesto.

#Si se ingresa algo que no sea número debe indicar que se ingrese un número.

#Información a tener en cuenta:

#Se recuerda que los años bisiestos son múltiplos de 4, pero los múltiplos de 100 no lo son, aunque los múltiplos de 400 sí. Estos son algunos ejemplos de posibles respuestas: 2012 es bisiesto, 2010 no es bisiesto, 2000 es bisiesto, 1900 no es bisiesto.




def año_bisiesto(año):
    print(f"El año es: {año}")
    if (type(año) == int):
        if año % 4 == 0:
            print("El año es bisiesto")
        else: 
            print("El año no es bisiesto")
    else:
        print("Ingrese un número")
        
      



print("*" * 90)
#año_bisiesto(int(input("Indique un año: ")))
año_bisiesto("sjdkajdk")
print("*" * 90)
año_bisiesto(2015)
print("*" * 90)
año_bisiesto(2010)
print("*" * 90)
