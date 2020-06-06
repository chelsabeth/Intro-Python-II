from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# print(room["treasure"].s_to.name)

# PLANNING:
'''
*The Brave Knight* 
display welcome message & describe game
player will start outside, tell them their location
prompt user to make a choice between n, s, e, w
    if user quits the game, stop the loop and show a msg
based on players chosen direction, go to new location & display new location
make sure players choice is a valid direction - if not display error msg
'''
current_player = Player("adventurer", room['outside'])

welcome_msg = f"Welcome {current_player.name}, let's begin your brave journey!\nYou are currently in the {current_player.current_room.name}, Description: {current_player.current_room.description}"
# quit_msg = "Thanks for playing 'The Brave Knight'!"

#
# Main
#

# step 1 - display welcome message & describe game
# welcome_msg = "Welcome to 'The Brave Knight', an adventure game! Please pick a direction to go in - you are currently outside"



# step 2 - prompt user to make a choice
def get_user_direction():
    direction = input("please choose a direction to go in - n, s, e, w\n")
    return direction


# step 3 - if user quits game, show message
# def quit_game():
    # quit = input("press q to quit")
    # quit_msg = "Thanks for playing 'The Brave Knight'!"
    # print(quit_msg)

def show_location_info():
    print(f"You are now in the {current_player.current_room.name}, Description: {current_player.current_room.description}")
    current_player.current_room.items_in_room()


def no_room_opt():
    print("Sorry, there is nothing in that direction")

# step 4 - compare users input and take them to location, if location is invalid, throw error
    # check the player's current location and see if there is 
    # a room in the specified direction 
    # if there is, move them there to that room 
    # otherwise, print a message saying "we can't go there" and 
    # not move the player 
def get_location(get_user_direction):
    if get_user_direction == "n" and not current_player.current_room.n_to == None:
        current_player.current_room = current_player.current_room.n_to
        show_location_info()
    elif get_user_direction == "s" and not current_player.current_room.s_to == None:
        current_player.current_room = current_player.current_room.s_to
        show_location_info()
    elif get_user_direction == "e" and not current_player.current_room.e_to == None:
        current_player.current_room = current_player.current_room.e_to
        show_location_info()
    elif get_user_direction == "w" and not current_player.current_room.w_to == None:
        current_player.current_room = current_player.current_room.w_to
        show_location_info()
    else:
        no_room_opt()



# ITEMS
items_list = [
    Item('bag of gold', 'oooh shiny'),
    Item('shield', 'to protect you'),
    Item('sword', 'slay your enemy'),
    Item('torch', 'light the way'),
    Item('rock', 'fight like David & Goliath')
]

# "saber": Item("light saber", "May the force be with you.")

room['narrow'].items.append(items_list[3])
room['foyer'].items.append(items_list[1])
room['foyer'].items.append(items_list[2])
room['outside'].items.append(items_list[0])
room['overlook'].items.append(items_list[4])


# print(items_list[0].name)
    


# Make a new player object that is currently in the 'outside' room.

# print(current_player.current_room.items)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
print(welcome_msg)
while True:
    choice = get_user_direction()
    get_location(choice)
