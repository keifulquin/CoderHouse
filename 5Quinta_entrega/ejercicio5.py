#CONSIGNA:

#Realizá una función llamada recortar() que reciba tres parámetros.

#El primero es el número a recortar, el segundo es el límite inferior y el tercero el límite superior.

#La función tendrá que cumplir lo siguiente:

#1 - Devolver el límite inferior si el número es menor que éste.

#2 - Devolver el límite superior si el número es mayor que éste.

#3 - Devolver el número sin cambios si no se supera ningún límite.

#Comprueba el resultado de recortar 15 entre los límites 0 y 10


def recortar(num, lim_inf, lim_sup):
    if num<lim_inf:
        print(lim_inf)
    elif num>lim_sup:
        print(lim_sup)
    else: 
        print(num)


recortar(15, 0, 10)