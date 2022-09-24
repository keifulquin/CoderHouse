#CONSIGNA:

#Realiza una función llamada relacion() que a partir de dos números cumpla lo siguiente:

#1 - Si el primer número es mayor que el segundo, debe devolver 1.

#2 - Si el primer número es menor que el segundo, debe devolver -1.

#3 - Si ambos números son iguales, debe devolver un 0.

#Comprueba la relación entre los números: '5 y 10', '10 y 5' y '5 y 5'

def relacion(num1, num2):
    if num1>num2:
        print("La relación es 1")
    elif num1<num2:
        print("La relación es -1")
    elif num1 == num2:
        print("La relación es 0")

relacion(int(input("Ingrese un número: ")), int(input("Ingrese otro número: ")))

#relacion(5, 10)
#relacion(10, 5)
#relacion(5,5)

