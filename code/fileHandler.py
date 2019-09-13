def file_to_dict(filename):
    try:
        f = open(filename, "r")
        file = f.read().split("\n")
    except FileNotFoundError as e:
        print("File not found:" + str(e))
    finally:
        f.close()

    return process_file_to_dict(filename, file)


def process_file_to_dict(filename, file):
    dictionary = {}
    for pair in file:
        pair = pair.split(',')
        if "favourites" in filename:
            dictionary[int(pair[0])] = int(pair[1])
        else:
            dictionary[int(pair[0])] = pair[1]
    return dictionary


def add_to_dict_file(filename, uid, value):
    try:
        f = open(filename, "a")
        f.write(format_for_file(uid, value))
    except FileNotFoundError as e:
        print("File not found:" + str(e))
    finally:
        f.close()


def format_for_file(uid, value):
    return f"\n{uid},{value}"

