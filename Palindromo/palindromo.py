def palindromo(palabra):
    return True if palabra == palabra[::-1] else False


def run():
    palabra = input('Escribe una palabra: ').replace(' ', '').lower()
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es palindromo')
    else:
        print('No es palindromo')


if __name__ == '__main__':
    run()