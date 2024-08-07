professora = input()
crianca = []

soletrar = input()
while soletrar != '.':
  crianca.append(soletrar)
  soletrar = input()

igual = "8-|"
while igual != "8-)":
  if len(professora) != len(crianca):
    igual = "8-|"
  else:
    for i in range(len(professora)): 
      if professora[i] == crianca[i]:
        igual = "8-)"
      break

print(igual)