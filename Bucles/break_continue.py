def run():
    # for contador in range(1000):
    #     if contador % 2 != 0:
    #         continue #Hace que se salte lo que está despues de esta linea dentro de la iteración
    #     print(contador)

    # for i in range (10000):
    #     print(i)
    #     if i == 5678:
    #         break

    texto = input('Escribe un texto: ')
    for caracter in texto:
        if caracter == 'o':
            break
        print(caracter)

if __name__ == "__main__":
    run()