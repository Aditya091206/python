print("name:aditya.M,USN:1AY24AI004,sec:'M")
import random

dice = ['brain', 'brain', 'brain', 'footsteps', 'footsteps', 'shot']


def roll():
    return random.choice(dice)

def zombie_dice_bot():
    brains = 0
    shots = 0
    while shots < 2:
        result = roll()
        print("Rolled:", result)
        if result == 'brain':
            brains += 1
        elif result == 'shot':
            shots += 1
        if shots >= 2:
            print("Too many shots! Stop rolling.")
            break
    print("Brains collected:", brains)

zombie_dice_bot()
