print ("Bem vindo ao App GorjetaConta")
valor_conta = float(input("Digite o valor da conta: "))
porcentagem_gorjeta = int(input("Digite a porcentagem que quer dar de gorjeta: 10, 12 ou 15: "))
quantidade_pessoas = int(input("Digite a quantidade de pessoas para pagar a conta: "))

valor_com_gorjeta = valor_conta + (porcentagem_gorjeta * valor_conta) / 100
valor_por_pessoa = valor_com_gorjeta / quantidade_pessoas

print (f"O valor com gorjeta é: {valor_com_gorjeta} e o valor por pessoa fica: {valor_por_pessoa}")
