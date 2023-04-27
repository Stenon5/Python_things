import random

options = ('piedra', 'papel', 'tijeras')

user_wins_numb = 0
computer_wins_numb = 0
rounds_numb = 0




##                                 funciones de código

def contador(round= 0, user_win= 0, computer_win= 0,):
    global user_wins_numb, computer_wins_numb, rounds_numb
    
    
    if round == 1:
        rounds_numb += 1
    elif user_win == 1:
        user_wins_numb += 1
    elif computer_win == 1:
        computer_wins_numb += 1

        
 


#                                      reglas de juego
def piedra(computer_option):
    if computer_option == 'tijeras':
        print('user win')
        contador(user_win=1)
    if computer_option == 'papel':   #else podría reemplazar estas líneas
        print('computer win')
        contador(computer_win= 1)

def papel(computer_option):
    if computer_option == 'piedra':
       print('user win')
       contador(user_win= 1)
    if computer_option == 'tijeras':
       print('computer win')
       contador(computer_win= 1)

def tijera(computer_option):
    if computer_option == 'papel':
        print('user win')
        contador(user_win= 1)
    if computer_option == 'piedra':
        print('computer win')     
        contador(computer_win= 1) 
      
    

##                                     inicio



if __name__ == '__main__':
    pass





while True:
    print('')
    print('')


    print('*' * 10)
    print(f"ROUND: {rounds_numb}")
    print(f"your wins {user_wins_numb}")
    print(f"computer wins {computer_wins_numb}")
    print('*' * 10)

    

    
    user_option = input('piedra, papel o tijera => ')      #Empaquetación del input 
    user_option = user_option.lower()                          #Validacion del input
#                                                              # 
    if not user_option in options:                             #
        print('esa opcion no es valida')                       #    
        continue                                               #

    computer_option = random.choice(options)                #valor de la computadora
        
    contador(round= 1)                                      #llamado a reglas de juego
    if user_option == computer_option:       
        print('Empate!, intenta de nuevo')
    elif user_option == 'piedra':
        piedra(computer_option)
    elif user_option == 'papel':
        papel(computer_option)
    elif user_option == 'tijera':
        tijera(computer_option)
