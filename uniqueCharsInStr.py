'''
Given a string, are all chars unique?
return boolean
'''

def unique(string):
    string = string.replace(' ', '')
    return len(set(string)) == len(string)


def unique2(s):
    s = s.replace(" ", "")
    characters = set()

    for letter in s:
        if letter in characters:
            return False
        else:
            characters.add(letter)
    return True