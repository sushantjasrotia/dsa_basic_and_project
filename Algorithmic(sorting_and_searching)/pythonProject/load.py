def load_numbers(numbers_sort):
    numbers = [ ]  # Initial hardcoded numbers
    try:
        with open(numbers_sort) as f:
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
