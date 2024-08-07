parada = None
contador = 0
while parada is None:
    parada = input()
while True:
    line = input()
    if line == parada:
        break
    contador += 1
print(contador)
