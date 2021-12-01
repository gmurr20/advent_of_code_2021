import argparse
from collections import deque

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
    
    # compare beginning of window with newest depth to determine if window increased in depth
    WINDOW_SIZE = 3
    window = deque()
    lines = input.readlines()
    num_increasing_depths = 0
    for line in lines:
        depth = int(line)
        if len(window) < WINDOW_SIZE:
            window.append(depth)
            continue
        if window[0] < depth:
            num_increasing_depths += 1
        window.popleft()
        window.append(depth)
    print("Answer:", num_increasing_depths)
    exit(0)


