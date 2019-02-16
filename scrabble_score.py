def score(word):
    letters = list(word.upper())
    d = dict()
    p1 = list('AEIOULNRST')
    p2 = list('DG')
    p3 = list('BCMP')
    p4 = list('FHVWY')
    p5 = ['K']
    p8 = list('JX')
    p10 = list('QZ')
    
    for l in p1:
        d[l]=1
    for l in p2:
        d[l]=2
    for l in p3:
        d[l]=3
    for l in p4:
        d[l]=4
    for l in p5:
        d[l]=5
    for l in p8:
        d[l]=8
    for l in p10:
        d[l]=10
        
    return sum([d[x] for x in letters])
