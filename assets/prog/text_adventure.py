# coding: utf-8
'''
Maze game

Define maze in 'map':
Letters relate to a description in the dictionary;
the numbers in the 2nd grid are for items.
'''
map = [[[1,1,1,1,1,1,1,1,1,1],
       [1,'X','A','A','A','A','B',1,1,1],
       [1,1,1,1,1,1,'A',1,1,1],
       [1,1,1,1,'D','A','E','A','F',1],
       [1,'G','A','A','J',1,1,'C',1,1],
       [1,'A',1,1,'J','K','L','E','F',1],
       [1,'M',1,1,'C',1,1,'F',1,1],
       [1,'N','M','A','B',1,1,1,1,1],
       [1,'N',1,1,1,1,1,1,1,1],
       [1,'Z',1,1,1,1,1,1,1,1]],
       
       [[0,0,0,0,0,0,0,0,0,0],
        [0,1,2,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]]]

description = {'A':'You are in a dark corridor.',
               'B':'You have come to a damp corner.',
               'C':'You have arrived at a junction.',
               'D':'You can see a pile of bones from the last adventurer.',
               'E':'The ceiling lowers until you have to stoop here.',
               'F':'You have reached a dead end.',
               'G':'This part of the dungeon smells terribly.',
               'H':'You arrive at a four-way junction.',
               'J':'You are at a three-way junction.',
               'K':'Vicious-looking rats scurry around your feet.',
               'L':'The ground is wet here.',
               'M':'You feel a fresh breeze on your face.',
               'N':'The breeze is getting stronger. The dungeon is getting lighter here.',
               'X':'There is a hole in the ceiling but it is too high to reach.',
               'Z':'EXIT'}

item = [['nothing'],
        ['rusty sword'],
        ['piece of rope'],
        ['gold coin'],
        ['mouldy bread'],
        ['water bottle'],
        ['crystal vial'],
        ['dead crow']]

#Set player starting position:
playerRow = 1
playerColumn = 1

#Set map exit location:
exitRow = 9
exitColumn = 1

#Set game loop to True
playGame = True

#Reset possible directions
north = False
east = False
south = False
west = False

#Intro
print('\n\nWelcome, peasant...You have been cast into the Dungeon of Doom! You must escape with your life and your sanity...')
print('\nType North, South, East and West to move in that direction.')
print('\nYou may abbreviate the directions to N, S, E and W.')
print('\nFind the exit if your feeble mind will allow it.')
input('\nPress ENTER when you are ready, fool...')

#
#Main game loop
#
while playGame:
    #Reset possible directions
    north = False
    east = False
    south = False
    west = False

    #Print current location
    locationDescription = map[0][playerRow][playerColumn]
    locationItem = item[map[1][playerRow][playerColumn]]
    
    print('\n')
    print(description[locationDescription])

    #IF there is an item, print it
    if map[1][playerRow][playerColumn] != 0:
        print('You can see a ' + str(locationItem).strip('[]\'') + '.')
        
    print('\nDirections from here are: ')

    #Get possible directions
    if map[0][playerRow-1][playerColumn] != 1:
        print('North')
        north = True
    if map[0][playerRow][playerColumn+1] != 1:
        print('East')
        east = True
    if map[0][playerRow+1][playerColumn] != 1:
        print('South')
        south = True
    if map[0][playerRow][playerColumn-1] != 1:
        print('West')
        west = True

    #Wait for player to enter direction
    direction = input('Awaiting your command: ')
    if direction == '': #Don't allow empty input
        direction = 'ASK FOR INPUT AGAIN'

    #Process direction 
    if str.lower(direction[0]) == 'n' and north == True:
        playerRow -=1
    elif str.lower(direction[0]) == 'e' and east == True:
        playerColumn +=1
    elif str.lower(direction[0]) == 's' and south == True:
        playerRow +=1
    elif str.lower(direction[0]) == 'w' and west == True:
        playerColumn -=1
    elif str.lower(direction[0]) == 'q':
        playGame = False
    else:
        print('\n***Please enter a valid direction or \'quit\'.***\n')
    
    #Is the player at the exit?
    if (playerRow == exitRow) and (playerColumn == exitColumn):
        print('\nWell done! You escaped! But for how long?')
        print('\nYou hear a noise behing you and glance nervously back at the dungeon exit.')
        print('\nSomething dark and cruel-looking is slithering towards you.')
        print('\nAs you turn to run, you feel a crack on the back of your head before losing conciousness...')
        playGame = False
    
