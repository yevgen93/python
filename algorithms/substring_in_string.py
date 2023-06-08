def count_substring(string, sub_string):
    count = 0
    l = len(sub_string)
    for i in range(0, len(string)):
        if string[i:l] == sub_string:
            count += 1
        l += 1
    return count

print(count_substring("ABCDCDC", "CDC"))
