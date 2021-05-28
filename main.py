import random
import time

encouraging_message = ("Don't be scared, you can do it!", "If you don't try, you can't win!", "What's the worst that can happen? Face your fears!")
random_int_for_e_m = random.randint(1,3) - 1
in_basement = True

#not yet implemented within the code.
basement_visiting_record = {"yellow": False, "red": False, "blue": False}

#helper functions
def back_to_the_hallway():
  stay_go_back = input("Would you like to go back to the hallway? (y/n)").lower()
  while "y" not in stay_go_back:
    print(encouraging_message[random_int_for_e_m])
    stay_go_back = input("Would you like to go back to the hallway? ").lower()

#not yet implemented
def accidental_location_revisit_check(record_dict, selection):
  if record_dict[selection]:
    if "n" in input("You have been there before. Are you sure you would like to go back to that creepy place again? (y/n)").lower():
      return True
    else:
      return False

#introduction
print("Welcome to the Choose Your Own Adventure Game!")
print("And so the story begins...")
print("You have just woken up in a hallway with no memory.  There are three doors and a rug on the floor")
#finding the key to open the three rooms
print("You decided to either look for a clue under the rug or in your pockets")
look = input("Where would you like to look? (rug or pockets)").lower()
if "pockets" in look:
  rug =  input("Your pockets are empty.  Do you want to look under the rug? (y/n)")
  while rug != ("y"):
    print(encouraging_message[random_int_for_e_m])
    rug = input("Please try again: ").lower()
print("You have found a key.")
#three-room and hallway keypad gameplay loop
while in_basement:
  print("There are three doors you could open.")
  which_door = input("Which one do you choose?  The yellow, the red, or blue door? (enter the color)").lower()
  #yellow room process
  if "yellow" in which_door:
    print("You are in the laboratory")
    print("You see a lab bench, test tubes, lab clothes, and a fire extinguisher. ")
    #checking the items, and retrieving the clue
    check_yellow = input("Which would you like to check? (enter the item name)").lower()
    while "bench" not in check_yellow:
      check_yellow = input("Sorry, no clue here.  Try again: ").lower()
    print("You have found Carbon, Iodide, Dubnium, Einsteinium, and Rubidium.  This is your clue.")

    back_to_the_hallway()
  #red/cellar room process
  elif "red" in which_door:
    print("You are in the cellar")
    check_red = input("There are cans, bottles, wine, and brewing equipment in the cellar. Which would you like to check? ").lower()
    while not(("brew" in check_red) or ("equipment" in check_red)):
      check_red = input("Sorry, no clue here.  Try again: ").lower()
    print("You have found Arugula, Purple Onions, Potatoes, Leeks, and Eggplants.  This is your clue.")

    back_to_the_hallway()
  #blue/music room process
  elif "blue" in which_door:
    print("You are in the music room")
    print("As you stand in the music room, you see music stands, rosin, a tuba case, sheet music, and you also hear creepy music playing behind a curtain.")
    time.sleep(3)
    print("SLAM! Oh no...the door just slammed shut behind you.")
    #The blue door slams shut behind the person as they stand in the music room.
    check_blue = input("Which item, or where in the room, would you like to check? ").lower()
    while not(("curtain" in check_blue) or ("creepy" in check_blue) or ("behind" in check_blue)):
      check_blue = input("Sorry, no clue here.  Try again: ").lower()
    print("You have found a Lute, an English horn, an Accordian, a Violin, and a Euphonium playing by themselves.  This is your clue.")

    back_to_the_hallway()#this is slightly confusing, since we give the process for them to go back, so they think they did go back, and then we say the door is shut, so then they are disoriented. That happened to me.
    print("Oh no.  You just realize the door is slammed shut and now you are locked in.")
    print("Thankfully, you see a letter keypad on the door.")
    passcode = input("What password would you like to try? ").lower()
    while passcode != "leave":
      passcode = input("I'm sorry, that is incorrect.  Please re-evaluate your clue and try again.").lower()
    print("The door has opened and you may escape to the hallway.")

    back_to_the_hallway()

  #attempting the password in the hallway
  print("You are back in the hallway, facing a letter keypad.")
  password_or_another_room = input("Do you want to guess the password or enter another room? ").lower()
  if "password" in password_or_another_room:
    currently_attempting_password = True#the while loop allows for immediate reattempting of the password
    while currently_attempting_password:
      password_attempt = input("Enter your attempt at the hallway password: ").lower()
      if "apple cider" in password_attempt:
        currently_attempting_password = False
        print("You have beat the basement!")
        print("A door creeeeeeaks open in the wall, with a gaping pitch-black staircase looming behind it.")
        print("A gust of icy wind FORCES you upppppppppppppp the staircase...")
        in_basement = False
      else:#gives them a chance at reattempting the password immediately
        if "y" not in input("Would you like to try at the password again? (y/n)").lower():
          currently_attempting_password = False