import os
import sys

from prettytable import PrettyTable

clear = lambda: os.system('clear')

menu_text = """
Welcome to brew app!

          {
       }   }   {
      {   {  }  }
       }   }{  {
      {  }{  }  }
     ( }{ }{  { )
    .-{   }   }-.
   ( ( } { } { } )
   |`-.._____..-'|
   |             ;--.
   |   (__)     (__  \\
   |   (oo)      | )  )
   |    \/       |/  /
   |             /  /    
   |            (  /
   \             y'
    `-.._____..-'


Please select an option:

    [1] Get a list of people
    [2] Get a list of drinks
    [3] Add person
    [4] Add drink
    [5] Show Favourites
    [6] Add Favourite
    [x] Exit
"""

uid_to_drink = {
    1: "bean juice",
    2: "leaf water",
    3: "water"
}

uid_to_person = {
    1: "Alice",
    2: "Bob",
    3: "Carol"
}

favourites = {
    1: 1,
    2: 2,
    3: 3
}


def get_name_from_uid(type, uid):
    if type == "person":
        mapping = uid_to_person
    elif type == "drink":
        mapping = uid_to_drink

    if mapping[uid]:
        return mapping[uid]
    else:
        return False

def run_session():
    mode = input("Enter your selection here: ")

    clear()

    if mode == "1":
        # get_people()
        get_people_and_id()
    elif mode == "2":
        get_drinks()
    elif mode == "3":
        add_person()
    elif mode == "4":
        add_drink()
    elif mode == "5":
        get_favourites()
    elif mode == "6":
        add_favourite()
    elif mode == "x":
        end_sessions()
    else:
        reject_input()


def end_sessions():
    exit()


def check_for_CLI_args():
    for i in range(1, len(sys.argv)):
        if sys.argv[i]:
            mode = sys.argv[i]
        else:
            if i == 1:
                reject_input()
                exit()
            else:
                exit()

        if mode == "get-people":
            get_people()
        elif mode == "get-drinks":
            get_drinks()
        elif mode == "--help":
            get_help()
        else:
            reject_input()

        wait_after_session()


def wait_after_session():
    selection = input("Would you like to continue? [y/n]").upper()

    if selection == "N":
        end_sessions()
    elif selection != "Y":
        reject_input()


def pretty_print_list(items, item_type):
    max_length = len(max([max(items, key=len), item_type], key=len)) + 4

    divider = "-"
    divider = "+" + divider * (max_length - 2) + "+"

    print(divider)
    header = "| " + item_type + " " * (max_length - 3 - len(item_type)) + "|"
    print(header)
    print(divider)

    for item in items:
        item_to_print = "| " + item + " " * (max_length - 3 - len(item)) + "|"
        print(item_to_print)
    print(divider)


def pretty_print_table(headers, data):
    x = PrettyTable()

    x.field_names = headers
    for row in data:
        x.add_row(row)

    print(x)


def add_person():
    new_entry = input("Please enter the new person's name: ").title()
    uid_to_person[max(uid_to_person.keys()) + 1] = new_entry


def get_people():
    pretty_print_list(uid_to_person.values(), 'People Names')


def get_people_and_id():
    headers = ["People", "UID"]
    data = []
    for uid in uid_to_person:
        name = uid_to_person[uid]
        data.append([name, uid])
    pretty_print_table(headers, data)


def add_drink():
    new_entry = input("Please enter the new drink name: ").title()
    uid_to_drink[max(uid_to_drink.keys()) + 1] = new_entry


def get_drinks():
    pretty_print_list(uid_to_drink.values(), 'Drinks Names')


def get_favourites():
    headers = ["People", "UID", "Favourite Drink"]
    data = []
    for uid in uid_to_person:
        name = uid_to_person[uid]
        try:
            data.append([name, uid, get_name_from_uid("drink", favourites[uid])])
        except:
            data.append([name, uid, "N/A"])
    pretty_print_table(headers, data)


def add_favourite():
    uid = int(input("Please enter the UID of the person: "))
    if uid not in uid_to_person.keys():
        reject_favourite()
    drink = int(input("Please enter the UID of their favourite drink: "))
    if drink not in uid_to_drink.keys():
        reject_favourite()

    favourites[uid] = drink





def reject_input():
    print("Unexpected command, please see the menu list or run again with --help")


def reject_favourite():
    print("Invalid input to create a favourite")

def get_help():
    help_text = """
    Comand Line Arguments:
    
    get-people - Prints a list of people stored
    get-drinks - Prints a list of drinks stored
    """


check_for_CLI_args()
while True:
    clear()
    print(menu_text)
    run_session()
    wait_after_session()
    clear()
