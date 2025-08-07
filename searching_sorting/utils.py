def read_number_from_file(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
    return[int(line.strip())for line in lines]