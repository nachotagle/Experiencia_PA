import random


def adivinar_par_o_impar():
    inpu = input()
    a = random.randint(1,100)
    """
    Esta función representa el juego de adivinar si un número es par o impar.
    Tienes que permitir que el usuario ingrese una de las dos opciones y
    generar un número aleatorio para ver si es par o impar.
    Se debe mostrar si el usuario adivina correctamente o no.
    """
    respuesta = str()
    if a%2 == 0:
        respuesta = "par"
    else:
        respuesta = "impar"
   
    if respuesta == inpu:
        print("Correcto, el numero era: ",a)
    else:
        print("Incorrecto",a)


    pass