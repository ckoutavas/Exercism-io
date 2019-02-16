import string

def word_count(phrase):
    phrase = phrase.replace(',', ' ').replace('_', ' ')
    valid_pun = string.punctuation.replace("'", '')
    phrase = ''.join([c for c in phrase if c not in valid_pun])
    word_list = phrase.lower().split()
    d = dict()
    
    for word in word_list:
        if word[0] == "'" and word[-1] == "'":
            clean_word = word[1:-1]
            update(clean_word, d)
        else:
            update(word, d)        
    return d

def update(k, d):
    if k in d:
        d[k]+=1
    else:
        d[k]=1
