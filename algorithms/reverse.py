def reverse(str):
    final = []
    n = (len(str)-1)
    while n > -1:
        final.append(str[n])
        n -= 1
    return ''.join(final)

print(reverse('cat'))

def reverseString(self, s: List[str]) -> None:
    left = 0
    right = len(s)-1
    while left < right:
        temp = s[left]
        s[left] = s[right]
        s[right] = temp
        left += 1
        right -= 1
    return s
