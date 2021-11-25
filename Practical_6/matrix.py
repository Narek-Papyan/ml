class Matrix:
    def __init__(self, *args, **kwargs):
        """
        Takes 2 keyword arguments: filename or list. If filename is given
        read the matrix from file. Else, read it directly from list.
        """
        if 'filename' in kwargs:
            self.read_from_file(kwargs['filename'])
        elif 'list' in kwargs:
            self.read_as_list(kwargs['list'])

    def read_as_list(self, matrix_list):
        if len(matrix_list) == 0:
            self._matrix = []
            self._columns = 0
            self._rows = 0
            return

        columns_count_0 = len(matrix_list[0])
        if not all(len(row) == columns_count_0 for row in matrix_list):
            raise ValueError('Got incorrect matrix')

        self._matrix = matrix_list
        self._rows = len(self._matrix)
        self._columns = columns_count_0

    def read_from_file(self, filename):
        with open(filename, 'r') as f:
            matrix_list = f.readlines()
        matrix_list = list(map(lambda s: list(map(float, s[:-1].split(' '))), matrix_list))
        self.read_as_list(matrix_list)

    def __str__(self):
        s = '---------MATRIX---------\n'
        s += '\n'.join(str(row) for row in self._matrix)
        s += '\n'
        s += f'colums = {self.shape[0]}\nrows = {self.shape[1]}'
        s += '\n------------------------\n'
        return s

    def write_to_file(self, filename):
        with open('filename', 'w') as file:
            array = file.write(matrix_list)
            return array
    
    def traspose(self):
        output = []
        for i in range(0, len(self._matrix[0])):
            output_raw = []
            for j in range(0, len(self._matrix)):
                output_raw.append(self._matrix[j][i])
            output.append(output_raw)
        return output

    @property
    def shape(self):
        return self._columns, self._rows

    def __add__(self, other):
        if shape(other) != shape(self._matrix):
            return self._matrix
        else:
            #c = self._matrix
            for i in range(self._rows):
                for j in range(len(self._columns)):
                    self._matrix[i][j] += other[i][j]
            return c

    def __mul__(self, other):
        c = self._matrix
        for i in range(self._row):
            for j in range(self._columns):
                c[i][j] = self._matrix[i][j] * other[i][j]
            return c


    def __matmul__(self, other):
        if columna != rowb:
            return self._matrix
        else:
            c = []
            for i in range(self._row):
                c_row = []
                for j in range(self._columns):
                    value = 0
                    for k in range(len(other[0])):
                        value += a[i][k] * b[k][j]
                    c_row.append(value)
                c.append(c_row)
            return c


    @property
    def trace(self):
        sum = 0
        for i in len(self._matrix):
            sum += self._matrix[i][i]
        return sum

    @property
    def determinant(self):
        def MatrixMinor(m,i,j):
            return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

    def MatrixDeternminant(m):
        if len(m) == 2:
            return m[0][0]*m[1][1]-m[0][1]*m[1][0]
        determinant = 0
        for c in range(len(m)):
            determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(MatrixMinor(m,0,c))
        return determinant

