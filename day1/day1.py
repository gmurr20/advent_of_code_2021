import argparse

if __name__ == '__main__':
    # argument parsing to grab input file
    parser = argparse.ArgumentParser(description="Process a list of sea floor depths")
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
    prev_depth = None
    num_increasing_depths = 0
    for line in lines:
        depth = int(line)
        if prev_depth is None:
            prev_depth = depth
            continue
        if prev_depth < depth:
            num_increasing_depths += 1
        prev_depth = depth
    print("Answer:", num_increasing_depths)
    exit(0)


