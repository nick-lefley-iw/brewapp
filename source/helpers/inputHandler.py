import sys


def get_input(request):
    return input(request).strip()


def get_input_as_string(user_input):
    try:
        user_input = str(user_input)
        return user_input
    except:
        return get_input_as_string(get_input("Please enter a valid string. "))


def get_input_as_integer(user_input, max=None, min=0):
    try:
        user_input = int(user_input)
        if max:
            if max >= user_input >= min:
                return user_input
            else:
                return get_input_as_integer(get_input("Please enter an integer within the limits. "), max, min)
        else:
            return user_input
    except:
        return get_input_as_integer(get_input("Please enter a valid integer. "), max, min)


def get_input_as_list(user_input, separator: str):
    try:
        user_input = user_input.split(separator)
        return user_input
    except:
        return get_input_as_list(get_input("Please enter a valid list. "), separator)


def reject_input():
    print("Invalid input.")


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


def get_confirmation_from_input(user_input, accept=["Y", "YES", "TRUE", True, ], refuse=["N", "NO", "FALSE", False]):
    try:
        user_input = str(user_input).upper()
        if user_input in accept:
            return True
        if user_input in refuse:
            return False
        return get_confirmation_from_input(get_input("Please enter Yes or No. "), accept, refuse)
    except:
        return get_confirmation_from_input(get_input("Please enter Yes or No. "), accept, refuse)
