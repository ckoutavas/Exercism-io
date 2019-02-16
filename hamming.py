def distance(strand_a, strand_b):
    count = 0
    a = list(strand_a)
    b = list(strand_b)
    
    if len(a) != len(b):
        raise ValueError(f'Strings must be the same lenght: strand_a is {len(a)} and strand_b is {len(b)}')
    
    for i in range(len(a)):
        if a[i] == b[i]:
            pass
        else:
            count+=1
    return count
