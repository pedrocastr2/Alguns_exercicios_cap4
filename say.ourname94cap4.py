#pede o nome do usuario
nome = input("seu nome é :  ")

#Laço while , continuara exibindo o nome até perdirmos que pare ,ao não escrever outro nome.

while nome != "" :
    
    #exibe o nome do usuário 20 veses ou mais se o código for alterado.
    
    for x in range(10):
        
        #Exibe o nome do usuário seguido de um espaço e não de uma quebra de linha.
        print(nome, end =" ") # Após a execução do laço,pula para  a próxima linha.  
        
    print()
        
#Pede outro nome ou termina o programa
    nome = input("Escolha outro nome ou aperter [ENTER] caso queira acabar o programa ")
print("Obrigado por jogar")