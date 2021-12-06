import argparse

'''
Class representing a bingo board
'''
class BingoBoard:
    def __init__(self, board : list):
        self.rows = [set([]) for i in range(len(board))]
        self.columns = [set([]) for i in range(len(board))]
        self.diagonals = [set([]) for i in range(2)]
        self.val_to_pos = {}
        self.score = 0
        self.is_bingo = False
        for y in range(len(board)):
            assert(len(board) == len(board[y]))
            for x in range(len(board[y])):
                curr_val = board[x][y]
                self.rows[x].add(curr_val)
                self.columns[y].add(curr_val)
                if x == y:
                    self.diagonals[0].add(curr_val)
                if x == (len(board[y]) - 1 - y):
                    self.diagonals[1].add(curr_val)
                self.score += curr_val
                assert(not curr_val in self.val_to_pos)
                self.val_to_pos[curr_val] = (x, y)
    
    def mark_number(self, number: int) -> bool:
        if not number in self.val_to_pos:
            return False
        position = self.val_to_pos[number]
        x = position[0]
        y = position[1]
        self.rows[x].remove(number)
        if(len(self.rows[x]) == 0):
            self.is_bingo = True
        self.columns[y].remove(number)
        if(len(self.columns[y]) == 0):
            self.is_bingo = True
        if x == y:
            self.diagonals[0].remove(number)
            # if(len(self.diagonals[0]) == 0):
            #     self.is_bingo = True
        if x == (len(self.rows) - 1 - y):
            self.diagonals[1].remove(number)
            # if(len(self.diagonals[1]) == 0):
            #     self.is_bingo = True
        self.score -= number
        return self.is_bingo

if __name__ == '__main__':
    # argument parsing to grab input file
    parser = argparse.ArgumentParser(description="Process bingo board for giant squid")
    required = parser.add_argument_group("required arguments")
    required.add_argument("-i", "--input_file", help="path to the input file", required=True)
    args = parser.parse_args()
    if args.input_file is None:
        print("No input file passed in")
        exit(1)
    try:
        input = open(args.input_file, "r")
    except:
        print("Input file path '%s' is invalid" % args.input_file)
        exit(1)
    
    # go through bingo board
    lines = input.readlines()

    numbers = None
    bingo_board = []
    boards = []
    for line in lines:
        if numbers == None:
            numbers = [int(val) for val in line.split(',')]
            continue
        if line == '\n':
            if len(bingo_board) > 0:
                boards.append(BingoBoard(bingo_board))
            bingo_board = []
            continue
        assert(bingo_board != None)
        bingo_board.append([int(val) for val in line.split()])
    boards.append(BingoBoard(bingo_board))

    max_score = 0
    for number in numbers:
        i = 0
        for board in boards:
            if board.mark_number(number):
                max_score = board.score * number
                print("Bingo:", board.score, "*", number, "=", max_score)
                exit(0)
            i += 1
    exit(0)


