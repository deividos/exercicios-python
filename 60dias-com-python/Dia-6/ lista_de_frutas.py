frutas = ["pera", "uva", "maca"]

for fruta in frutas:
    print (fruta)


frutas = []
while True:
    fruta = input("Digite uma fruta: ")
    if fruta == "sair" or fruta == "Sair":
        break
    frutas.append(fruta)
    
print(frutas)