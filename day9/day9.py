import argparse
from collections import deque

def is_low_point(grid : list, x : int, y : int) -> bool:
    curr_val = grid[y][x]
    if x + 1 < len(grid[y]) and grid[y][x + 1] <= curr_val:
        return False
    if x - 1 >= 0 and grid[y][x - 1] <= curr_val:
        return False
    if y + 1 < len(grid) and grid[y + 1][x] <= curr_val:
        return False
    if y - 1 >= 0 and grid[y - 1][x] <= curr_val:
        return False
    return True

if __name__ == '__main__':
    # argument parsing to grab input file
    parser = argparse.ArgumentParser(description="Day 9: Smoke Basin")
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
    
    # go through list of lines
    lines = input.readlines()
    input_grid = []
    for line in lines:
        input_grid.append([])
        for digit in line:
            if digit == '\n':
                break
            input_grid[-1].append(int(digit))
    
    basins_list = []
    for y in range(len(input_grid)):
        for x in range(len(input_grid[y])):
            if not is_low_point(input_grid, x, y):
                continue
            
            # discover basin with bfs
            basin_size = 0
            visited = set([])
            positions = deque([(x,y)])
            while len(positions) != 0:
                pos = positions.popleft()
                if pos in visited:
                    continue
                curr_x = pos[0]
                curr_y = pos[1]
                curr_val = input_grid[curr_y][curr_x]
                visited.add((curr_x, curr_y))
                if curr_val == 9:
                    continue
                basin_size += 1
                # go right
                if curr_x + 1 < len(input_grid[curr_y]):
                    positions.append((curr_x + 1, curr_y))
                # go left
                if curr_x - 1 >= 0:
                    positions.append((curr_x - 1, curr_y))
                # go down
                if curr_y + 1 < len(input_grid):
                    positions.append((curr_x, curr_y + 1))
                # go up
                if curr_y - 1 >= 0:
                    positions.append((curr_x, curr_y - 1))
            basins_list.append(basin_size)
    basins_list = sorted(basins_list)
    assert(len(basins_list) >= 3)
    final_val = 1
    for i in range(3):
        final_val *= basins_list[len(basins_list) - 1 - i]
    print(final_val)
    exit(0)


