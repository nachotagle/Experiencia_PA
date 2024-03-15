import random
def adivinar_numero():
    salida = True
    x = random.randint(1,10)
    respuesta = int(input("ingresa un numero entre 1 y 10"))
    while salida == True:
        if respuesta == x:
            salida = False
            print("ganaste")
        else:
            salida = True
            respuesta = int(input("Incorrecto, intenta denuevo"))
    
    """
    Esta función representa el juego de adivinar un número.
    Debes generar un número al azar entre 1 y 10, y luego pedir al usuario que adivine el número.
    Se debe mostrar un mensaje si el usuario adivina correctamente o no.
    """
    pass