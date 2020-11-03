def primera_letra(lista_de_palabras):
    primeras_letras = []

    for palabra in lista_de_palabras:
        try:
            assert type(palabra) == str, f'{palabra} no es string'
            assert len(palabra) > 0, f'No se permiten strings vacios'
            primeras_letras.append(palabra[0])
        except AssertionError as e:
            print(e)

    return primeras_letras

lista = ['Angelo', 5.5, 2, '', '1235124', 0.35]
print('Primeras letras validas son: ', primera_letra(lista))