import sys

people = ["Alice", "Bob", "Carol"]
drinks = ["Tea", "Coffee", "Water"]

preferences = {"Alice": "Tea",
               "Bob": "Coffee",
               "Carol": "Water"}


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


def get_people():
    pretty_print_list(people, 'People Names')


def get_drinks():
    pretty_print_list(drinks, 'Drinks')


def reject_input():
    print("Unexpected command, try get-people or get-drinks")


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
    else:
        reject_input()
