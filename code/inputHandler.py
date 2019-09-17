def get_input(request):
    return input(request).strip()

def get_input_as_string(user_input):
    try:
        user_input = str(user_input)
    except:
        print("Please enter a valid string.")
        return


def get_input_as_integer(user_input):
    try:
        user_input = int(user_input)
    except:
        print("Please enter a valid integer.")
        return


def get_input_as_list(user_input, separator: str):
    try:
        user_input = user_input.split(separator)
    except:
        print("Please enter a valid list.")
