def factorial(n):
    """Calcula el factorial de n.

    n int > 0
    returns n!

    """
    if n == 1:
        return 1
    
    return n * factorial(n-1)

def run():
    n = int(input('Escribe un entero: '))
    print(f'El factorial de {n} es: {factorial(n)}')

if __name__ == "__main__":
    run()

