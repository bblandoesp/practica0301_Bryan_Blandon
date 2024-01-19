import csv
import os
F1 = "50.csv"
F2 = "1000.csv"

def leerfichero(fichero):
        """Funcion que lee cualquier fichero en formato CVS.
        Parámetros:
                -Fichero: Un fichero en el directorio 
                con el formato CVS.
        Salida:
                -Lista con el contenido del fichero."""
        if os.path.isfile(fichero):
                with open(fichero, "r") as file:
                        Doc = csv.reader(file)
                        lista = list(Doc)
                return lista
        else:
               return("El fichero no Existe")
        
def formato_capitalizado (lista):
        """Funcion que le aplica el sistema capitalizado a un nombre.

        Parámetros:
                -Lista: La lista que contiene el nombre con el DNI 
        Salida:
                -El nombre en formato capitalizado."""
        for linea in lista:
            lineas = linea[0]
            mayusculas = lineas.title()
            return(mayusculas)
        
def CalcularDNI(lista):
        """Funcion que calcula la letra del DNI en base a una fórmula.
        
        Parámetros:
                -Lista: La lista que los números del DNI con el nombre. 
        Salida:
                -La letra que le corresponde al DNI."""
        for linea in lista:
            lineas = linea[1]
            letras = "TRWAGMYFPDXBNJZSQVHLCKE"
            calcular = int(lineas) % 23
            digito = letras[calcular]
            return(digito)
       
       
fichero = leerfichero("55.csv")
print(formato_capitalizado(fichero))
print(CalcularDNI(fichero))