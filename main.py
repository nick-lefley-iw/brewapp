import sys
import os

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
    [x] Exit
"""

people = ["Alice", "Bob", "Carol"]
drinks = ["Tea", "Coffee", "Water"]


def run_session():
    mode = input("Enter your selection here: ")

    clear()

    if mode == "1":
        get_people()
    elif mode == "2":
        get_drinks()
    elif mode == "3":
        add_person()
    elif mode == "4":
        add_drink()
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


def add_person():
    new_entry = input("Please enter the new person's name: ").title()
    people.append(new_entry)


def get_people():
    pretty_print_list(people, 'People Names')


def add_drink():
    new_entry = input("Please enter the new drink name: ").title()
    drinks.append(new_entry)


def get_drinks():
    pretty_print_list(drinks, 'Drinks')


def reject_input():
    print("Unexpected command, please see the menu list or run again with --help")


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
