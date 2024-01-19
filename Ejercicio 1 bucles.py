n = int(input("Numero entero:"))
def fibonacci(n):
    """función que reciba un número entero positivo n y calcule 
    el número de fibonacci asociado a ese número bucles.

    Parámetros:
        -Fichero: Un fichero con formato CSV

    Salida:
        El número de fibonacci asociado a un número solicitado. """
    a = 0
    b = 1
    if n == 0:
        return(a)
    elif n == 1:
        return(b)
    elif n != 0 and n != 1:
        for i in range(n-1):
            c = a + b
            a = b
            b = c
        return(c)

import datetime
start_time = datetime.datetime.now()
print(fibonacci(n))
end_time = datetime.datetime.now()
print("El tiempo de ejecución es:", end_time - start_time)