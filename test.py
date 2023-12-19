from ICEDRAGON import Icedragon
dragon = Icedragon("Ice Dragon", 1000, "The dragon taunts you to fight. \nEngage in fight?")
def StartIceDragon():
    roadsChoice = input("You hear rumbling sounds from a nearby cave. It sounds like there's a creature inside. \nWould you like to investigate?")
    if roadsChoice == "Yes":
        print("You travel torwards the sound.")
    elif roadsChoice == "No":
        print("You continue travelling as if nothing happened before.")
        return
def meeting(): 
    if dragon == "Yes":
        print("Preparing to fight...")
    if dragon == "No":
        print("You quickly run away from the cave and continue your journey like before.")
        return
## def fight():
    ##ummmm yeah
def friendship():
    ally = ally.battleoutcome()
    print(ally.battleoutcome)
if Icedragon.health == 0:
    icedragonBATTLEresult = Icedragon.battleresult()
    print (icedragonBATTLEresult)
##  mcVICTORY = mc.victory(Icedragon.weapon) import later ahaha 
##  print (mcVICTORY) + add if mc lose