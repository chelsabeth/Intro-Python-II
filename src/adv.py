from room import Room

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
*Penelope the Princess* 
display welcome message & describe game
player will start outside, tell them their location
prompt user to make a choice between n, s, e, w
    if user quits the game, stop the loop and show a msg
based on players chosen direction, go to new location & display new location
make sure players choice is a valid direction - if not display error msg
'''

welcome_msg = "Welcome to Penelope the Princess, an adventure game! Please pick a direction to go in - you are currently outside"
quit_msg = "Thanks for playing Penelope the Princess!"

direction_options = {
    1: "n",
    2: "s",
    3: "e",
    4: "w",
    5: "q"
}

#
# Main
#

# step 1 - display welcome message & describe game
def show_welcome_msg():
    welcome_msg = "Welcome to Penelope the Princess, an adventure game! Please pick a direction to go in - you are currently outside"
    print(welcome_msg)


# step 2 - prompt user to make a choice
def get_user_direction():
    direction = input("[1] n [2] s [3] e [4] w [5] q")
    return direction_options[int(direction)]

# Make a new player object that is currently in the 'outside' room.

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
