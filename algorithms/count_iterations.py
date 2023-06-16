def count_repetitions(string):
    repetitions = {}
    for char in string:
        if char == " ":
            continue
        if char in repetitions:
            repetitions[char] += 1
        else:
            repetitions[char] = 1
    return repetitions

input_string = "hello world"
result = count_repetitions(input_string)
print(result)
