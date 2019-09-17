import os
import pickle


def check_for_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


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


def unpickle(path, file):
    check_for_dir(path)
    path = f"{path}{file}.pickle"
    if os.path.exists(path):
        return pickle.load(open(path, "rb"))
    else:
        return False


def pickle_variable(path, file, variable):
    pickle.dump(variable, open(f"{path}{file}.pickle", "wb"))
