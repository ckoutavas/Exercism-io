import string

def abbreviate(words):
    t = str.maketrans('', '', string.punctuation)
    words = words.replace('-',' ')
    words = words.translate(t).split()
    l = [w[0].upper() for w in words]
    return ''.join(l)
