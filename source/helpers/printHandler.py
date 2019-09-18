from prettytable import PrettyTable

def pretty_print_table(header, data):
    x = PrettyTable()

    x.field_names = header
    for row in data:
        x.add_row(row)

    print(x)