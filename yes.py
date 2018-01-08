# Midyear project

""" 
alrighty so the rules of the game:
a crime went down and the player gotta solve it
1. the player gotta pick a character
2. they gotta enter the room
3. now they see if there are clues
4. ask if they can remove anyone from the suspect list
5. if yes, well remove the suspect. if they remove the guilty person they lose and game over. otherwise, well i guess they got closer to figuring it out.
6. ask if they know who did it for sure. if they get it right, they win. if not, they lose and game over. they can only guess once.
then u just sorta repeat all that till the game is over.
"""

import random
suspects = ("Tanish", "Chris", "Melissa", "Mr. Isecke", "Suspect 5", "Suspect 6")
rooms = ("The Compsci Room", "Lower Caf", "Upper Caf", "The gym", "The grill", "The breezeway", "Mr. Zhang's room", "Mr. Demeter's room", "Ms. Fillebrown's room")


# do we need a class? i dont see how we would use it
def print_list():
    # this part is from battle
    var3 = 0
    for c in suspects:
        print("%d : %s" % (var3, c))
        var3 += 1


def clues():
    """
    alrighty so what i'm thinking is that each suspect gets their own clues specific to them
    will that be too hard to do tho?
    because i dont see how the clues would work otherwise
    """
    
    suspect = random.choice(suspects)
    if suspect == "Tanish":
        clues = {"Clue 1": "", "Clue 2": "", "Clue 3": ""}
    if suspect == "Chris":
        clues = {"Clue 1": "", "Clue 2": "", "Clue 3": ""}
    if suspect == "Melissa":
        clues = {"Clue 1": "", "Clue 2": "", "Clue 3": ""}
    if suspect == "Mr. Isecke":
        clues = {"Clue 1": "", "Clue 2": "", "Clue 3": ""}


def room_choice():
    # so we pick three rooms for the clues to be hidden in
    room_choice1 = random.choice(rooms)
    room_choice2 = random.choice(rooms)
    if room_choice1 == room_choice2:
        room_choice2 = random.choice(rooms)
    room_choice3 = random.choice(rooms)
    if room_choice3 == room_choice1 or room_choice3 == room_choice2:
        room_choice3 = random.choice(rooms)
        
    """
    now what we could also do is remove the room from the list so that it cant be picked again
    but we would need a second list bc you want all the rooms later on
    """


def gameplay():
    print("Welcome to Clue! In this game, you'll have to help Mr. Respass figure out who took his computer."
          "\nA list of suspects has already been made. But first of all, who are you? "
          "\nTo select a character, type in its number.")

    print_list()
    # this next part is also from battle, its just error checking
    char_choice = int(input())
    while char_choice < 0 or char_choice >= len(suspects):
        choice = int(input("Please choose between 0 and " + str(len(suspects)) + "."))

    # ok so this part doesn't work because it gives you the number of the character chosen, not the name
    print("Hello, %s. Think you can solve the mystery of who took Mr. Respass' computer?" % char_choice)


gameplay()
