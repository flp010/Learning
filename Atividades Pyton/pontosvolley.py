resp = str(input())
print (resp)
cont = 0
while resp != "timeout":
    if resp == "accepted":
        cont += 1
    resp = str(input())
    print (resp)
    
print(cont)