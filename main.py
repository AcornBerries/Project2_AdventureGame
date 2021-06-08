"""
#Header. Story Outline?
"""

import random
import time
import math


def encouragingMessage():
    encouraging_message = (
        "Don't be scared, you can do it!", "If you don't try, you can't win!",
        "What's the worst that can happen? Face your fears!")
    random_int_for_e_m = random.randint(1, 3) - 1
    print(encouraging_message[random_int_for_e_m])

playing_hotcold = False
#s_int is a boolean parameter that is True when an integer input is desired, and False if a string is desired. By default, it is False.
def take_input(prompt_str, is_int=False):
    user_input = input("\n" + prompt_str)
    if playing_hotcold:
      while True:
        if "map" in user_input:
            print_map()
            user_input = input("\n" + prompt_str)
        else:
          break

    if is_int:
        casted_input = None
        while True:
            try:
                casted_input = int(user_input)
                break
            except ValueError:
                print("You did not enter a plain digit. Please try again.")
                user_input = input("\n" + prompt_str)
                continue

        print("\n")
        return casted_input
    else:
        print("\n")
        return user_input


#helper functions for the ground floor
def back_to_the_hallway():
    stay_go_back = take_input(
        "Would you like to go back to the hallway? (y/n)").lower()
    while "y" not in stay_go_back:
        encouragingMessage()
        stay_go_back = take_input(
            "Would you like to go back to the hallway? ").lower()



#not yet implemented
def accidental_location_revisit_check(record_dict, selection):
  if record_dict[selection]:
    if "n" in take_input("You have been there before. Are you sure you would like to go back to that creepy place again? (y/n)").lower():
      return True
    else:
      return False

#not yet implemented within the code.
basement_visiting_record = {"yellow": False, "red": False, "blue": False}


#introduction
print("Welcome to the Choose Your Own Adventure Game!")
print("And so the story begins...")
time.sleep(2)
print("You have just woken up in a hallway with no memory.")
time.sleep(3)
print("There are three doors and a rug on the floor.")
#finding the key to open the three rooms
print("You decided to either look for a clue under the rug or in your pockets")
look = take_input("Where would you like to look? (rug or pockets)").lower()
if "pockets" in look:
    rug = take_input(
        "Your pockets are empty.  Do you want to look under the rug? (y/n)")
    while rug != ("y"):
        encouragingMessage
        rug = take_input("Please try again: ").lower()
print("You have found a key.")

#three-room and hallway keypad gameplay loop
in_basement = True
while in_basement:
    print("There are three doors you could open.")
    which_door = take_input(
        "Which one do you choose?  The yellow, the red, or blue door? (enter the color)"
    ).lower()
    #yellow room process
    if "yellow" in which_door:
        print("You are in the laboratory")
        print(
            "You see a lab bench, test tubes, lab clothes, and a fire extinguisher. "
        )
        #checking the items, and retrieving the clue
        check_yellow = take_input(
            "Which would you like to check? (enter the item name)").lower()
        while "bench" not in check_yellow:
            check_yellow = take_input("Sorry, no clue here.  Try again: ").lower()
        print(
            "You have found Carbon, Iodide, Dubnium, Einsteinium, and Rubidium.  This is your clue."
        )

        back_to_the_hallway()
    #red/cellar room process
    elif "red" in which_door:
        print("You are in the cellar")
        check_red = take_input(
            "There are cans, bottles, wine, and brewing equipment in the cellar. Which would you like to check? "
        ).lower()
        while not (("brew" in check_red) or ("equipment" in check_red)):
            check_red = take_input("Sorry, no clue here.  Try again: ").lower()
        print(
            "You have found Arugula, Purple Onions, Potatoes, Leeks, and Eggplants.  This is your clue."
        )

        back_to_the_hallway()
    #blue/music room process
    elif "blue" in which_door:
        print("You are in the music room")
        print(
            "As you stand in the music room, you see music stands, rosin, a tuba case, sheet music, and you also hear creepy music playing behind a curtain."
        )
        time.sleep(5)
        print("SLAM! Oh no...the door just slammed shut behind you.")
        #The blue door slams shut behind the person as they stand in the music room.
        check_blue = take_input(
            "Which item, or where in the room, would you like to check? "
        ).lower()
        while not (("curtain" in check_blue) or ("creepy" in check_blue) or
                   ("behind" in check_blue)):
            check_blue = take_input("Sorry, no clue here.  Try again: ").lower()
        print(
            "You have found a Lute, an English horn, an Accordian, a Violin, and a Euphonium playing by themselves.  This is your clue."
        )

        back_to_the_hallway()  #They try to go back, but can't.
        print(
            "Oh no.  You just realize that the door is locked; you are trapped in the haunted music room."
        )
        time.sleep(1)
        print("Thankfully, you see a letter keypad on the door.")
        passcode = take_input("What password would you like to try? ").lower()
        while passcode != "leave":
            passcode = take_input(
                "I'm sorry, that is incorrect.  Please re-evaluate your clue and try again."
            ).lower()
        print("The door has opened and you may escape to the hallway.")

        back_to_the_hallway()

    #attempting the password in the hallway
    print("You are back in the hallway, facing a letter keypad.")
    password_or_another_room = take_input(
        "Do you want to guess the password or enter another room? ").lower()
    if ("password"
            in password_or_another_room) or ("guess"
                                             in password_or_another_room):
        currently_attempting_password = True  #the while loop allows for immediate reattempting of the password
        while currently_attempting_password:
            password_attempt = take_input(
                "Enter your attempt at the hallway password: ").lower()
            if "apple cider" in password_attempt:
                currently_attempting_password = False
                print("You have beat the basement!")
                time.sleep(1)
                print("A door creeeeeeaks open in the wall,")
                time.sleep(2)
                print("with a gaping pitch-black staircase looming behind it.")
                time.sleep(1)
                print(
                    "A gust of icy wind FORCES you upppppppppppppp the staircase..."
                )
                time.sleep(2)
                in_basement = False
            else:  #gives them a chance at reattempting the password immediately
                if "y" not in take_input(
                        "That is incorrect.  Would you like to try at the password again? (y/n)"
                ).lower():
                    currently_attempting_password = False



# Living room: Tv and couch
# Dining Room: Stack of Chairs and table
# Bathroom: Sink and Toilet
# Kitchen: Stove and Sink
locations = (
    ("LIVING ROOM", ("Tv", 5, 8), ("Couch", 5, 11), ("Carpet", 9, 2), ("START", 11, 0)),
    ("KITCHEN", ("Stove", 15, 11), ("Kitchen sink", 23, 10), ("Fridge", 20,
                                                              11)),
    ("BATHROOM", ("Bathroom sink", 3, 1), ("Toilet", 1, 1), ("Cupboard", 4,
                                                             1)),
    ("DINING ROOM", ("Stack of Chairs", 22, 1), ("Table", 17, 3), ("Sideboard",
                                                                   22, 5)),
)

current_loc = [
    0, 4
]  #the first int is the index of the room, and the second is the index of the object.


#helper functions for the main floor
def print_map():
    print("\n")
    print("                                           Ground Floor Map")
    print(" ")
    print(" 12┌───────────────────────────────────────────────────────────────────────────────────────────────┐")
    print("   │                                               |                                               │")
    print(" 11│   .   .   .   .  (2)  .   .   .   .   .   .       .   .  (1)  .   .   .   .  (2)  .   .   .   │")
    print("   │                 Couch                         |         Stove              Fridge             │")
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
    print("   │Toilet  Sink  board│                     START |                                   of Chairs   │")
    print(" 0 └───────────────────┴──────────────────────(┼)──────────────────────────────────────────────────┘")
    print("       1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  22  23  24")
    print("\n")

def get_current_room_obj_name():
    room_name = locations[current_loc[0]][0]
    obj_name = locations[current_loc[0]][current_loc[1]][0]
    return (room_name, obj_name)

def hotcold_get_new_room(previous_room):
    letter_to_idx = {"a": 0, "b": 1, "c": 2, "d": 3}
    user_letter_input = take_input("Out of the living room (a), the kitchen (b), the bathroom (c), and the dining room (d), where would you like to go? (enter the letter) ")
    current_loc[0] = int(letter_to_idx[user_letter_input])
    
    new_location = locations[current_loc[0]][0]
    print("You have moved from the", previous_room, "to the", new_location)


def hotcold_get_new_obj(previous_object):
    print("In this room, there is a:")
    object_counter = 1
    for idx in range(3):
        obj_name = locations[current_loc[0]][object_counter][0]
        print(
            "{} ({})".format(obj_name, object_counter)
        )  #outputs item (1) etc. depending on the item and the number of the item
        object_counter += 1

    current_loc[1] = int(
        take_input(
            "Out of the above objects, which would you like to check? (enter the number) ", True
        ))
    new_obj_tuple = locations[current_loc[0]][current_loc[1]]
    print("You have moved from the", previous_object, "to the", new_obj_tuple[0])



def get_room_obj_coord(room_obj_idxs):
    x_value = locations[room_obj_idxs[0]][room_obj_idxs[1]][1]
    y_value = locations[room_obj_idxs[0]][room_obj_idxs[1]][2]
    return (x_value, y_value)


def distance_coord_to_ladder(coord_pair):
    x_diff = ladder_coords[0] - coord_pair[0]
    y_diff = ladder_coords[1] - coord_pair[1]
    return math.sqrt(x_diff**2 + y_diff**2)


#take_input() is also used for the basement, and in the basement, take_input() checks for the word "map" as well.

#setting ladder object location and retrieving coordinates
ladder_loc = (random.randint(0, 3), random.randint(1, 3)
              )  #first int is the room index, second int is the object index
ladder_coords = get_room_obj_coord(ladder_loc)

playing_hotcold = True#so input will check for "map"

#MAIN FLOOR CODE
print("Congratulations!  You have made it to the main floor!")
print("You are now faced with an open-concept house layout. Type \"map\" at any prompt to re-print this image.")

print_map()

print("You have walked into the main floor, and are standing by the wall in the living room. \n")

distance_old = distance_coord_to_ladder((
    11,
    0,
))  #(12, 0) is the coordinate pair of the basement door (START)
start_loc_names = get_current_room_obj_name()
hotcold_get_new_room(start_loc_names[0])
hotcold_get_new_obj(start_loc_names[1])
#this variable is the current distance (after moving to the current object)
distance_new = distance_coord_to_ladder(get_room_obj_coord(current_loc))
starting_location = "Basement Stairs"

while playing_hotcold:
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

    while True:
        y_n_check = take_input(
            "Would you like to check another object in this room (y/n): ")
        if "y" in y_n_check:
            distance_old = distance_coord_to_ladder(
                get_room_obj_coord(current_loc))

            from_room_obj = get_current_room_obj_name()
            hotcold_get_new_obj(from_room_obj[1])

            distance_new = distance_coord_to_ladder(
                get_room_obj_coord(current_loc))
            break
        else:
            y_n_other_room = take_input(
                "Would you like to go to another room then? (y/n): ")
            if "y" in y_n_other_room:
                distance_old = distance_coord_to_ladder(
                    get_room_obj_coord(current_loc))

                from_room_obj = get_current_room_obj_name()# ("ROOM", "OBJECT")
                hotcold_get_new_room(from_room_obj[0])
                hotcold_get_new_obj(from_room_obj[1])

                distance_new = distance_coord_to_ladder(
                    get_room_obj_coord(current_loc))
                break
            else:
                encouragingMessage()

#The ladder location is at a specific thing in the main floor (bathroom sink, chairs, etc.)
print(
    "CREAK. Whoosh. A trapdoor opens above you, and a ladder falls down, missing you by a hair."
)
open_trapdoor = str(input("Would you like to climb up the ladder? y/n "))
while "n" in open_trapdoor:
  encouragingMessage()
  open_trapdoor = take_input("Please try again: ").lower()
print("You steadily climb the ladder and reach a circular door. ")
open_2nd_door = str(input("Would you like to open the second door? "))
while "n" in open_2nd_door:
  encouragingMessage()
  open_2nd_door = take_input("Please try again: ").lower()
print("You open the door, and realize you are sliding down a water slide! ")
time.sleep(3)
print("You land in a pool, and quickly remember where you are! ")
print("Just a few minutes ago, you were swimming in your friend's pool! ")
time.sleep(3)
print("You look down at the bottom of the pool, see a vortex, and realize you must have been sucked in! ")
time.sleep(3)
print("With all your strength, you pull yourself out of the pool. ")
time.sleep(3)
print("You are saved!  Congratulations!  You have escaped from the house and now you are free! ")
print("Just remember to always look (at the bottom of every pool) before you leap. ")