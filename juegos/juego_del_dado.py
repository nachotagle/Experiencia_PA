import random
def juego_del_dado():
    usuario = 0
    comp = 0
    gano = False
    print('COMENZO!')
    print('Ambos iniciaran con cero')
    while not gano:
        print('\nPresione enter para lanzar el dado')
        x = input()
        num = random.randint(1,7)
        usuario += num
        print('Te salio un', num)
        num = random.randint(1,7)
        comp += num
        print('Al computador un', num)
        print('TÚ:', usuario)
        print('COMPUTADOR:', comp)
        if comp >= 30 or usuario >= 30:
            gano = True

    if comp > usuario:
        print('\nTe gano el computador!')
    elif usuario > comp:
        print('\nGanaste MAQUNIA!!')
    else:
        print('\nEMPATARON')
    
    pass