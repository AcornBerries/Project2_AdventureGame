import random
encouraging_message = ("Don't be scared, you can do it!", "If you don't try, you can't win!", "What's the worst that can happen? Face your fears!")
random_int_for_e_m = random.randint(1,3) - 1
in_basement = True

print("Welcome to the Choose Your Own Adventure Game!")
print("And so the story begins...")
print("You have just woken up in a hallway with no memory.  There are three doors and a rug on the floor")
print("You decided to either look for a clue under the rug or in your pockets")
look = input("Where would you like to look? (rug or pockets)").lower()
if "pockets" in look:
  rug =  input("Your pockets are empty.  Do you want to look under the rug? (y/n)")
  while rug != ("y"):
    print(encouraging_message[random_int_for_e_m])
    rug = input("Please try again: ").lower()
print("You have found a key.")
while in_basement:
  print("There are three doors you could open.")
  which_door = input("Which one do you choose?  The yellow, the red, or blue door? (enter the color)").lower()
  if "yellow" in which_door:
    print("You are in the laboratory")
    print("You see a lab bench, test tubes, lab clothes, and a fire extinguisher. ")
    check_yellow = input("Which would you like to check? (enter the item name)").lower()
    while "bench" not in check_yellow:
      check_yellow = input("Sorry, no clue here.  Try again: ").lower()
    print("You have found Carbon, Iodide, Dubnium, Einsteinium, and Rubidium.  This is your clue.")
    stay_go_back_y = input("Would you like to go back to the hallway? (y/n)").lower()
    while "y" not in stay_go_back_y:
      print(encouraging_message[random_int_for_e_m])
      stay_go_back_y = input("Would you like to go back to the hallway? ").lower()
  elif "red" in which_door:
    print("You are in the cellar")
    check_red = input("There are cans, bottles, wine, and brewing equipment in the cellar. Which would you like to check? ").lower()
    while not(("brew" in check_red) or ("equipment" in check_red)):
      check_red = input("Sorry, no clue here.  Try again: ").lower()
    print("You have found Arugula, Purple Onions, Potatoes, Leeks, and Eggplants.  This is your clue.")
    stay_go_back_r = input("Would you like to stay or go back to the hallway? ").lower()
    while "stay" in stay_go_back_r:
      print(encouraging_message[random_int_for_e_m])
      stay_go_back_r = input("Would you like to stay or go back to the hallway? ").lower()
  elif "blue" in which_door:
    print("You are in the music room")
    print("As you stand in the music room, you see music stands, rosin, a tuba case, sheet music, and you also hear creepy music playing behind a curtain.")
    print("SLAM! Oh no...the door just slammed shut behind you.")
    check_blue = input("Which item, or where in the room, would you like to check? ").lower()
    while not(("curtain" in check_blue) or ("creepy" in check_blue) or ("behind" in check_blue)):
      check_blue = input("Sorry, no clue here.  Try again: ").lower()
    print("You have found a Lute, an English horn, an Accordian, a Violin, and a Euphonium playing by themselves.  This is your clue.")
    stay_go_back_b = input("Would you like to go back to the hallway? (y/n)").lower()
    while "y" not in stay_go_back_b:
      print(encouraging_message[random_int_for_e_m])
      stay_go_back_b = input("Would you like go back to the hallway? (y/n)").lower()
    print("Oh no.  You just realize the door has slammed shut and now you are locked in.")
    print("Thankfully, you see a letter keypad on the door.")
    passcode = input("What password would you like to try? ").lower()
    while passcode != "leave":
      passcode = input("I'm sorry, that is incorrect.  Please re-evaluate your clue and try again.").lower()
    print("The door has opened and you may escape to the hallway.")
    go_back = input("Would you like to go back to the hallway? (y/n)").lower()
    while "y" not in go_back:
      print(encouraging_message[random_int_for_e_m])
      go_back = input("Would you like go back to the hallway? (y/n)").lower()
  print("You are back in the hallway, facing a letter keypad.")
  password_or_another_room = input("Do you want to guess the password or enter another room? ").lower()
  if "password" in password_or_another_room:
    currently_attempting_password = True
    while currently_attempting_password:
      password_attempt = input("Enter your attempt at the hallway password: ").lower()
      if "apple cider" in password_attempt:
        currently_attempting_password = False
        print("You have beat the basement!")
        print("A door creeeeeeaks open in the wall, with a gaping pitch-black staircase looming behind it.")
        print("A gust of icy wind FORCES you upppppppppppppp the staircase...")
        in_basement = False
      else:
        if "y" not in input("Would you like to try at the password again? (y/n)").lower():
          currently_attempting_password = False