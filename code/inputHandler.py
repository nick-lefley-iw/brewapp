import sys


def get_input(request):
    return input(request).strip()


def get_input_as_string(user_input):
    try:
        user_input = str(user_input)
        return user_input
    except:
        print("Please enter a valid string.")
        return


def get_input_as_integer(user_input, max=None, min=0):
    try:
        user_input = int(user_input)
        if max:
            if user_input <= max and user_input >= min:
                return user_input
            else:
                print("Please enter an integer within the limits.")
        else:
            return user_input
    except:
        print("Please enter a valid integer.")
        return


def get_input_as_list(user_input, separator: str):
    try:
        user_input = user_input.split(separator)
        return user_input
    except:
        print("Please enter a valid list.")


def reject_input():
    print("Invalid input")


def check_for_cli_args():
    args = []
    for i in range(1, len(sys.argv)):
        if sys.argv[i]:
            args.append(sys.argv[i])
        else:
            if i == 1:
                reject_input()
                exit()
            else:
                exit()
    return args

def get_confirmation_from_input(user_input):

