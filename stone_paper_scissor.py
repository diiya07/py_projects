import random

possibilities = ['stone', 'paper', 'scissor']

def play(possibilities):
    while True:
        user = input('your choice is: ').lower()

        if user == "exit":
            print('---GAME ENDED---')
            break

        if user not in possibilities:
            print('enter correct choice')
            continue

        computer = random.choice(possibilities)
        print(f'computer choose {computer}')

        if user == computer:
            print("it's a tie 🫥")

        elif (user == 'stone' and computer == 'scissor') or \
            (user == 'scissor' and computer == 'paper') or \
            (user == 'paper' and computer == 'stone'):
            print('you won! 🏆')

        else:
            print('computer wins! 🙁')
    
#function call
play(possibilities)

#1st try--

# def play(possibilities):

#     while True:
#         user = input('your choice is: ')
#         computer = random.choice(possibilities)
#         print(f'computer choose {computer}')
    
#         if user == computer:
#             print("it's a tie 🫥")
        
#         elif user == 'stone' and computer == 'paper':
#             print('computer wins! 🙁')
        
#         elif user == 'stone' and computer == 'scissor':
#             print('you won! 🏆')

#         elif user == 'paper' and computer == 'stone':
#             print('you won! 🏆')

#         elif user == 'paper' and computer == 'scissor':
#             print('computer wins! 🙁')   
        
#         elif user == 'scissor' and computer == 'paper':
#             print('you won! 🏆')

#         elif user == 'scissor' and computer == 'stone':
#             print('computer wins! 🙁') 

#         else:
#             print('enter correct input')    