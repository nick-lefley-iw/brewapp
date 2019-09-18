#!/usr/bin/env python3

import os

from helpers import fileHandler, inputHandler, printHandler, devito as danny
from classes.Drink import Drink
from classes.Person import Person
from classes.Round import Round
from helpers.printHandler import pretty_print_table

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

    [P] Get a list of people
    [D] Get a list of drinks
    [P+] Add person
    [D+] Add drink
    [P-] Remove person
    [D-] Remove drink
    [R] Start Round
    [LR] Load last round
    [X] Exit
"""


def run_session(mode, drinks, people):
    clear()
    if mode == "P":
        show_people(people)
    elif mode == "D":
        show_drinks(drinks)
    elif mode == "P+":
        people = add_person(people, drinks)
    elif mode == "D+":
        drinks = add_drink(drinks)
    elif mode == "P-":
        people = remove_person(people)
    elif mode == "D-":
        drinks = remove_drink(drinks, people)
    elif mode == "R":
        start_round(people)
    elif mode == "LR":
        load_round("store/", "lastround")
    elif mode == "X":
        end_sessions()
    elif mode == "DEVITO":
        print(danny.devito_time())
    else:
        inputHandler.reject_input()

    return [drinks, people]


def end_sessions():
    exit()


def start_round(people):
    show_people(people)

    maker_id_prompt = "Please enter the UID of the round's maker: "
    maker_id = inputHandler.get_input_as_integer(inputHandler.get_input(maker_id_prompt))
    people_id_prompt = "Please enter the ids of the people who want a drink, separated by comma: "
    people_id_list = inputHandler.get_input_as_list(inputHandler.get_input(people_id_prompt), ",")

    people_list = []
    for people_id in people_id_list:
        people_list.append(get_person(people, int(people_id)))
    new_round = Round(get_person(people, maker_id), people_list)
    new_round.print_round()
    fileHandler.pickle_variable("store/", "lastround", new_round)


def load_round(path, file):
    round = fileHandler.unpickle(path, file)
    if round:
        return round
    else:
        print("No round saved to a file.")



def wait_after_session():
    confirm_prompt = "Would you like to continue? [y/n]"
    selection = inputHandler.get_confirmation_from_input(inputHandler.get_input(confirm_prompt))

    if not selection:
        end_sessions()
    return


def show_people(people):
    header = ["UID", "Name", "Favourite Drink"]
    data = []
    for index, person in enumerate(people):
        data.append([index, person.get_name(), person.get_favourite()])
    pretty_print_table(header, data)


def show_drinks(drinks):
    header = ["UID", "Name", "Temperature"]
    data = []
    for index, drink in enumerate(drinks):
        data.append([index, drink.get_name(), drink.get_temperature()])
    pretty_print_table(header, data)


def get_person(people, uid):
    return people[uid]


def get_drink(drinks, uid):
    if drinks[uid]:
        return drinks[uid]
    else:
        return None


def add_person(people, drinks):
    if len(drinks) == 0:
        print("Please enter at least one drink before adding a person")
        return people
    show_people(people)
    first_name = input("Please enter the new person's first name: ")
    surname = input("Please enter the new person's surname: ")
    show_drinks(drinks)
    favourite = int(input("Please enter the ID of their preferred drink: "))

    new_person = Person(first_name, surname, get_drink(drinks, favourite))

    people.append(new_person)
    fileHandler.pickle_variable("store/", "people", people)
    return people


def add_drink(drinks):
    show_drinks(drinks)
    name = input("Please enter the new drink name: ")
    temperature = input("Please enter the temperature of the new drink: ")

    new_drink = Drink(name, temperature)
    drinks.append(new_drink)
    fileHandler.pickle_variable("store/", "drinks", drinks)
    return drinks


def remove_person(people):
    show_people(people)
    uid = int(input("Please enter the UID of the person to be deleted: "))
    person = get_person(people, uid)
    confirm = input(f"This will delete {person}, are you sure you want to continue deletion? [y/n]").upper()

    if confirm == "Y":
        del people[uid]
        return people
    else:
        return


def remove_drink(drinks, people):
    show_drinks(drinks)
    uid = int(input("Please enter the UID of the drink to be deleted: "))
    drink = get_drink(drinks, uid)
    if is_favourite(drink, people):
        print(f"{drink} is someone's favourite drink, please don't delete it.")
    else:
        confirm = input(f"This will delete {drink}, are you sure you want to continue deletion? [y/n]").upper()

        if confirm == "Y":
            del drinks[uid]
    return drinks


def is_favourite(drink, people):
    for person in people:
        if person.get_favourite() == drink:
            return True

    return False


def run_cli_args(args):
    for instruction in args:
        if instruction == "get-people":
            show_people()
        elif instruction == "get-drinks":
            show_drinks()
        elif instruction == "--help":
            get_help()
        else:
            inputHandler.reject_input()


def get_help():
    help_text = """
    Comand Line Arguments:
    
    get-people - Prints a list of people stored
    get-drinks - Prints a list of drinks stored
    """


if __name__ == '__main__':
    drink_list = fileHandler.unpickle_list("store/", "drinks")
    people_list = fileHandler.unpickle_list("store/", "people")


    args = inputHandler.check_for_cli_args()
    if args:
        run_cli_args(args)

    while True:
        clear()
        print(menu_text)
        updated_lists = run_session(input("Enter your selection here: ").upper(), drink_list, people_list)
        drink_list = updated_lists[0]
        people_list = updated_lists[1]
        wait_after_session()
        clear()
