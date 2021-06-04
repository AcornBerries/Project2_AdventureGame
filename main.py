import random
import time
import math


def encouragingMessage():
  encouraging_message = ("Don't be scared, you can do it!", "If you don't try, you can't win!", "What's the worst that can happen? Face your fears!")
  random_int_for_e_m = random.randint(1,3) - 1
  print(encouraging_message[random_int_for_e_m])


#helper functions for the ground floor
def back_to_the_hallway():
  stay_go_back = input("Would you like to go back to the hallway? (y/n)").lower()
  while "y" not in stay_go_back:
    encouragingMessage()
    stay_go_back = input("Would you like to go back to the hallway? ").lower()

#not yet implemented
def accidental_location_revisit_check(record_dict, selection):
  if record_dict[selection]:
    if "n" in input("You have been there before. Are you sure you would like to go back to that creepy place again? (y/n)").lower():
      return True
    else:
      return False

in_basement = True

#not yet implemented within the code.
basement_visiting_record = {"yellow": False, "red": False, "blue": False}

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
    encouragingMessage
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
        time.sleep(1)
        print("A door creeeeeeaks open in the wall,")
        time.sleep(2)
        print("with a gaping pitch-black staircase looming behind it.")
        time.sleep(1)
        print("A gust of icy wind FORCES you upppppppppppppp the staircase...")
        time.sleep(2)
        in_basement = False
      else:#gives them a chance at reattempting the password immediately
        if "y" not in input("That is incorrect.  Would you like to try at the password again? (y/n)").lower():
          currently_attempting_password = False


# Living room: Tv and couch
# Dining Room: Stack of Chairs and table
# Bathroom: Sink and Toilet
# Kitchen: Stove and Sink
locations = (("LIVING ROOM", ("Tv", 5,8), ("Couch",5,11), ("Carpet", 9,2)), ("DINING ROOM", ("Stack of Chairs", 22,1), ("Table", 17,3), ("Sideboard", 22,5)), ("BATHROOM", ("Bathroom sink", 3,1), ("Toilet", 1,1), ("Cupboard", 4,1)), ("KITCHEN", ("Stove", 15,11), ("Kitchen sink", 23,10), ("Fridge", 19,11)))

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
  
  current_loc[1] = int(input("Out of the above objects, which would you like to check? (enter the number) "))

def get_room_obj_coord(room_obj_idxs):
  x_value = locations[room_obj_idxs[0]][room_obj_idxs[1]][1]
  y_value = locations[room_obj_idxs[0]][room_obj_idxs[1]][2]
  return (x_value, y_value)

def distance_coord_to_ladder(coord_pair):
  x_diff = ladder_coords[0] - coord_pair[0]
  y_diff = ladder_coords[1] - coord_pair[1]
  return math.sqrt(x_diff**2 + y_diff**2)

#setting ladder object location and retrieving coordinates
ladder_loc = (random.randint(0, 3), random.randint(1, 3))#first int is the room index, second int is the object index
ladder_coords = get_room_obj_coord(ladder_loc)

#MAIN FLOOR CODE
print("Congratulations!  You have made it to the main floor!")
print("You are now faced with an open-concept house layout.")

print("                                           Ground Floor Map")
print(" ")
print(" 12┌───────────────────────────────────────────────────────────────────────────────────────────────┐")
print("   │                                               |                                               │")
print(" 11│   .   .   .   .  (2)  .   .   .   .   .   .       .   .  (1)  .   .   .  (2)  .   .   .   .   │")
print("   │                 Couch                         |         Stove          Fridge                 │")
print(" 10│   .   .   .   .   .   .   .   .   .   .   .       .   .   .   .   .   .   .   .   .   .  (3)  │")
print("   │                                               |                                           Sink│")
print(" 9 │   .   .   .   .   .   .   .   .   .   .   .       .   .   .   .   .   .   .   .   .   .   .   │")
print("   │                                               |                    KITCHEN                    │")
print(" 8 │   .   .   .   .  (1)TV.   .   .   .   .   .       .   .   .   .   .   .   .   .   .   .   .   │")
print("   │                                               |                                               │")
print(" 7 │   .   .   .   .   .   .   .   .   .   .   .       .   .   .   .   .   .   .   .   .   .   .   │")
print("   │                 LIVING ROOM                   |                                               │")
print(" 6 │   .   .   .   .   .   .   .   .   .   .   .    _ _._ _._ _._ _._ _._ _._ _._ _._ _._ _._ _._ _│")
print("   │                                               |                                               │")
print(" 5 │   .   .   .   .   .   .   .   .   .   .   .       .   .   .   .   .   .   .   .   .  (3)  .   │")
print("   │                                               |            DINING ROOM           Sideboard    │")
print(" 4 │   .   .   .   .   .   .   .   .   .   .   .       .   .   .   .   .   .   .   .   .   .   .   │")
print("   │                                               |                                               │")
print(" 3 ├───────────────────┐   .   .   .   .   .   .       .   .   .   .  (2)  .   .   .   .   .   .   │")
print("   │     BATHROOM      │            Carpet         |                 Table                         │")
print(" 2 │   .   .   .   .   │   .   .   .  (3)  .   .       .   .   .   .   .   .   .   .   .   .   .   │")
print("   │              Cup- │                           |                                     Stack     │")
print(" 1 │  (1)  .  (2) (3)  │   .   .   .   .   .   .       .   .   .   .   .   .   .   .   .  (1)  .   │")
print("   │Toilet  Sink  board│                         START                                 of Chairs   │")
print(" 0 └───────────────────┴──────────────────────────(┼)──────────────────────────────────────────────┘")
print("       1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  22  23  24")

distance_old = distance_coord_to_ladder((12, 0,))#(12, 0) is the coordinate pair of the basement door (START)
hotcold_get_new_room()
hotcold_get_new_obj()
#this variable is the current distance (after moving to the current object)
distance_new = distance_coord_to_ladder(get_room_obj_coord(current_loc))

while True:
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
  else:
    print("You have not moved.")
  
  #TO MAKE PROGRAM PROCESS MORE CLEAR WHILE PROGRAMMING IS INCOMPLETE
  print("distance_new:", distance_new)
  print("distance_old:", distance_old)
  print("current_loc:", current_loc)

  while True:
    y_n_check = input("Would you like to check another object in this room (y/n): ")
    if "y" in y_n_check:
      distance_old = distance_coord_to_ladder(get_room_obj_coord(current_loc))
      hotcold_get_new_obj()
      distance_new = distance_coord_to_ladder(get_room_obj_coord(current_loc))
      break
    else:
      y_n_other_room = input("Would you like to go to another room then? (y/n): ")
      if "y" in y_n_other_room:
        distance_old = distance_coord_to_ladder(get_room_obj_coord(current_loc))
        hotcold_get_new_room()
        hotcold_get_new_obj()
        distance_new = distance_coord_to_ladder(get_room_obj_coord(current_loc))
        break
      else:
        encouragingMessage()


    

#The ladder location is at a specific thing in the main floor (bathroom sink, chairs, etc.)
print("CREAK. Whoosh. A trapdoor opens above you, and a ladder falls down, missing you by a hair.")
