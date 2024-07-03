print("You are in a dark room in a mysterious castle.")
print("In front of you are five doors you must choose one.")
playerChoice = input("choose 1,2,3,4 or 5")
if playerChoice =="1":
    print("you find a room full of treasure. you're rich.")
    print ("GAME OVER,YOU WIN!")
elif playerChoice == "2":
    print("the door opens and a furious ogre hits you with his club.")
    print("GAME OVER YOU LOSE")
elif playerChoice == "3":
    print("you go into a room and find a dragon sleeping on a pile of treasure.")
    print("you can either:")
    print("1)try to steal the dragons treasure.")
    print("2) try to tame the dragon")
    dragonChoice = input("type 1 or 2...")
    if dragonChoice == "1":
        print("the dragon wakes up and eats you, you are delicious.")
        print("GAME OVER,YOU LOSE.")
    elif dragonChoice == "2":
        print("you tame the dragon and use it to fly out of the castle.")
        print("GAME OVER, YOU WIN")
    else:
        print("sorry you didn't enter 1 or 2")
elif playerChoice == "4":
    print("A knight takes out his sword and strikes you down easily.")
    print("GAME OVER, YOU LOSE")
elif playerChoice == "5":
    print("A killer bunny jumps at you and bites your head off.")
    print ("GAME OVER, YOU LOSE.")
