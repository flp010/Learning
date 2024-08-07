memoria = []
while True:
    entrada = input()
    if entrada == '0':
        break
    entrada = int(entrada)
    memoria.append(entrada)

maximoMemoria = 0
memoriaAtual = 0

for entrada in memoria:
    if entrada > 0:
        memoriaAtual += entrada
    elif entrada < 0:
        memoriaAtual -= abs(entrada)

    if memoriaAtual > maximoMemoria:
        maximoMemoria= memoriaAtual

print(maximoMemoria)