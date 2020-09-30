import random

def run():
    numero_al = random.randint(1, 100)
    numero_us = int(input('¿En que número estoy pensando? (del 1 al 100): '))

    while numero_al != numero_us:
        if numero_al > numero_us:
            numero_us = int(input('Prueba con un número más grande: '))
        elif numero_al < numero_us:
            numero_us = int(input('Prueba con un número más pequeño: '))

    print('¡GANASTE!')


if __name__ == '__main__':
    run()