import random


class SudokuGenerator:
    def __init__(self, removed_cells, row_length=9):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.box_length = 0
        self.board = []

    def get_board(self):
        """
        :return: 2D list of numbers that represents the board
        """
        board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.board = board
        return board

    def get_box(self, start_row, start_col):
        box = []
        if start_row <= 2 and start_col <= 2:
            box = [self.board[0][0], self.board[0][1], self.board[0][2],
                   self.board[1][0], self.board[1][1], self.board[1][2],
                   self.board[2][0], self.board[2][1], self.board[2][2]]
        elif start_row <= 2 and start_col <= 5:
            box = [self.board[0][3], self.board[0][4], self.board[0][5],
                   self.board[1][3], self.board[1][4], self.board[1][5],
                   self.board[2][3], self.board[2][4], self.board[2][5]]
        elif start_row <= 2 and start_col <= 8:
            box = [self.board[0][6], self.board[0][7], self.board[0][8],
                   self.board[1][6], self.board[1][7], self.board[1][8],
                   self.board[2][6], self.board[2][7], self.board[2][8]]
        elif start_row <= 5 and start_col <= 2:
            box = [self.board[3][0], self.board[3][1], self.board[3][2],
                   self.board[4][0], self.board[4][1], self.board[4][2],
                   self.board[5][0], self.board[5][1], self.board[5][2]]
        elif start_row <= 5 and start_col <= 5:
            box = [self.board[3][3], self.board[3][4], self.board[3][5],
                   self.board[4][3], self.board[4][4], self.board[4][5],
                   self.board[5][3], self.board[5][4], self.board[5][5]]
        elif start_row <= 5 and start_col <= 8:
            box = [self.board[3][6], self.board[3][7], self.board[3][8],
                   self.board[4][6], self.board[4][7], self.board[4][8],
                   self.board[5][6], self.board[5][7], self.board[5][8]]
        elif start_row <= 8 and start_col <= 2:
            box = [self.board[6][0], self.board[6][1], self.board[6][2],
                   self.board[7][0], self.board[7][1], self.board[7][2],
                   self.board[8][0], self.board[8][1], self.board[8][2]]
        elif start_row <= 8 and start_col <= 5:
            box = [self.board[6][3], self.board[6][4], self.board[6][5],
                   self.board[7][3], self.board[7][4], self.board[7][5],
                   self.board[8][3], self.board[8][4], self.board[8][5]]
        elif start_row <= 8 and start_col <= 8:
            box = [self.board[6][6], self.board[6][7], self.board[6][8],
                   self.board[7][6], self.board[7][7], self.board[7][8],
                   self.board[8][6], self.board[8][7], self.board[8][8]]
        return box

    def print_board(self):
        """
        :return: void, displays the board to the console
        """
        print(self.board)

    def valid_in_row(self, row, num):
        """
        :param row: row number
        :param num: number to search for
        :return: boolean value, whether num is contained in the given row
        """
        in_row = False
        for i in self.board[row]:
            if num == self.board[row][i]:
                in_row = True
                break
        return in_row

    def valid_in_col(self, col, num):
        """
        :param col: column number
        :param num: number to search for
        :return: boolean value, whether num is contained in the given row
        """
        in_col = False
        for row in self.board:
            if num == row[col]:
                in_col = True
                break
        return in_col

    def valid_in_box(self, row_start, col_start, num):
        """
        :param row_start: number of first row in box
        :param col_start: number of first column in box
        :param num: number to search for
        :return: boolean value, whether num is contained in the 3x3 box
        """
        box = []
        valid = False
        box = self.get_box(row_start, col_start)
        for i in box:
            if num == i:
                valid = True
                break
        return valid

    def is_valid(self, row, col, num):
        """
        :param row: row number
        :param col: column number
        :param num: number to insert
        :return: boolean, if it is valid to enter a num in given square
        """
        valid = 0
        # Make sure box is empty
        if self.board[row][col] == 0:
            valid += 1
        # Make sure num is not in row
        for i in self.board[row]:
            if row[i] == num:
                break
        else:
            valid += 1
        # Make sure num is not in col
        for i in self.board:
            if self.board[i][col] == num:
                break
        else:
            valid += 1
        if valid == 3:
            return True
        else:
            return False

    def fill_box(self, row_start, col_start):
        """
        :param row_start: number of first row in box
        :param col_start: number of first column in box
        :return: void, fills 3x3 with randomly filled values
        """
        box = self.get_box(row_start, col_start)
        random_list = []
        for i in range(9):
            random_list.append(random.randint(1, 9))
        box = random_list

    def fill_diagonal(self):
        """
        :return: void, fills the three boxes of the board's main diagonal
        """
        self.fill_box(0, 0)
        self.fill_box(4, 4)
        self.fill_box(7, 7)

    def fill_remaining(self, row, col):
        """
        :param row: #FIXME
        :param col: #FIXME
        :return: completely filled board
        """
        if col >= self.row_length and row < self.row_length - 1:
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    def fill_values(self):
        """
        :return: void, constructs a solution
        """
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    def remove_cells(self):
        """
        :return: void, removes appropriate number of cells from the board
        """
        cells = []
        for i in range(self.empty_cells):
            num = random.randint(0, 80)
            cells.append(num)

        def locate_cell(number):
            if 0 <= number <= 8:
                row = 0
            elif 9 <= number <= 17:
                row = 1
            elif 18 <= number <= 26:
                row = 2
            elif 27 <= number <= 35:
                row = 3
            elif 36 <= number <= 44:
                row = 4
            elif 45 <= number <= 53:
                row = 5
            elif 54 <= number <= 62:
                row = 6
            elif 63 <= number <= 71:
                row = 7
            elif 72 <= number <= 80:
                row = 8
            return row

        for num in cells:
            row_num = locate_cell(num)
            index = num - (num // 9)
            self.board[row_num][index] = 0


def generate_sudoku(size, removed):
    """
    :param size: how many boxes make up each side of the board
    :param removed: the amount of cells that will be cleared
    :return: size-by-size Sudoku board
    """
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board