import random

def array_diff(a, b):
    for elemento1 in a[:]:
        for elemento2 in b[:]:
            if elemento1 == elemento2:
                a.remove(elemento1)
    
    return a
            
        

def run():

    print(array_diff([19, 9, 0, 17, -8, 3, 2], [-10, -1, 6, 19, -15, -4, 17, -19]))

if __name__ == '__main__':
    run()