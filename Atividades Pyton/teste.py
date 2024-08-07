saldo = float(input())
item = float(input())
compras = 0
troco = saldo
while troco >= item:
    compras += 1
    troco -= item
    item = float(input())
print('Número de itens', compras)
print('Saldo:', "%.2f" % (troco))
