import random
escolha = int(input("Escolha(digite) 1 para 'cara' ou 2 para 'coroa': "))
cara_coroa = random.randint(1, 2)
if cara_coroa == escolha:
    print(f"O resultado foi {cara_coroa} você venceu!")
else:
    print(f"O resultado foi {cara_coroa} você perdeu")



