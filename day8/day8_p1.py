import argparse

if __name__ == '__main__':
    # argument parsing to grab input file
    parser = argparse.ArgumentParser(description="Day 8: Segment search")
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
    
    easy_set = set([2, 4, 3, 7])
    # go through list of lines
    lines = input.readlines()
    count = 0
    for line in lines:
        input_output = line.split('|')
        digits = input_output[0]
        segments = input_output[1].split()
        for segment in segments:
            if len(segment) in easy_set:
                count += 1
    print("Final count: ", count)
    exit(0)


