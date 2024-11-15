import random


no=random.randint(1,10)
guess=int(input("enter the guess: "))
if guess==no:
    print("wow!")
else:
    print("failed")