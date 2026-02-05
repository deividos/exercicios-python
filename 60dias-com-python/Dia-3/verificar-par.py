num = int(input("Digite um numero inteiro: "))
if num % 2 == 0:
    print ("O número", num, "é par.")
else:
    print ("O número", num, "não é par.")
    
    
    
num1 = input("Digite um numero inteiro: ")

try: #tentar rodar
    num1 = int(num1)
    if num1 % 2 == 0:
        print ("O número", num1, "é par.")
    else:
        print ("O número", num1, "não é par.")
except ValueError:
    print ("Você não digitou um número inteiro.")