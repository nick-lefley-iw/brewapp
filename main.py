import sys
people = ["Alice", "Bob", "Carol"]
drinks = ["tea", "coffee", "water"]


def get_people():
    print(people)

def get_drinks():
    print(drinks)

def reject_input():
    print("Unexpected command, try get-people or get-drinks")

for i in range(1,len(sys.argv)):
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