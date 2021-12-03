import argparse

def convert_binary_string(binary_string: str) -> int:
    val = 0
    for i in range(len(binary_string)):
        if binary_string[len(binary_string) - 1 - i] == '0':
            continue
        val += 2 ** i
    return val

def grab_rate(binary_strings: list, index: int, majority : bool) -> int:
    assert(len(binary_strings) != 0)
    if len(binary_strings) == 1:
        return convert_binary_string(binary_strings[0])
    bit_to_strings = {'0' : [], '1': []}
    for line in binary_strings:
        binary_string = str(line).strip()
        if index >= len(binary_string):
            return convert_binary_string(binary_string)
        bit_to_strings[binary_string[index]].append(binary_string)
    
    if majority:
        if len(bit_to_strings['0']) > len(bit_to_strings['1']):
            return grab_rate(bit_to_strings['0'], index + 1, majority)
        return grab_rate(bit_to_strings['1'], index + 1, majority)
    else:
        if len(bit_to_strings['0']) <= len(bit_to_strings['1']):
            return grab_rate(bit_to_strings['0'], index + 1, majority)
        return grab_rate(bit_to_strings['1'], index + 1, majority)

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
    
    # construct gamma and epsilon rate
    oxygen = grab_rate(lines, 0, True)
    co2 = grab_rate(lines, 0, False)
    print("Oxygen:", oxygen)
    print("CO2:", co2)
    print("Answer:", oxygen * co2)
    exit(0)