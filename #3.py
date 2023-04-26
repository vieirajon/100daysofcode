#CAÇA AO TESOURO

print(''' 
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_______/
*******************************************************************************
''')
print('Bem Vindo a Ilha do Tesouro.')
print('Sua missão é achar o tesouro.')
escolha1 = input('Você está numa encruzilhada, pra onde deseja ir? Digite "Esquerda" ou "Direita".').lower()

if escolha1 == "Esquerda":
    escolha2 = input('Você chegou em um lago. Tem um ilha no meio do lago. Digite "Esperar" para esperar o bote. Digite "Mergulhar" para atravessar o lago nadando.').lower()
    if escolha2 == "Esperar":  
       escolha3 = input('Você chegou na ilha ileso. Tem uma casa com 3 portas. Uma Vermelha, uma Amarela e uma Azul. Qual cor você escolhe? ').lower()
       if escolha3 == "Vermelha":
            print('É um quarto em chamas. Game Over.')
       elif escolha3 == "Amarela":
            print('Você achou o Tesouro! Você Ganhou!')
       elif escolha3 == "Azul":
            print('Você entrou em um quarto de monstros. Game Over.')
       else:
           print('Você escolheu uma porta que não existe. Game Over.')
    else:
        print('Você foi atacado por um jacaré. Game Over.')
else:
    print('Você caiu em um buraco. Game Over.')

