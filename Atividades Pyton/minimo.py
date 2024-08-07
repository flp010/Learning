valor_minimo = int(input())
valores = []
while True:
    try:
        valor = int(input())
        valores.append(valor)
    except ValueError:
        break
total = sum(valores)
sobra = 0
if total >= valor_minimo:
    print("minimo", valor_minimo)
    print("total", total)
    sobra = total - valor_minimo
    print("sobra", sobra)
else:
    print("valor minimo nao atingido")