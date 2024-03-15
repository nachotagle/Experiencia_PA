import random
def memoria():
    sec = []
    for x in range(6):
        sec.append(random.randint(1,11))
        
    print(sec)
    print('Reescribe denuevo los 6 digitos: ')
    pifia = False
    mal = 0
    p = 1
    for x in sec:
        c = int(input(str(p) + ': '))
        p += 1
        if c == x:
            print('BIEN')
        else:
            print('MAL')
            pifia = True
            mal += 1
        
    
    if not pifia:
        print('\nLe achuntaste a TODOS!!')
    else:
        print('\nDiablos, pifiaste en', str(mal))
    
        
    """
    Esta función representa el juego de memoria.
    Debes generar una secuencia de números al azar y mostrarla al usuario.
    Luego, debes pedir al usuario que repita la secuencia.
    Se debe mostrar un mensaje si el usuario acierta o no.
    """
    pass