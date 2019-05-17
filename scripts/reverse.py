def reverse(str):
    final = []
    n = (len(str)-1)
    while n > -1:
        final.append(str[n])
        n = n - 1
    return ''.join(final)

print(reverse('cat'))
