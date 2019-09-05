import sys
people = ["Alice", "Bob", "Carol"]
drinks = ["tea", "coffee", "water"]


def get_people():
    print(people)

def get_drinks():
    print(drinks)

def reject_input():
    print("Unexpected command, try get-people or get-drinks")


if sys.argv[1]:
    mode = sys.argv[1]
else:
    reject_input()
    exit()

if mode == "get-people":
    get_people()
elif mode == "get-drinks":
    get_drinks()
else:
    reject_input()