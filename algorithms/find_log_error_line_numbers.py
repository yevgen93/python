def find_error_line_numbers(file_path):
    error_line_numbers = []
    with open(file_path, 'r') as file:
        for line_number, line in enumerate (file, start=1):
            if "ERROR" in line:
                error_line_numbers.append(line_number)
    return error_line_numbers

file_path = "logfile.txt"
error_line_numbers = find_error_line_numbers(file_path)
print("Line numbers with 'ERROR':", error_line_numbers)

# logfile.txt
# This is a log
# This is a log
# This is an ERROR log
# This is a log
# This is a log
# This is a log
# This is an ERROR log
# This is a log
# This is a log
# This is an ERROR log
# This is a log
