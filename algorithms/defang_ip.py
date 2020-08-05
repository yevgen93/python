# Given a valid (IPv4) IP address, return a defanged version of that IP address.
# A defanged IP address replaces every period "." with "[.]".
# Example 1:
# Input: address = "1.1.1.1"
# Output: "1[.]1[.]1[.]1"

def defangIPaddr(self, address: str) -> str:
    final = []
    for char in address:
        if char.isdigit():
            final.append(char)
        else:
            final.append("[.]")
    return ''.join(final)
    
# Built in replace function
# return address.replace('.', '[.]')
