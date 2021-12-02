import argparse

if __name__ == '__main__':
    # argument parsing to grab input file
    parser = argparse.ArgumentParser(description="Process a list of submarine commands")
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
    
    # go through depth by depth and find number of increases
    lines = input.readlines()
    curr_depth = 0
    curr_x = 0
    for line in lines:
        command = str(line).split(" ")
        assert(len(command) == 2)
        direction = command[0]
        val = int(command[1])
        if direction == "forward":
            curr_x += val
        elif direction == "up":
            assert(curr_depth >= val)
            curr_depth -= val
        else:
            assert(direction == "down")
            curr_depth += val
    print("Answer:", curr_depth * curr_x)
    print(" - depth=", curr_depth)
    print(" - x=", curr_x)
    exit(0)


