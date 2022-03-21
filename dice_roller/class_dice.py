from time import sleep
from random import randint
from os import system

class Dice:
    def __init__(self) -> None:
        pass

    dice01 = randint(1, 6)
    dice02 = randint(1, 6)

    def generate_dices(self):
        self.dice01 = randint(1, 6)
        self.dice02 = randint(1, 6)
        return [self.dice01, self.dice02]
        #Returns the random dice values

def ask_to_roll():
    _test = True
    while _test:
        _test = False
        answer = input("Do you wanna roll the dice? [Y/N]  ").strip().lower()
        system("clear")
        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print("Unexpected value. Try again")
            _test = True
    #Runs until returns true or false depending if it has to roll the dices or not

if __name__ == "__main__":
    
    while True:
        if ask_to_roll():
            dice = Dice()
            print(dice.generate_dices())
        else:
            print("Process finished")
            break
        
        