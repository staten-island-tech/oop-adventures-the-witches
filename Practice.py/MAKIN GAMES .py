


                

            

     


def BombDefusion() :
    WIRES = ["RED","GREEN","BLUE","YELLOW"]
    print("There are 4 wires. RED, YELLOW , GREEN, OR BLUE.")
    print("Objective: Cut the correct wire in order to stop the bomb.")
    print("Each round the correct wire regenerates. Meaning that this game is based off of pure luck.")
    chances = 3
    import random
    print("You Currently have", chances, "Chances. Goodluck.")

    while chances < 0 :
            for i in range() :
                YourWireCut = input("Which Color Wire Would You Like To Cut? RED, YELLOW, GREEN, OR BLUE?")
                Correct_Wire = random.choice(WIRES)
                if YourWireCut != "RED" or "YELLOW" or "GREEN" or "BLUE":
                    print("Something went wrong. Are you sure you typed that correctly? Im gonna have to take away a chance for that one buddy.")
                    print("You have", chances, "Chances left")
                if YourWireCut == Correct_Wire :
                    print("Well Done!", YourWireCut,"Was the correct choice")
                    break
                if YourWireCut != Correct_Wire :
                    print("Guess Again!", YourWireCut, "Is not correct.")
                    chances -=1
                    print("You have", chances, "Chances left. Goodluck.")
                if chances == 0 :
                    print("GAME OVER! You Ran out of tries.")
                    print("You have failed to defuse the bomb.")
BombDefusion()