import random
import time
import math

encouraging_message = ("Don't be scared, you can do it!", "If you don't try, you can't win!", "What's the worst that can happen? Face your fears!")
random_int_for_e_m = random.randint(1,3) - 1
in_basement = True

#comment
#not yet implemented within the code.
basement_visiting_record = {"yellow": False, "red": False, "blue": False}

#helper functions for the ground floor
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

"""
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
        if "y" not in input("That is incorrect.  Would you like to try at the password again? (y/n)").lower():
          currently_attempting_password = False
"""


# Living room: Tv and couch
# Dining Room: Stack of Chairs and table
# Bathroom: Sink and Toilet
# Kitchen: Stove and Sink
locations = (("living room", ("tv", 5,8), ("couch",5,11)), ("dining room", ("stack of chairs", 22,1), ("table", 17,3)), ("bathroom", ("bathroom sink", 3,1), ("toilet", 1,1)), ("kitchen", ("stove", 15,11), ("kitchen sink", 23,10)))

ladder_loc = (random.randint(0, 3), random.randint(1, 2))#first int is the room index, second int is the object index

current_loc = [0, 1]#the first int is the index of the room, and the second is the index of the object.

#helper functions for the main floor
def hotcold_get_new_room():
  current_loc[0] = int(input("Out of the living room (1), the dining room (2), the bathroom (3), and the kitchen (4), where would you like to go? ")) - 1

def hotcold_get_new_obj():
  print("In this room, there is a:")
  object_counter = 1
  for item in locations[current_loc[0]][1:]:
    print("{} ({})".format(item[0], object_counter))#outputs item (1) etc. depending on the item and the number of the item
    object_counter += 1
  
  current_loc[1] = int(input("Out of the above objects, which would you like to check? (enter the number)"))

def current_distance_to_ladder():
  x_diff = locations[ladder_loc[0]][ladder_loc[1]][1] - locations[current_loc[0]][current_loc[1]][1]
  y_diff = locations[ladder_loc[0]][ladder_loc[1]][2] - locations[current_loc[0]][current_loc[1]][2]
  return math.sqrt(x_diff^2 + y_diff^2)

#MAIN FLOOR CODE
print("Congratulations!  You have made it to the main floor!")
print("You are now faced with an open-concept house layout.")

while True:
  hotcold_get_new_room()

  #the distance is between the ladder and the object
  distance_old = current_distance_to_ladder()
  hotcold_get_new_obj()
  distance_new = current_distance_to_ladder()#not distance new, distance current

#is the current object the ladder location?
  if tuple(current_loc) == ladder_loc:
    break
  elif distance_new <= 2:
    print("Hot")
  elif distance_new > 20:
    print("Cold")
  elif distance_new < distance_old:
    print("Warmer")
  elif distance_new > distance_old:
    print("Colder")
  
  while True:
    y_n_check = str(input("Would you like to check another object in this room: ")
    if "yes" in y_n_check:
      hotcold_get_new_obj()
      break
    else:
      y_n_other_room = str(input("Would you like to check another object in another room: "))
      if "yes" in y_n_check:
        distance_old = current_distance_to_ladder()
        hotcold_get_new_room()
        hotcold_get_new_obj()
        distance_new = current_distance_to_ladder()
        break
      else:
        print(encouraging_message)
  
  


    

#The ladder location is at a specific thing in the main floor (bathroom sink, chairs, etc.)
print("CREAK. Whoosh. A trapdoor opens above you, and a ladder falls down, missing you by a hair.")

