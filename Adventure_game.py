# =================================== Variables ===================================
pickup_item = []   #this is the list for the items picked up by the user 
user_location = []   #this is the list for the rooms visited by the user 
all_rooms = ["room1","room2","room3","room4","room5","room6","room7","room8","room9","room10","room11","room12"]   #this is the list of all the rooms in the game

# =================================== Functions ===================================
def user_controls():   #this is the function that prints all the controls for the user
    print("Enter ,")
    print("N/n - To travel to the room in the North direction.")
    print("S/s - To travel to the room in the South direction.")
    print("E/e - To travel to the room in the East direction.")
    print("W/w - To travel to the room in the West direction.")
    print("B/b - To travel back to the previous room.")
    print("O/o - To observe the room for objects and items.")
    print("I/i - To take an item into your Inventory.")
    print("V/v - To view items in your Inventory.")
    print("L/l - To view user controls list.")
    print("R/r - To restart the game.")
    print("C/c - To check all visited rooms.")
    print("X/x - To Quit Game.")
    print("--------------------------------------------------")

def go_back(room_number):   #this is the function that allows the user to go back to the previous room 
    if len(user_location) > 1:
        previous_room = user_location[-2]
        user_location.append(previous_room)
        g = Game(previous_room)
        g.play()
    else:
        print("*  There aren't any rooms before first room.")
        print("*  You are still in the "+room_number+".")
    print("----------------------------------------------------")

def view_inventory():   #this is the function that allows user to check the items that were picked up
    print("*  Currently the item/items in your inventory.")
    if len(pickup_item) == 0:
        print("*  Your inventory is empty.")
    else:
        for items in pickup_item:
            print("            + " + items)
        print("----------------------------------------------------")
        
def restart_game():   #this is the function that allows user to restart the game
    restart_option = str(input("Do you want to restart? (Y/N).").upper())
    if restart_option == "Y":
        print("*  Game will restart.")
        pickup_item.clear()
        user_location.clear()
        main()
    elif restart_option == "N":
        print("*  Returning to the game again.")
    else:
        print("*  Wrong input.Try again !")
    print("----------------------------------------------------")
   

def exit_game():   #this is the function that allows user to exit the game
    exit_option = str(input("Do you want to quit? (Y/N).").upper())
    if exit_option == "Y":
        print("*  Exiting Now. Play again later!")
        exit()
    elif exit_option == "N":
        print("*  Return to the game again.")
    else:
        print("*  Wrong input.Try again !")
    print("----------------------------------------------------")

def observe_room(room_item):    #this is the function that allows user to observe the room for objects and items present in the room
    print("*  You observed the "+user_location[-1]+".")
    print("*  You noticed,")
    if len(room_item) == 0:
        print("*  This room is empty.")
    else:
        for items in room_item:
            print("            + " + items)
    print("----------------------------------------------------")

def pick_room_item(room_item):   #this is the function that helps the addto_inventory function work. This checks the inventory and add the item to the inventory 
    inventory_input = str(
        input("Enter the exact item name of the item \nyou want to take into your inventory: "))
    if inventory_input in room_item:
        pickup_item.append(inventory_input)
        print("* "+inventory_input + " was added to your inventory.")
        room_item.remove(inventory_input)
    else:
        print("*  Item name given is Incorrect. Please Try again !")

def addto_inventory(room_item):   #this is the function that uses the pick_room_item function.
    if len(pickup_item) == 0:
        print("*  Your inventory is empty.")
        pick_room_item(room_item)
    else:
        pick_room_item(room_item)
    print("----------------------------------------------------")

def travelto_next_room(room_number, travel_direction):   #this is the main function that alloes user to move to the next room and call the game class
    if room_number != 0:
        user_location.append("room" + str(room_number))
        g = Game("room" + str(room_number))
        g.play()
    else:
        print("*  No room to the "+travel_direction+". Try another Direction !")
    print("----------------------------------------------------")

def check_visited_rooms():  #this is the function that allows user to check the rooms that have already been visited
    room_order = 1
    print("*  All visited rooms in order,")
    for room in user_location:
        if room_order % 4 == 0:
            print(str(room_order)+"."+room)
        else:
            print(str(room_order)+"."+room, end="   ")
        room_order += 1
    print("")
    print("")
    print("*  Visited times of each room,")
    count = 1
    for room in all_rooms:
        if room in user_location:
            count_room = user_location.count(room)
            if room_order % 4 == 0:
                print("+"+room+":"+str(count_room)+" times")
            else:
                print("+"+room+":"+str(count_room)+" times", end="   ")
            room_order += 1
    print("")
    print("----------------------------------------------------")

# =================================== classes ===================================
class Item:
    def __init__(self, name):
        self.name = name

room1_items = (Item(['spoon', 'fork', 'knife'])).name
room2_items = (Item(['apple', 'bat', 'ball'])).name
room3_items = (Item(['pen', 'book', 'cup'])).name
room4_items = (Item(['torch', 'bottle', 'battery'])).name
room5_items = (Item(['dice', 'rubic cube', 'clock'])).name
room6_items = (Item(['toy', 'shoe', 'bulb'])).name
room7_items = (Item(['laptop', 'charger', 'usb'])).name
room8_items = (Item(['plate', 'cup', 'mug'])).name
room9_items = (Item(['hammer', 'plier', 'brush'])).name
room10_items = (Item(['bucket', 'mop', 'lamp'])).name
room11_items = (Item(['bandaid', 'gauze', 'water'])).name
room12_items = (Item(['ladder', 'bin', 'phone'])).name

class Player:
    def __init__(self, name):
        self.name = name
        self.items = []

class Room:
    def __init__(self, name, item, north, east, south, west):
        self.name = name

        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.item = item

    def current_room(room):   #This is the function that checks the user input and calls the related function according to that user input
        if len(user_location) == 0:
            user_location.append(room.name)
            print("*  You entered the " + room.name+".")
            print("*  Your current location is " +room.name+ ".")
        else:
         print("*  You entered the "+room.name+".")
         print("*  Your current location is " + room.name + ".")

        while True:
            user_input = str(input("What do you want to do now? "))
            print("----------------------------------------------------")
            user_input = user_input.upper()
            if user_input == "N":
                travelto_next_room(room.north, "North side")

            elif user_input == "E":
                travelto_next_room(room.east, "East side")

            elif user_input == "W":
                travelto_next_room(room.west, "West side")

            elif user_input == "S":
                travelto_next_room(room.south, "South side")

            elif user_input == "O":
                observe_room(room.item)

            elif user_input == "I":
                addto_inventory(room.item)

            elif user_input == "B":
                go_back(room.name)

            elif user_input == "V":
                view_inventory()

            elif user_input == "L":
                user_controls()

            elif user_input == "C":
                check_visited_rooms()

            elif user_input == "R":
                restart_game()
                
            elif user_input == "X":
                exit_game()

class Game:
    def __init__(self, startRoom):
        self.start = startRoom

    def play(gamePlay):

        if gamePlay.start == "room1":
            room1 = Room("room1", room1_items, 2, 0, 0, 0)
            room1.current_room()

        elif gamePlay.start == "room2":
            room2 = Room("room2", room2_items, 0, 3, 1, 0)
            room2.current_room()

        elif gamePlay.start == "room3":
            room3 = Room("room3", room3_items, 6, 4, 0, 2)
            room3.current_room()

        elif gamePlay.start == "room4":
            room4 = Room("room4", room4_items, 7, 5, 0, 3)
            room4.current_room()

        elif gamePlay.start == "room5":
            room5 = Room("room5", room5_items, 0, 0, 0, 4)
            room5.current_room()

        elif gamePlay.start == "room6":
            room6 = Room("room6", room6_items, 9, 7, 3, 0)
            room6.current_room()

        elif gamePlay.start == "room7":
            room7 = Room("room7", room7_items, 10, 0, 4, 6)
            room7.current_room()

        elif gamePlay.start == "room8":
            room8 = Room("room8", room8_items, 0, 9, 0, 0)
            room8.current_room()

        elif gamePlay.start == "room9":
            room9 = Room("room9", room9_items, 0, 10, 6, 8)
            room9.current_room()

        elif gamePlay.start == "room10":
            room10 = Room("room10", room10_items, 0, 11, 7, 9)
            room10.current_room()

        elif gamePlay.start == "room11":
            room11 = Room("room11", room11_items, 12, 0, 0, 10)
            room11.current_room()

        else:
            gamePlay.start == "room12"
            room12 = Room("room12", room12_items, 0, 0, 11, 0)
            room12.current_room()

# =================================== main ===================================
def main():
    print("-----------------------------------------------------------------------------------")
    print("                               Adventure game!")
    print("-----------------------------------------------------------------------------------")
    print("*  You can start from any room you want. For example in the first prompt type 'room1'\nto start in room 1 or 'room12' to start in room 12")
    print("*  By using the buttons 'N', 'S', 'E', 'W' in your keyboard you can move to the next\nroom.")
    print("*  After moving to a new room you can click the button 'B' to travel back to the\nprevious room.")
    print("*  While inside the room you can click the button 'O' to Observe the room.")
    print("*  Once investigating the room you will get a list of Items inside the room.")
    print("*  You can click 'I' to take items from the room to users inventory.")
    print("*  If you forget the controls you can click 'I' to view the user controls again.")
    print("*  You can click 'R' to restart the game again.")
    print("*  You can click 'C' to check visited rooms.")
    print("*  If want to quit you can click 'X'.")
    print("-----------------------------------------------------------------------------------")

    while True:
        player_name = Player(input("Enter your name : "))
        start_room = input("Enter the first room you want to enter : ")
        if start_room in all_rooms:
            print("*  "+player_name.name + " , You are about to start the game.")
            print("----------------------------------------------------")
            user_controls()
            g = Game(start_room)
            g.play()
        else:
            print("*  Wrong room name. Try again !\n(room1,room2,room3,room4,room5,room6,room7,room8,room9,room10,room11,room12)")
        print("----------------------------------------------------")

if __name__=="__main__":
    main()
