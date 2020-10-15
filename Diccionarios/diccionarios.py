def run():
    mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }
    
    # print(mi_diccionario['llave1'])
    # print(mi_diccionario['llave2'])
    # print(mi_diccionario['llave3'])

    poblacion_paises = {
        'Argentina': 44_938_712,
        'Brasil': 210_147_125,
        'Colombia': 50_372_424
    }

    # print(poblacion_paises['Bolivia']) PARA ACCEDER CON LA LLAVE DEL ITEM DEL DICCIONARIO

    # for pais in poblacion_paises.keys(): PARA ACCEDER A LAS LLAVES
    #     print(pais)

    # for pais in poblacion_paises.values(): PARA ACCEDER AL VALOR DE LOS ITEMS
    #     print(pais)

    for pais, poblacion in poblacion_paises.items(): # SE PUEDE ACCEDER A AMBOS ELEMENTOS DE LOS ITEMS, INCLUSO POR SEPARADO
        print(pais + ' tiene ' + str(poblacion) + ' habitantes')

if __name__ == '__main__':
    run()