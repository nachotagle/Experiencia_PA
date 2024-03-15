import random
def cachipun():
    a = random.randint(1,3)
    inpu = input('\nTira algo: ')
    if a == 1:
        resulta = 'Papel'
    elif a == 2:
        resulta = 'Piedra'
    elif a == 3:
        resulta = 'Tijera'
    
    print('\n' + resulta, 'vs', inpu)
    gano = False
    empate = False
    if resulta == inpu:
        empate = True
        print('\nEMPATE!')
    elif resulta == 'Tijera' and inpu == 'Piedra' or resulta == 'Papel' and inpu == 'Tijera' or resulta == 'Piedra' and inpu == 'Papel':
        gano = True
    
    if gano:
        print('\nGANASTE!!')
    elif not gano and not empate:
        print('\nPERDISTE!')
    
    """
    Esta función representa el juego de cachipun.
    Debes pedir al usuario que elija piedra, papel o tijera, y luego comparar su elección con la de la computadora.
    La computadora debe elegir una opción al azar.
    """
    pass
