class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string

    def row(self, index):
        m = [list(map(int, x.replace(' ', ',').split(','))) for x in self.matrix_string.split('\n')]
        return m[index-1]
        

    def column(self, index):
        m = [list(map(int, x.replace(' ', ',').split(','))) for x in self.matrix_string.split('\n')]
        return [m[r][index-1] for r in range(len(m))]
