import re

def count_regex_matches_in_file(file_path, regex_pattern):
    match_count = 0

    with open(file_path, 'r') as file:
        for line in file:
            matches = re.findall(regex_pattern, line)
            match_count += len(matches)
    return match_count

file_path = "regex.txt"
regex_pattern = r'the'
match_count = count_regex_matches_in_file(file_path, regex_pattern)
print("Number of regex matches:", match_count)
