###########################################################################################
# Name: Dr. Jean Gourd
# Date: 2022-01-04
# Description: A basic GUI Room Adventure game to show its mechanics and gameplay.
###########################################################################################

###########################################################################################
# import libraries
from tkinter import *

###########################################################################################
# constants
#the supported vocabulary verbs
VERBS = [ "go", "look", "take", "use", "fly" ]
#the supported quit commands
QUIT_COMMANDS = [ "exit", "quit", "bye" ]

###########################################################################################
# the blueprint for a room

class Room:
    # the constructor
    def __init__(self, name, image):
        # rooms have a name, image, description, exits (e.g., south), exit locations (e.g., to the
        # south is room n), items (e.g., table), item descriptions (for each item), and grabbables
        # (things that can be taken into inventory)
        self._name = name
        self._image = image
        self._description = ""
        self._exits = []
        self._exitLocations = []
        self._items = []
        self._itemDescriptions = []
        self._grabbables = []
        self._hint = ""

    # getters and setters for the instance variables
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def exits(self):
        return self._exits

    @exits.setter
    def exits(self, value):
        self._exits = value

    @property
    def exitLocations(self):
        return self._exitLocations

    @exitLocations.setter
    def exitLocations(self, value):
        self._exitLocations = value

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value

    @property
    def itemDescriptions(self):
        return self._itemDescriptions

    @itemDescriptions.setter
    def itemDescriptions(self, value):
        self._itemDescriptions = value

    @property
    def grabbables(self):
        return self._grabbables

    @grabbables.setter
    def grabbables(self, value):
        self._grabbables = value
        
        
    @property
    def hint(self):
        return self._hint
    @hint.setter
    def hint(self, value):
        self._hint = value
        
    # returns a string description of the room
    # adds an exit to the room
    # the exit is a string (e.g., north)
    # the room is an instance of a room
    def addExit(self, exit, room):
        # append the exit and room to the appropriate lists
        self._exits.append(exit)
        self._exitLocations.append(room)

    # adds an item to the room
    # the item is a string (e.g., table)
    # the desc is a string that describes the item (e.g., it is made of wood)
    def addItem(self, item, desc):
        # append the item and description to the appropriate lists
        self._items.append(item)
        self._itemDescriptions.append(desc)

    # adds a grabbable item to the room
    # the item is a string (e.g., key)
    def addGrabbable(self, item):
        # append the item to the list
        self._grabbables.append(item)
    def delGrabbable(self, item):
    # remove the item from the list
        self._grabbables.remove(item)
    # returns a string description of the room as follows:
    #  <name>
    #  <description>
    #  <items>
    #  <exits>
    # e.g.:
    #  Room 1
    #  You look around the room.
    #  You see: chair table 
    #  Exits: east south 
    def __str__(self):
        # first, the room name and description
        s = "You are in {} .\n".format(self._name)
        s += "{}\n".format(self._description)
        s += "\n{}\n".format(self.hint)

        # next, the items in the room
        s += "You see: "
        for item in self._items:
            s += item + " "
        s += "\n"

        # next, the exits from the room
        s += "Exits: "
        for exit in self._exits:
            s += exit + " "

        
        return s
###########################################################################################
# the blueprint for a Game
# inherits from the Frame class of Tkinter
class Game(Frame):
    # the constructor
    def __init__(self, parent):
        # call the constructor in the Frame superclass
        Frame.__init__(self, parent)

    # creates the rooms
    def createRooms(self):
        global r6
        global r7
        #global Game
        # a list of rooms will store all of the rooms
        # r1 through r4 are the four rooms in the "mansion"
        # currentRoom is the room the player is currently in (which can be one of r1 through r4)
        Game.rooms = []

        # first, create the room instances so that they can be referenced below
        r1 = Room("Hogwarts Main Hall", "R1.gif")
        r2 = Room("Gryffindor Common Area", "R2.gif")
        r3 = Room("Quidditch Arena", "R3.gif")
        r4 = Room("Hagrid's Place", "R4.b2.gif")
        r5 = Room("Graveyard", "R5.gif")
        r6 = Room("DEATH ROOM!", "skull.gif")
        r7 = Room("WINNING ROOM1", "hp.gif")

        # room 1
        r1.description = "\n\nHelp, Voldemort is back! You need to find Harry and help save Hogwarts! \nSearch the grounds for Harry, be on the lookout for items that help you on your quest. \nBe careful, Voldemort hid cursed objects that can kill you if you touch them. \nBest of luck, young wizard! \n \n"
        r1.addExit("east", r2)
        r1.addGrabbable("wand")
        r1.addGrabbable("goblet")
        r1.addItem("table", "It is made of oak. Harry's wand, a goblet, and the sorting hat rest on it.")
        Game.rooms.append(r1)

        # room 2
        r2.description = "You are now in the Common Area, look around and see if you can find anything that may be helpful!"
        r2.hint = "Hint: Pick objects that you think will help you find Harry, but be careful."
        r2.addExit("south", r3)
        r2.addGrabbable("cloak")
        r2.addGrabbable("diary")
        r2.addItem("bed", "It is made. A cloak and a diary rest on it.")
        r2.addItem("fireplace", "There is a fire blazing.")
        Game.rooms.append(r2)

        # room 3
        r3.description = "You are now in the Arena!!."
        r3.hint = "Hint: Quick!! FLY away on the broom before the dementor gets you..."
        r3.addExit("west", r4)
        r3.addGrabbable("broom")
        r3.addGrabbable("dementor")
        r3.addItem("field", "It is a big grassy field. There is a broom and a dementor here.")
        Game.rooms.append(r3)

        # room 4
        r4.description = "You are now at Hagrid's Place!!"
        r4.hint = "Hint: Hmmm Maybe consider taking a better look at the chairs..."
        r4.addExit("north", r5)
        r4.addGrabbable("harry")
        r4.addGrabbable("beer")
        r4.addItem("table", "It is a massive table. There is a beer on it.")
        r4.addItem("chairs", "There are three chairs. Harry, Ron, and Hermione are sitting in them.")
        Game.rooms.append(r4)

        #room 5
        r5.description = "You are now in the Graveyard!!"
        r5.hint = "Oh no Voldemort's here ... \n There are 2 specific items in your inventory that can help you \n Choose Wisely."
        r5.addExit("none", r5)
        r5.addItem("gravestone", "There is a gravestone that reads Tom Riddle.")
        r5.addItem("voldemort", "He who shall not be named is standing in front of you.")
        r5.addItem("dobby", "Dobby is here to help Harry Potter and friends! \nQuick, use Harry to fight voldemort before he kills you and destroys Hogwarts!")
        Game.rooms.append(r5)
        
        #room 6
        r6.description = "You Died! Game over!"
        Game.rooms.append(r6)
        
        r7.description = "You did it!! You won!"
        Game.rooms.append(r7)
        
        # set room 1 as the current room at the beginning of the game
        Game.currentRoom = r1

        # initialize the player's inventory
        Game.inventory = []


    # sets up the GUI
    def setupGUI(self):
        # organize the GUI
        self.pack(fill=BOTH, expand=1)

        # setup the player input at the bottom of the GUI
        # the widget is a Tkinter Entry
        # set its background to white
        # bind the return key to the function process() in the class
        # bind the tab key to the function complete() in the class
        # push it to the bottom of the GUI and let it fill horizontally
        # give it focus so the player doesn't have to click on it
        Game.player_input = Entry(self, bg="white")
        Game.player_input.bind("<Return>", self.process)
        Game.player_input.bind("<Tab>", self.complete)
        Game.player_input.pack(side=BOTTOM, fill=X)
        Game.player_input.focus()

        # setup the image to the left of the GUI
        # the widget is a Tkinter Label
        # don't let the image control the widget's size
        img = None
        Game.image = Label(self, width=WIDTH // 2, image=img)
        Game.image.image = img
        Game.image.pack(side=LEFT, fill=Y)
        Game.image.pack_propagate(False)

        # setup the text to the right of the GUI
        # first, the frame in which the text will be placed
        text_frame = Frame(self, width=WIDTH // 2)
        # the widget is a Tkinter Text
        # disable it by default
        # don't let the widget control the frame's size
        Game.text = Text(text_frame, bg="lightgray", state=DISABLED)
        Game.text.pack(fill=Y, expand=1)
        text_frame.pack(side=RIGHT, fill=BOTH)
        text_frame.pack_propagate(True)

    # set the current room image on the left of the GUI
    def setRoomImage(self):
        if (Game.currentRoom == None):
            # if dead, set the skull image
            Game.img = PhotoImage(file="skull.gif")
        else:
            # otherwise grab the image for the current room
            Game.img = PhotoImage(file=Game.currentRoom.image)

        # display the image on the left of the GUI
        Game.image.config(image=Game.img)
        Game.image.image = Game.img

    # sets the status displayed on the right of the GUI
    def setStatus(self, status):
        # enable the text widget, clear it, set it, and disable it
        Game.text.config(state=NORMAL)
        Game.text.delete("1.0", END)
        if (Game.currentRoom == r6):
            # if dead, let the player know
            Game.text.insert(END, "You are dead. Next time, think before you take and look ... \n Now the only thing left for you to do is quit.\n")
        elif (Game.currentRoom == r7):
            Game.text.insert( END, "You did it! You saved Hogwarts! \nGreat job, young wizard. We couldn't have done it without you. You can quit now!!! \n")
        else:
            # otherwise, display the appropriate status
            Game.text.insert(END, "{}\n\n{}\nYou are carrying: {}\n\n".format(status, Game.currentRoom, Game.inventory))
        Game.text.config(state=DISABLED)

        # support for tab completion
        # add the words to support
        if (Game.currentRoom != None):
            Game.words = VERBS + QUIT_COMMANDS + Game.inventory + Game.currentRoom.exits + Game.currentRoom.items + Game.currentRoom.grabbables
        



    # play the game
    def play(self):
        # create the room instances
        self.createRooms()
        # configure the GUI
        self.setupGUI()
        # set the current room
        self.setRoomImage()
        # set the initial status
        self.setStatus("WELCOME TO ROOM ADVENTURE!")

    # processes the player's input
    def process(self, event):        
        # grab the player's input from the input at the bottom of the GUI
        action = Game.player_input.get()
        # set the user's input to lowercase to make it easier to compare the verb and noun to known values
        action = action.lower().strip()

        # exit the game if the player wants to leave (supports quit, exit, and bye)
        if (action in QUIT_COMMANDS):
            exit(0)

        # if the current room is None, then the player is dead
        # this only happens if the player goes south when in room 4
        if (Game.currentRoom == None):
            # clear the player's input
            Game.player_input.delete(0, END)
            return

        # set a default response
        response = "I don't understand. Try verb noun. Valid verbs\nare {}.".format(", ".join(VERBS))
        # split the user input into words (words are separated by spaces) and store the words in a list
        words = action.split()

        # the game only understands two word inputs
        if (len(words) == 2):
            # isolate the verb and noun
            verb = words[0].strip()
            noun = words[1].strip()


            #room 1 nouns:                    
            if noun == "goblet": #if you try and take the goblet you die
                if verb == "take":
                    Game.currentRoom = r6


            #room 2 nouns: 
            
            if noun == "diary": #diary was tom riddles- it is cursed and will kill you if you touch it
                if verb == "take":
                    Game.currentRoom = r6

            if noun == "fireplace": #looking in a fireplace that is burining will set you on fire. duh.
                if verb == "look":
                    Game.currentRoom = r6

                
            #room 3 nouns: 
            if noun == "dementor": #if you take the dementor, it kills you and you die- ending game
                if verb == "take":
                    Game.currentRoom = r6
            
  
            if Game.currentRoom.name == "Graveyard": #in the fifth and final room, no exits because only way out is death or winning, using exits to determine which room player is in
                    if "harry" not in Game.inventory: 
                        Game.currentRoom = r6            
                        
                    if "wand" not in Game.inventory:
                        Game.currentRoom = r6                        
                        
                    if verb == "use":
                        if noun == "harry": #use harry to go fight off voldemort, but he gets pinned up against the grave
                            print()
                        elif noun == "wand": #one way to end game- use wand to disarm voldemort
                            Game.currentRoom = r7
                            
                        else: #if player doesn't use wand, they didn't win
                            print("\nThat didn't work. Try something else.")
                            


            # we need a valid verb
            if (verb in VERBS):
                # the verb is: go
                if (verb == "go"):
                    # set a default response
                    response = "Invalid exit."
                    # check for valid exits in the current room
                    for i in range(len(Game.currentRoom.exits)):
                        # a valid exit is found
                        if (noun == Game.currentRoom.exits[i]):
                            # if broom is in inventory, you cannot use the go verb anymore, you have to fly
                            if "broom" in Game.inventory:
                                break
                             # change the current room to the one that is associated with the specified exit
                            Game.currentRoom =  Game.currentRoom.exitLocations[i]
                            # set the response (success)
                            response = "Room changed."
                            # no need to check any more exits
                            break
                             
 
                # the verb is: look
                elif (verb == "look"):
                    # set a default response
                    response = "I don't see that item."
                    # check for valid items in the current room
                    for i in range(len(Game.currentRoom.items)):
                        # a valid item is found
                        if (noun == Game.currentRoom.items[i]):
                            # set the response to the item's description and update if necessary (item taken means its not in old description)
                            #room 1 description updates: 
                            if noun == "table" and "wand" in Game.inventory: #if the item is in the inventory, its not on the table so it needs to be removed
                                Game.currentRoom.itemDescriptions[i] = "It is made of oak. A goblet and the sorting hat rest on it."
                            
                            #room 2 description updates:
                            elif noun == "bed" and "cloak" in Game.inventory:
                                Game.currentRoom.itemDescriptions[i] = "It is made. A diary rests on it."
                            
                            #room 3 description updates:
                            elif noun == "field" and "broom" in Game.inventory:
                                Game.currentRoom.itemDescriptions[i] = "It is a big grassy field. There is a dementor here."
                            
                            #room 4 description updates:
                            elif noun == "table" and "beer" in Game.inventory:
                                Game.currentRoom.itemDescriptions[i] = "It is a massive table. Nothing rests on it."
                            elif noun == "chairs" and "harry" in Game.inventory:
                                Game.currentRoom.itemDescriptions[i] = "There are three chairs. Ron and Hermione are sitting in them."
                            
                            # set the response with all updates made
                            response = Game.currentRoom.itemDescriptions[i]       
                            # no need to check any more items
                            break
         
         
                # the verb is: take
                elif (verb == "take"):
                    # set a default response
                    response = "I don't see that item."
                    if noun == "hat": #hat is not a grabbable, but has different response if it is taken (response can't be I don't see that item)
                        response = "You cannot pick up the sorting hat. It gets very cranky and does not want to go with you."
                    # check for valid grabbable items in the current room
                    for grabbable in Game.currentRoom.grabbables:
                        # a valid grabbable item is found
                        if (noun == grabbable):
                            # add the grabbable item to the player's inventory
                            Game.inventory.append(grabbable)
                            # remove the grabbable item from the room
                            Game.currentRoom.delGrabbable(grabbable)
                            # set the response (success)
                            response = "Item grabbed."
                            # no need to check any more grabbable items
                            break
                
               
               # the verb is use
                elif (verb == "use"):
                    # set a default response
                    response = "I don't see that item."
                    # check for valid grabbable items in inventory to be used
                    for grabbable in Game.inventory:
                        # a valid grabbable is found in inventory
                        if noun == grabbable: #add grabbable to room, but do not remove it from inventory- main function of use is to use harry to fight at end of game, game will end and voldemort will kill us if harry is not always with us
                            # add grabbable to the current room
                            Game.currentRoom.addGrabbable(grabbable)
                            # set the responses (success)
                            response = "Item used."
                            # no need to check any more grabbable items
                            break
                
               # the verb is: fly
                elif (verb == "fly"):
                    # set a default response
                    response = "Invalid exit."
                    # check for valid exits in the current room
                    for i in range(len(Game.currentRoom.exits)):
                        # a valid exit is found
                        if (noun == Game.currentRoom.exits[i]):
                            # if broom is in inventory, you cannot use the go verb anymore, you have to fly
                            if "broom" in Game.inventory:
                                 # change the current room to the one that is associated with the specified exit
                                Game.currentRoom =  Game.currentRoom.exitLocations[i]
                            # set the response (success)
                            response = "Room changed."
                            # no need to check any more exits
                            break
                    

        # display the response on the right of the GUI
        # display the room's image on the left of the GUI
        # clear the player's input
        self.setStatus(response)
        self.setRoomImage()
        Game.player_input.delete(0, END)


    # implements tab completion in the Entry widget
    def complete(self, event):
        # get user input and the last word of input
        words = Game.player_input.get().split()
        # continue only if there are words in the user's input
        if (len(words)):
            last_word = words[-1]
            # check if the last word of input is part of a valid verb/noun
            results = [ x for x in Game.words if x.startswith(last_word) ]

            # initially, there is no matching verb/noun
            match = None

            # is there only a single valid verb/noun?
            if (len(results) == 1):
                # the result is a match
                match = results[0]
            # are there multiple valid verbs/nouns?
            elif (len(results) > 1):
                # find the longest starting substring of all verbs/nouns
                for i in range(1, len(min(results, key=len)) + 1):
                    # get the current substring
                    match = results[0][:i]
                    # find all matches
                    matches = [ x for x in results if x.startswith(match) ]
                    # if there are less matches than verbs/nouns
                    if (len(matches) != len(results)):
                        # go back to the previous substring
                        match = match[:-1]
                        # stop checking
                        break
            # if a match exists, replace the user's input
            if (match):
                # clear user input
                Game.player_input.delete(0, END)
                # add all but the last (matched) verb/noun
                for word in words[:-1]:
                    Game.player_input.insert(END, "{} ".format(word))
                # add the match
                Game.player_input.insert(END, "{}{}".format(match, " " if (len(results) == 1) else ""))

        # prevents the tab key from highlighting the text in the Entry widget
        return "break"

###########################################################################################
# START THE GAME!!!

f = "you burned alive"


# the default size of the GUI is 800x600
WIDTH = 850
HEIGHT = 1300

# create the window
window = Tk()
window.title("Room Adventure")

# create the GUI as a Tkinter canvas inside the window
g = Game(window)
# play the game
g.play()

# wait for the window to close
window.mainloop()
