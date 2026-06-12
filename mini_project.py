import random 
print("welcome to the number guessing game")
num=random.randint(0,100)
guess=None
while guess!=num:
    guess=int(input("guess the number between 0 and 100: "))
    if guess<num:
        print("higher ra howle")
    elif guess>num:
        print("lower ra bachee")
print("congratulations! you guessed the number correctly")

