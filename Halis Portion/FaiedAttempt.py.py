def RussianRoulette() :
    import random
    REVOLVER = [1,2,3,4,5,6]
    LOADEDBulletSlot = random.choice(REVOLVER)
    lives = 2
    A= input("There is 1 bullet in the revolver(6 spaces).")
    B =input("Each round, You will decide how many spins you would like to add.(0-2)")
    C =input("The other participants amounts of spins are randomly selected.")
    D =input("There Are 3 rounds.")
    E =input("Because I am Generous,You have 2 lives.")
    F = input("Good Luck.")
    PARTICIPANTSPIN1 = [0,1,2]
    PARTICIPANTSPIN2 = [0,1,2]
    PARTICIPANTSPIN3 = [0,1,2]
    PARTICIPANTSPIN4 = [0,1,2]
    PARTICIPANTS = ["Player1", "Player2", "Player3", "Player4","YOU"]
    while lives > 0 :
        for i in range(2):
            PlayerChoice1 =random.choice(PARTICIPANTSPIN1)
            PlayerChoice2 =random.choice(PARTICIPANTSPIN2)
            PlayerChoice3 =random.choice(PARTICIPANTSPIN3)
            PlayerChoice4 =random.choice(PARTICIPANTSPIN4)
            YourSPIN = int(input("How many spins would you like to add? 0, 1, or 2"))
            print("Player1 chose to add ", PlayerChoice1, "Spins.")
            print("Player 2 chose to add ", PlayerChoice2, "Spins.")
            print("Player 3 chose to add", PlayerChoice3, "Spins.")
            print("Player 4 chose to add ", PlayerChoice4, "Spins.")
            print("You chose to add",YourSPIN," Spins.")
            TotalSPINS = PlayerChoice1+PlayerChoice2+PlayerChoice3+PlayerChoice4+YourSPIN
            print("The revolver has spun",TotalSPINS, "Times.")
            Seats = random.shuffle(PARTICIPANTS)
            print("Everyone takes their seat in the following order:", random.shuffle(PARTICIPANTS))
            G = input(Seats(0),"picks up the gun.")
            if LOADEDBulletSlot == 1:
                print(Seats(0), "Was shot")
            elif LOADEDBulletSlot != 1:
                input("This slot was empty. The gun continues.")
                PARTICIPANTS.remove(Seats(0))
            elif LOADEDBulletSlot == 2:
                print(Seats(1),"Has been shot.")
                PARTICIPANTS.remove(Seats(1))
            elif LOADEDBulletSlot != 2:
                input("This slot was empty. The Gun continue to spin.")
            elif LOADEDBulletSlot == 3:
                print(Seats(2), "Has been shot.")
                PARTICIPANTS.remove(Seats(2))
            elif LOADEDBulletSlot!= 3:
                input("This slot was Empty. The gun continues..")
            elif LOADEDBulletSlot == 4 :
                print(Seats(3), "Has Been shot.")
                PARTICIPANTS.remove(Seats(3))
            elif LOADEDBulletSlot != 4:
                input("This slot was empty. Th gun continues...")
            elif LOADEDBulletSlot == 5 :
                print(Seats(4), "Has been shot.")
                PARTICIPANTS.remove(Seats(4))
            elif LOADEDBulletSlot != 5:
                input("This slot was Empty. The gun continues.")
            elif LOADEDBulletSlot == 6:
                print(Seats(5), "Was shot.")
                PARTICIPANTS.remove(Seats(5))
            elif LOADEDBulletSlot != 6:
                input("This slot was empty... The gun continues.")
            if PARTICIPANTS.remove("You") :
                print("GAME OVER.")
                break

            print(PARTICIPANTS, "Has won this round.")

            





                




    
RussianRoulette()