def countLetters(string):
    d = {}
    final = ""
    for x in range(0, len(string)):
        if string[x] not in d.keys():
            d[string[x]] = 1
        elif string[x] in d.keys():
            d[string[x]] += 1
    for key, value in sorted(d.iteritems()):
        final += key + str(value)
    return final

print(countLetters("AAAABBBCCDE"))
