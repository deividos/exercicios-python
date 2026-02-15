print ("Bem vindo a ilha do Tesouro! \n A aventura vai começar!")
print(''' 

     __ |             
     __\|,-           
     ,-`=--.         
      /=8\            
       =              
       =              
       =
       =
~..:::::::::::::..~~
~~~~~~~~~~~~~~~~~~~~


''')

passo1 = input(" Você tem dois caminhos esquerda ou direita, por qual você vai? ( digite esquerda ou direita) ").lower()
if passo1 == "esquerda":
    passo2 = input("Agora você precisa nadar ou andar, só tem uma opção correta: (digite nadar ou andar): ").lower()
    if passo2 == "andar":
        passo3 = input("Agora seu último desafio, escolha uma das 3 portas \n vermelha, amarela ou azul: (digite vermelha ou amarela ou azul) ").lower()
        #while passo3 != "amarela" or "vermelha" or "azul":   #poderia usar while
           # passo3 = input("Digite uma porta válida vermelha ou amarela ou azul: ")
        if passo3 == "amarela":
            print("Parabéns você venceu!")
        else:
            print("Game Over!")
    else:
        print("Game Over")

else:
    print("Game Over")           

        

    