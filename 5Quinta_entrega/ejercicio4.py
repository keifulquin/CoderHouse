#CONSIGNA:

#Realiza una función llamada intermedio() que a partir de dos números, devuelva su punto intermedio:

#🖐 Ayuda: El número intermedio de dos números corresponde a la suma de los dos números dividida entre 2

#Comprueba el punto intermedio entre -12 y 24

def intermedio (num1, num2):
    suma= num1+num2
    print("El número intermedio es: ", suma//2)

intermedio(int(input("Elija el primer número: ")), int(input("Elija el segundo número: ")))

