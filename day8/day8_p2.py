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
    
    # letter_to_index = {'a' : 0, 'b' : 1, 'c' : 2, 'd' : 3, 'e' : 4, 'f' : 5, 'g' : 6}
    # letter_to_possible_spots = []
    # for i in range(7):
    #     letter_to_possible_spots.append(set([0, 1, 2, 3, 4, 5, 6]))
    # known_letters = []
    # len_to_number = {2 : [1], 3 : [7], 4: [4], 5 : [2, 3, 5], 6: [0, 6, 9], 7 : [8]}
    # number_to_spots = {0 : set([0, 1, 2, 4, 5, 6], )}
    # print(logic_puzzle_grid)
    # # go through list of lines
    # lines = input.readlines()
    # count = 0
    # for line in lines:
    #     input_output = line.split('|')
    #     digits = input_output[0].split()
    # print("Final count: ", count)
    exit(0)


