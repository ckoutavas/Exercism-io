import string

def is_isogram(s):
    alpha = string.ascii_lowercase
    s = s.lower()
    l = list(s.replace('-', '').replace(' ', ''))
    print(l)
    if len(set(l)) == len(l):
        return True
    else:
        return False
