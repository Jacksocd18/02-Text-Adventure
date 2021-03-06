#!/usr/bin/env python3
import sys, os, json
# Check to make sure we are running the correct version of Python
assert sys.version_info >= (3,7), "This script requires at least Python 3.7"

# The game and item description files (in the same folder as this script)
game_file = 'game.json'
item_file = 'items.json'
inventory = []
points = 0
moves = 0



# Load the contents of the files into the game and items dictionaries. You can largely ignore this
# Sorry it's messy, I'm trying to account for any potential craziness with the file location
def load_files():
    try:
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        with open(os.path.join(__location__, game_file)) as json_file: game = json.load(json_file)
        with open(os.path.join(__location__, item_file)) as json_file: items = json.load(json_file)
        return (game,items)
    except:
        print("There was a problem reading either the game or item file.")
        os._exit(1)


def check_inventory(item):
    for i in inventory:
        if i == item:
            return True
    return False


def calculate_points(items):
    points = 0
    for i in inventory:
        if i in items:
            points += items[i]["points"]
    return points


def render(game,items,current,moves,points):
    c = game[current]
    print("\n\n{} Moves\t\t\t\t{} Points".format(moves, points))
    print("\nYou are at the" + c["name"])
    print(c["desc"])

    #display any items
    for item in c["items"]:
        if not check_inventory(item["item"]):
            print(item["desc"])

    #display item information
    for i in inventory:
        if i in items:
            if current in items[i]["exits"]:
                print(items[i]["exits"][current])

    print("\nAvailable exits: ")
    for e in c["exits"]:
        print(e["exit"].lower())



def get_input():
    response = input("\nWhat would you like to do?")
    response = response.upper().strip()
    return response

def update(game,items,current,response):
    if response == "INVENTORY":
        print("You are carrying:")
        if len(inventory) == 0:
            print("Nothing")
    else:
        for i in inventory:
            print(i.lower())
        return current


    c = came[current]
    for e in c["exits"]
        if response == e["exit"]:
            return e["target"]


     for item in c["items"]:
        if response == "GET" + item["item"] and not check_inventory(item["item"]):
            print(item["take"])
            inventory.append(item["item"])
            return current

    for i in inventory:
        if i in items:
            for actionin items[i]("actions"):
                if response == action + "" +i:
                    print(items[i]["actions"][action])
                    return current
        # To do: verb object direct-object

    if response[0:3] "GET":
        prinnt("You can't take that!")
    elif response in ["NORTH","SOUTH","WEST","EAST","NW","NE","SW","SE","UP","DOWN"]:
        print("You can't go that way")
    else:
        print("I don't understand what your trying to do")

    return current




# The main function for the game
def main():
    current = 'BEDROOM'  # The starting location
    end_game = ['OUTSIDE']  # Any of the end-game locations
    moves = 0
    points = 0

    (game,items) = load_files()


    while True:
        render(game,items,current,moves,points)


        for e in end_game:
            if current == e:
                print("You win!")
                break #break out of the loop


        response = get_input()


        if response == "QUIT" or response == "Q":
            break #break out of the while loop


        current = update(game,current,response)
        moves += 1
        points = calculate_points{items}

    print("Thanks for playing!")
    print("You sored {} points in {} moves". format(points,moves))

# run the main function
if __name__ == '__main__':
	main()