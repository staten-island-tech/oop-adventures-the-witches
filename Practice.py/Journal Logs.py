def RussianRoulette() :
    import random
    REVOLVER = [1,2,3,4,5,6]
    AmountOfBullets = random.sample(REVOLVER, k=3)
    A= input("There are 3 bullets in the revolver(6 spaces).")
    B =input("Each round, You will decide how many spins you would like to add.")
    C =input("The other participants amounts of spins are randomly selected.")
    D =input("There Are 3 rounds.")
    E =input("You have 2 lives")
    F = input("Good Luck")
    
RussianRoulette()