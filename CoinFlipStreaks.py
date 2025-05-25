print("name:aditya.M,USN:1AY24AI004,sec:'M")
import random
streaks= 0 # to count how many times we get a streak of 6
for test in range(10000): # do this 10000 times
    flips=[] #list to store the coin flips
     # flip a coin 100 times
    for i in range(100):
        flips.append(random.choice(['H','T'])) # H= Heads, T = Tails
        
    count=1
    found_streak= False
    for i in range(1,100):
            if flips[i] == flips[i - 1]:
                count += 1
                if count == 10:
                    found_streak = True
                    break
            else:
                    count=1
    if found_streak:
                    streaks += 1
print("streaks found:",streaks)
print("chance of streak:",(streaks/10000)*100,"%")