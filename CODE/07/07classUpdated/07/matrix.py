class MatrixGenerator:

    def __init__(self, n):
        self.numbers = range(1, n * n + 1)
        self.n = n
         # self.numbers = map(lambda x: x + 1, range(n * n))
    #     self.numbers = map(self.add_one, range(n * n))

    # def add_one(self, n):
    #     return n + 1

    def __str__(self):
        pass




    def generate_matrix(self):
        matrix = self.generate_zero_filled_matrix()

        matrix = self.fill_matrix(matrix)

        return matrix

    

    def fill_matrix(self, matrix):
        row = 0
        column = 0
        for item in self.numbers:
            matrix[row][column] = item
#            row, column = self.next_position(row, column)
            row, column = self.next_position_espiral(row, column)

        return matrix


    def generate_zero_filled_matrix(self):
        return [[0] * self.n for x in range(self.n)]

    def can_fill_top_right_cell(self, row, column):
        return row - 1 >= 0 and column + 1 < self.n

    def can_fill_bottom_left_cell(self, row, column):
        return row + 1 < self.n and column - 1 >= 0

    def can_fill_right_cell(self, row, column):
        return column + 1 >= 0
            # column = column + 1
            # return row, column

    def can_fill_bottom_cell(self, row, column):
        return row +1 >= 0
            # row = row +1
            # return row, column

    def can_fill_left_cell(self, row, column):
        return column - 1 >= 0

    def next_position(self, row, col):
        if (self.can_fill_top_right_cell(row, col)):
            return row - 1, col + 1
        else:
            row = row + 1
            while(self.can_fill_bottom_left_cell(row, col)):
                row = row + 1
                col = col - 1
            return row, col

        return matrix

    def next_position_espiral(self, row, col):
        if (self.can_fill_right_cell(row, col)):
            return self.row , self.col + 1
        else:
            row = row + 1
            while(self.can_fill_bottom_cell(row, col)):
                row = row + 1
            return row, col
            while (not self.can_fill_bottom_cell(row,col) and not self.can_fill_right_cell(row, col)):
                
                if (self.can_fill_left_cell(row, col)):
                    col = col - 1
                else:
                    row = row -1


            return row , col


        return matrix
