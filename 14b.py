def add_string_to_file_append(file_path, string_to_add):
    try:
        with open(file_path, 'a') as file:
            file.write(string_to_add + '\n')  # Adding a newline after the string
        print("String added to the file successfully!")
    except IOError:
        print("Error: File not accessible or does not exist.")

# Usage example:
file_path = 'names.txt'  # Replace with your file path
string_to_add = "This is the string I want to add."
num = int (3)
for i in range(3):
    name = input(f"Enter name {i + 1}: ")
    add_string_to_file_append(file_path, name)

add_string_to_file_append(file_path, "try")
