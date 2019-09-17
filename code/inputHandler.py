def get_input_as_string(user_input):
    try:
        user_input = str(user_input)
    except:
        print("Please enter a valid string.")
        return