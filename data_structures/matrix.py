class Matrix:
    def __init__(self, rows, cols, default_value=0):
        self.rows = rows
        self.cols = cols
        self.data = [[default_value for _ in range(cols)] for _ in range(rows)]
        
    def len(self):
        if self.rows == 1:
            return self.cols
        return (self.rows, self.cols)

    def get(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.data[row][col]
        else:
            raise IndexError("Index out of bounds")

    def set(self, row, col, value):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.data[row][col] = value
        else:
            raise IndexError("Index out of bounds")
        
    def is_empty(self):
        return self.rows == 0 or self.cols == 0
    
    def __bool__(self):
        return not self.is_empty()
    
    def __getitem__(self, pidx, sidx=None):
        if pidx<0 or pidx>=self.rows or (sidx is not None and (sidx<0 or sidx>=self.cols)):
            raise IndexError("Index out of bounds")
        if sidx is None:
            return self.data[pidx]
        return self.data[pidx][sidx]
    
    def __setitem__(self, pidx, sidx, value):
        if pidx<0 or pidx>=self.rows or (sidx is not None and (sidx<0 or sidx>=self.cols)):
            raise IndexError("Index out of bounds")
        if sidx is None:
            self.data[pidx] = value
        else:
            self.data[pidx][sidx] = value
            
    def add_row(self, values=None):
        if values is None:
            values = [0] * self.cols
        elif len(values) != self.cols:
            raise ValueError("Row length must match number of columns")
        self.data.append(values)
        self.rows += 1
        
    def add_column(self, values=None):
        if values is None:
            values = [0] * self.rows
        elif len(values) != self.rows:
            raise ValueError("Column length must match number of rows")
        for i in range(self.rows):
            self.data[i].append(values[i])
        self.cols += 1

    def zero(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] = 0

    def identity(self):
        if self.rows != self.cols:
            raise ValueError("Identity matrix must be square")
        self.zero()
        for i in range(self.rows):
            self.data[i][i] = 1

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

    def transpose(self):
        transposed = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                transposed.set(j, i, self.get(i, j))
        return transposed
    
    def add(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions to add")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.set(i, j, self.get(i, j) + other.get(i, j))
        return result
    
    def subtract(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions to subtract")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.set(i, j, self.get(i, j) - other.get(i, j))
        return result
    
    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError("Incompatible dimensions for multiplication")
        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                sum_product = 0
                for k in range(self.cols):
                    sum_product += self.get(i, k) * other.get(k, j)
                result.set(i, j, sum_product)
        return result
    
    def submatrix(self, row_start, col_start, row_end=None, col_end=None):
        if row_end == None:
            row_end = self.rows
        if col_end == None:
            col_end = self.cols
        if row_start < 0 or row_end > self.rows or col_start < 0 or col_end > self.cols:
            raise IndexError("Submatrix indices out of bounds")
        sub = Matrix(row_end - row_start, col_end - col_start)
        for i in range(row_start, row_end):
            for j in range(col_start, col_end):
                sub.set(i - row_start, j - col_start, self.get(i, j))
        return sub
    
    def set_submatrix(self, row_start, row_end, col_start, col_end, sub):
        if row_start < 0 or row_end > self.rows or col_start < 0 or col_end > self.cols:
            raise IndexError("Submatrix indices out of bounds")
        if (row_end - row_start != sub.rows) or (col_end - col_start != sub.cols):
            raise ValueError("Submatrix dimensions do not match")
        for i in range(row_start, row_end):
            for j in range(col_start, col_end):
                self.set(i, j, sub.get(i - row_start, j - col_start))
    
    
    # Strassen's matrix multiplication
    def strassen_multiply(self, other):
        if self.rows != self.cols or other.rows != other.cols or self.rows != other.rows:  # only for square matrices of same size
            raise ValueError("Strassen's algorithm requires square matrices of the same size")
        n = self.rows
        if n == 1:
            return Matrix(1, 1, self.get(0, 0) * other.get(0, 0))
        else:
            mid = n // 2
            A11 = self.submatrix(0, mid, 0, mid)
            A12 = self.submatrix(0, mid, mid, n)
            A21 = self.submatrix(mid, n, 0, mid)
            A22 = self.submatrix(mid, n, mid, n)

            B11 = other.submatrix(0, mid, 0, mid)
            B12 = other.submatrix(0, mid, mid, n)
            B21 = other.submatrix(mid, n, 0, mid)
            B22 = other.submatrix(mid, n, mid, n)

            P = (A11.add(A22)).strassen_multiply(B11.add(B22))
            Q = (A21.add(A22)).strassen_multiply(B11)
            R = A11.strassen_multiply(B12.subtract(B22))
            S = A22.strassen_multiply(B21.subtract(B11))
            T = (A11.add(A12)).strassen_multiply(B22)
            U = (A21.subtract(A11)).strassen_multiply(B11.add(B12))
            V = (A12.subtract(A22)).strassen_multiply(B21.add(B22))

            C11 = P.add(S).subtract(T).add(V)
            C12 = R.add(T)
            C21 = Q.add(S)
            C22 = P.subtract(Q).add(R).add(U)

            result = Matrix(n, n)
            result.set_submatrix(0, mid, 0, mid, C11)
            result.set_submatrix(0, mid, mid, n, C12)
            result.set_submatrix(mid, n, 0, mid, C21)
            result.set_submatrix(mid, n, mid, n, C22)

            return result
        
        
