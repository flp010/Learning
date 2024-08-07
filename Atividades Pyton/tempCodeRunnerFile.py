especial = "!@#$%¨&*()_-+="
outro = "bcdfghjklmnpqrstvwxyz"
vogal = "aeiouAeIOU"
algarismo = "1234567890"

caracter = input()
if caracter in especial:
    print("especial")
elif caracter in outro:
    print("outro")
elif caracter in vogal:
    print("vogal")
else:
    print("algarismo")