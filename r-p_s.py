import random

ch=["rock","paper","scissors"]

comp=random.choice(ch)
hari=input("choose one: ")

if comp==hari:
    print("tie")
elif {
    hari=="rock",comp=="scissors" or
    hari=="paper",comp=="rock" or
    hari=="scissors",comp=="paper"
    }:
    print("you win")
else: print("computer won")
print(comp)