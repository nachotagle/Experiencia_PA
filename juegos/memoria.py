import random
def memoria():
    sec = []
    for x in range(6):
        sec.append(random.randint(1,11))
        
    print(sec)
    usuario = str(input('Reescribe denuevo los 6 digitos: '))
    if usuario == sec:
        print('\nLe achuntaste!!')
    else:
        print('\nDiablos, no le achuntaste')
    
        
    """
    Esta función representa el juego de memoria.
    Debes generar una secuencia de números al azar y mostrarla al usuario.
    Luego, debes pedir al usuario que repita la secuencia.
    Se debe mostrar un mensaje si el usuario acierta o no.
    """
    pass