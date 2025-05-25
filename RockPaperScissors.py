import random
choices =['rock','paper','scissor']
user_choice=input("enter the user choice(Rock,Paper,Scissor):")
computer_choice=random.choice(choices)
print(computer_choice)

if user_choice == computer_choice:
    print("it's tie!")
elif(user_choice== 'rock' and computer_choice== 'scissor') or (user_choice== 'paper' and computer_choice== 'rock') or (user_choice== 'scissor' and computer_choice== 'paper'):
      print('you win')
elif(user_choice== 'scissor' and computer_choice== 'rock') or (user_choice== 'rock' and computer_choice== 'paper') or (user_choice== 'paper' and computer_choice== 'scissor'):
   print('computer wins!')
else:
     print('invalid input,please choice rock,paper,scissor')