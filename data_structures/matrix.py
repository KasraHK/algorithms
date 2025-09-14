"""Matrix data structure utilities.

Provides a lightweight 2D matrix with helpers for vector operations, sorting,
basic arithmetic, submatrix operations, and Strassen multiplication.
"""


class Matrix:
    """Simple row-major matrix.

    Use rows=1 to represent vectors. The implementation avoids external libs
    and is intended for educational purposes and algorithm demos.
    """

    def __init__(self, rows, cols, default_value=0):
        self.rows = rows
        self.cols = cols
        self.data = [[default_value for _ in range(cols)] for _ in range(rows)]
        
    def len(self):
        """Return length for vectors or (rows, cols) for matrices."""
        if self.rows == 1:
            return self.cols
        return (self.rows, self.cols)

    def get(self, row, col):
        """Get value at (row, col). Raises IndexError if out of bounds."""
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.data[row][col]
        else:
            raise IndexError("Index out of bounds")

    def set(self, row, col, value):
        """Set value at (row, col). Raises IndexError if out of bounds."""
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.data[row][col] = value
        else:
            raise IndexError("Index out of bounds")
        
    def is_empty(self):
        """Return True if matrix has zero rows or zero cols."""
        return self.rows == 0 or self.cols == 0
    
    def __bool__(self):
        """Truthiness: empty matrices are False, others True."""
        return not self.is_empty()
    
    def __getitem__(self, pidx, sidx=None):
        """Get element at (row, col) or entire row.
        
        Args:
            pidx: row index
            sidx: column index (optional, if None returns entire row)
            
        Returns:
            Element at (pidx, sidx) or list representing row pidx
        """
        if pidx<0 or pidx>=self.rows or (sidx is not None and (sidx<0 or sidx>=self.cols)):
            raise IndexError("Index out of bounds")
        if sidx is None:
            return self.data[pidx]
        return self.data[pidx][sidx]
    
    def __setitem__(self, pidx, sidx, value):
        """Set element at (row, col) or entire row.
        
        Args:
            pidx: row index
            sidx: column index (optional, if None sets entire row)
            value: value to set (single value or list for entire row)
        """
        if pidx<0 or pidx>=self.rows or (sidx is not None and (sidx<0 or sidx>=self.cols)):
            raise IndexError("Index out of bounds")
        if sidx is None:
            self.data[pidx] = value
        else:
            self.data[pidx][sidx] = value

    # ---- Vector helpers ----
    def _ensure_vector(self):
        if self.rows != 1:
            raise ValueError("Operation valid only for 1xN vector matrices")

    def swap(self, i: int, j: int):
        """Swap two elements in a 1xN vector."""
        self._ensure_vector()
        if not (0 <= i < self.cols and 0 <= j < self.cols):
            raise IndexError("Index out of bounds")
        self.data[0][i], self.data[0][j] = self.data[0][j], self.data[0][i]

    def copy(self):
        """Return a deep copy of the matrix."""
        m = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                m.data[i][j] = self.data[i][j]
        return m
            
    def add_row(self, values=None):
        """Append a row; values defaults to zeros of current column count."""
        if values is None:
            values = [0] * self.cols
        elif len(values) != self.cols:
            raise ValueError("Row length must match number of columns")
        self.data.append(values)
        self.rows += 1
        
    def merge_rows(self, other):
        """Concatenate rows of another matrix with same number of columns."""
        if self.cols != other.cols:
            raise ValueError("Matrices must have the same number of columns to merge rows")
        self.data.extend(other.data)
        self.rows += other.rows
        
    def merge_columns(self, other):
        """Concatenate columns of another matrix with same number of rows."""
        if self.rows != other.rows:
            raise ValueError("Matrices must have the same number of rows to merge columns")
        for i in range(self.rows):
            self.data[i].extend(other.data[i])
        self.cols += other.cols
        
    def add_column(self, values=None):
        """Append a column; values defaults to zeros of current row count."""
        if values is None:
            values = [0] * self.rows
        elif len(values) != self.rows:
            raise ValueError("Column length must match number of rows")
        for i in range(self.rows):
            self.data[i].append(values[i])
        self.cols += 1

    def zero(self):
        """Set all entries to 0."""
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] = 0

    def identity(self):
        """Transform into an identity matrix (must be square)."""
        if self.rows != self.cols:
            raise ValueError("Identity matrix must be square")
        self.zero()
        for i in range(self.rows):
            self.data[i][i] = 1

    def __str__(self):
        """Pretty string representation with space-separated rows."""
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

    def transpose(self):
        """Return the transpose of the matrix as a new Matrix."""
        transposed = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                transposed.set(j, i, self.get(i, j))
        return transposed

    # ---- Sorting for 1xN vectors ----
    def _partition(self, low: int, high: int) -> int:
        self._ensure_vector()
        pivot = self.get(0, high)
        i = low - 1
        for j in range(low, high):
            if self.get(0, j) <= pivot:
                i += 1
                x = self.get(0, i)
                self.set(0, i, self.get(0, j))
                self.set(0, j, x)
        x = self.get(0, i + 1)
        self.set(0, i + 1, self.get(0, high))
        self.set(0, high, x)
        return i + 1

    def quick_sort(self):
        """In-place quicksort for 1xN vector. Uses internal partition."""
        self._ensure_vector()

        def _qs(l, r):
            if l < r:
                p = self._partition(l, r)
                _qs(l, p - 1)
                _qs(p + 1, r)
        _qs(0, self.cols - 1)

    def merge_sort(self):
        """Stable merge sort for 1xN vector (returns new sorted Matrix)."""
        self._ensure_vector()
        if self.cols <= 1:
            return self.copy()

        mid = self.cols // 2
        left = Matrix(1, mid)
        right = Matrix(1, self.cols - mid)
        for i in range(mid):
            left.set(0, i, self.get(0, i))
        for i in range(self.cols - mid):
            right.set(0, i, self.get(0, mid + i))
        left_sorted = left.merge_sort()
        right_sorted = right.merge_sort()

        # merge
        result = Matrix(1, self.cols)
        i = j = k = 0
        while i < left_sorted.cols and j < right_sorted.cols:
            if left_sorted.get(0, i) <= right_sorted.get(0, j):
                result.set(0, k, left_sorted.get(0, i))
                i += 1
            else:
                result.set(0, k, right_sorted.get(0, j))
                j += 1
            k += 1
        while i < left_sorted.cols:
            result.set(0, k, left_sorted.get(0, i))
            i += 1
            k += 1
        while j < right_sorted.cols:
            result.set(0, k, right_sorted.get(0, j))
            j += 1
            k += 1
        return result
    
    def add(self, other):
        """Element-wise addition; returns a new Matrix."""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions to add")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.set(i, j, self.get(i, j) + other.get(i, j))
        return result
    
    def subtract(self, other):
        """Element-wise subtraction; returns a new Matrix."""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions to subtract")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.set(i, j, self.get(i, j) - other.get(i, j))
        return result
    
    def multiply(self, other):
        """Matrix multiplication; returns a new Matrix."""
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
        """Return a copy of the specified submatrix range."""
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
        """Overwrite a region with entries from given submatrix."""
        if row_start < 0 or row_end > self.rows or col_start < 0 or col_end > self.cols:
            raise IndexError("Submatrix indices out of bounds")
        if (row_end - row_start != sub.rows) or (col_end - col_start != sub.cols):
            raise ValueError("Submatrix dimensions do not match")
        for i in range(row_start, row_end):
            for j in range(col_start, col_end):
                self.set(i, j, sub.get(i - row_start, j - col_start))
    
    
    # Strassen's matrix multiplication
    def strassen_multiply(self, other):
        """Strassen's multiplication for same-size square matrices; returns new Matrix."""
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


