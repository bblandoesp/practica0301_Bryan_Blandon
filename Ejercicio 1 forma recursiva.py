numero = int(input("Numero entero:"))
def fiborec(numero_entero):
    if numero_entero == 0:
        return 0
    elif numero_entero == 1:
        return 1
    else:
        return fiborec(numero_entero-1) + fiborec(numero_entero-2)

import datetime
start_time = datetime.datetime.now() 
print(fiborec(numero))
end_time = datetime.datetime.now()
print("El tiempo de ejecución es:", end_time - start_time)