import argparse

if __name__ == '__main__':
    # argument parsing to grab input file
    parser = argparse.ArgumentParser(description="Day 5: Hydrothermal Venture")
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
    point_to_line_count = {}
    dangerous_count = 0
    for line in lines:
        points = line.strip('\n').split(" -> ")
        assert(len(points) == 2)
        starting_point = [int(val) for val in points[0].split(',')]
        ending_point = [int(val) for val in points[1].split(',')]

        # horizontal line check
        if starting_point[1] == ending_point[1]:
            min_val = min(starting_point[0], ending_point[0])
            max_val = max(starting_point[0], ending_point[0])
            for x in range(min_val, max_val + 1):
                pos = (x,starting_point[1])
                if not pos in point_to_line_count:
                    point_to_line_count[pos] = 0
                point_to_line_count[pos] += 1
                if point_to_line_count[pos] == 2:
                    dangerous_count += 1
            continue
        # vertical line check
        if starting_point[0] == ending_point[0]:
            min_val = min(starting_point[1], ending_point[1])
            max_val = max(starting_point[1], ending_point[1])
            for y in range(min_val, max_val + 1):
                pos = (starting_point[0], y)
                if not pos in point_to_line_count:
                    point_to_line_count[pos] = 0
                point_to_line_count[pos] += 1
                if point_to_line_count[pos] == 2:
                    dangerous_count += 1
            continue

        # sloped line
        # slope = 1.0 * (starting_point[1] - ending_point[1]) / (starting_point[0] - ending_point[0])
        # curr_x = starting_point[0]
        # curr_y = starting_point[1]
        # for i in range(abs(starting_point[0] - ending_point[0])):
        #     pos = (curr_x,curr_y)
        #     if not pos in point_to_line_count:
        #         point_to_line_count[pos] = 0
        #     point_to_line_count[pos] += 1
        #     if point_to_line_count[pos] == 2:
        #         dangerous_count += 1
        #     if starting_point[0] < ending_point[0]:
        #         curr_x += 1
        #     else:
        #         curr_x -= 1
        #     curr_y += slope
    print("Danger count", dangerous_count)
    exit(0)


