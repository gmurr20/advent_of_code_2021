import argparse

if __name__ == '__main__':
    # argument parsing to grab input file
    parser = argparse.ArgumentParser(description="Process a list of binary numbers for diagnostic report")
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
    
    # go through diagnostic report
    lines = input.readlines()
    byte_counts = None # indexed by the bit position, number of 1s set
    majority_threshold = len(lines) / 2
    for line in lines:
        binary_string = str(line).strip()
        if byte_counts is None:
            byte_counts = [0] * len(binary_string)
        for i in range(len(binary_string)):
            if binary_string[i] == '1':
                byte_counts[len(byte_counts) - 1 - i] += 1
    
    # construct gamma and epsilon rate
    gamma = 0
    epsilon = 0
    for i in range(len(byte_counts)):
        if byte_counts[i] > majority_threshold:
            gamma += 2 ** i
        else:
            assert(byte_counts[i] != majority_threshold)
            epsilon += 2 ** i
    print("Gamma:", gamma)
    print("Epsilon:", epsilon)
    print("Answer:", gamma * epsilon)
    exit(0)


