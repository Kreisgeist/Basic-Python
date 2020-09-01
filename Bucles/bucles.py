def run():
    potencia = 0
    contador = 0
    while potencia < 1000000:
        potencia = 2 ** contador
        if potencia < 1000000:
            print('2 elevado a la potencia ' + str(contador) + ' = ' + str(potencia))
        contador = contador + 1


if __name__ == '__main__':
    run()