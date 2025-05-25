print("name:aditya.M,USN:1AY24AI004,sec:'M")
import random
number=random.randint(1,100)
guess=int(input("guess the number between 1 and 100:"))
if guess==number:
    print("you guessed it!!")
else:
    print(f"wrong! the number was {number}")