pesos = input("¿Cuántos pesos mexicanos tienes?: ")
pesos = float(pesos)
valor_dolar = 21.75
dolares = pesos / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print("Tienes $" + dolares + " dólares")

dolares = input("¿Cuantos dolares tienes?: ")
dolares = float(dolares)
valor_peso = 0.046
pesos = dolares / valor_peso
pesos = round(pesos, 2)
pesos = str(pesos)
print("Tienes $" + pesos + " pesos mexicanos")