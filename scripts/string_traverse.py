def trav(string):
    count = 1
    final = ""
    for x in range(0, len(string)-1):
        if string[x] == string[x+1]:
            count += 1
    final += string[0] + str(count)
    return final


def maps(string):
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


print trav("AAAAA")
print maps("AAAABBBCCD")
