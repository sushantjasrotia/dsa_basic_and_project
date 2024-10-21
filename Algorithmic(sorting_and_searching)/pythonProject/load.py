def load_numbers(numbers_sort):
    numbers = [ ]  # Initial hardcoded numbers
    try: #it is used to handle exception if error occur or anything goes wrong
        with open(numbers_sort) as f: #open file and assign variable f and with it auto close the file when the block is exited
            for line in f:
                numbers.append(int(line.strip()))  # Convert each line to an integer
        print("Numbers loaded:", numbers)
    except FileNotFoundError:
        print(f"Error: File '{numbers_sort}' not found.")
    except ValueError:
        print(f"Error: Invalid number found in the file '{numbers_sort}'.")

    return numbers

def load_strings(file_name):
    strings = []
    with open(file_name) as f:
        for line in f:
            cleaned_string = line.strip()  # Remove leading/trailing whitespaces
            print(f"Loaded string: '{cleaned_string}'")  # Debugging: Print each loaded line
            strings.append(cleaned_string)
    return strings
