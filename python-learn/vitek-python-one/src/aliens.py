aliens = 2
password = "ALIENS"
print("Quickly aliens are invading the planet.")
print("You need to activate the global defence platforms.")
print("Hope you know the password, for earth's sake.")
print()
print("---------------------------------------------------")
print("       WELCOME TO THE GLOBAL DEFENCE SYSTEM       ")
print("---------------------------------------------------")
guess = input("please enter the password").upper()
while guess != password:
    print("")
    print("INCORRECT PASSWORD")
    print("")
    aliens = aliens ** 2
    print("There are",aliens,"aliens now on earth. Try again")
    if aliens > 8200000000:
        break
    print("")
    print("Password hint: the things that are attacking us.")
    print("")
    guess = input("Quick! Please enter the password: ").upper()
if aliens > 8200000000:
    print("noooooo! The aliens have outnumbered us. All is lost")
else:
    print("Hooray we won the fight and the world is saved")
    print()
    print("static")
    print("we will be back. ")
    print("static static.")
    print("will not.")
    print("static ")
    print("rid of us so easily")
    print()
    print("---------------------------------------------------")
    print("                TRANSMISSION OVER                  ")
    print("---------------------------------------------------")














