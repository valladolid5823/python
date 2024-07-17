import os

def replace_string_in_file(file_path, old_string, new_string):
    # Check if the file exists
    if not os.path.isfile(file_path):
        print(f"The file {file_path} does not exist.")
        return

    temp_file_path = file_path + '.tmp'

    # Open the original file for reading and a temporary file for writing
    with open(file_path, 'r', encoding='utf-8') as file, open(temp_file_path, 'w', encoding='utf-8') as temp_file:
        for line in file:
            # Replace the old string with the new string in each line
            new_line = line.replace(old_string, new_string)
            temp_file.write(new_line)

    # Replace the original file with the modified temporary file
    os.replace(temp_file_path, file_path)
    print(f"Replaced all instances of '{old_string}' with '{new_string}' in {file_path}.")

# Usage example
sql_file_path = 'iiq.sql'  # Replace with your .sql file path
replace_string_in_file(sql_file_path, 'utf8mb4_0900_ai_ci', 'utf8mb4_general_ci')
