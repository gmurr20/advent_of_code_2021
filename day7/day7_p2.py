import argparse

def recursive_solution(fish : list, days : int) -> int:
    if days == 0:
        return len(fish)
    ret_val = 0
    if len(fish) > 1:
        for i in range(len(fish)):
            ret_val += recursive_solution([fish[i]], days)
        return ret_val
    
    curr_fish_val = fish[0]
    if curr_fish_val == 0:
        ret_val += recursive_solution([6], days - 1) + recursive_solution([8], days - 1)
        return ret_val
    return recursive_solution([curr_fish_val - 1], days - 1)

def better_solution(fish : list, days: int) -> int:
    fish_population_by_life = [0 for i in range(9)]
    for f in fish:
        fish_population_by_life[f] += 1
    for i in range(days):
        new_population = [0 for i in range(9)]
        for i in range(9):
            num_fish = fish_population_by_life[i]
            if num_fish == 0:
                continue
            if i == 0:
                new_population[8] += num_fish
                new_population[6] += num_fish
            else:
                new_population[i - 1] += num_fish
        fish_population_by_life = new_population
    return sum(fish_population_by_life)

if __name__ == '__main__':
    # argument parsing to grab input file
    parser = argparse.ArgumentParser(description="Day 7: Whales!")
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
    horizontal_positions = None
    for line in lines:
        assert(horizontal_positions == None)
        horizontal_positions = [int(val) for val in line.split(',')]
    horizontal_positions.sort()
    curr_val = horizontal_positions[0]
    prev_sum = None
    for i in range(horizontal_positions[0], horizontal_positions[len(horizontal_positions) - 1]):
        curr_val = i
        new_sum = 0
        for val in horizontal_positions:
            n = abs(val - curr_val)
            new_sum += int(n * (n + 1) / 2)
        if prev_sum != None:
            if prev_sum < new_sum:
                print(i, curr_val)
                break
        prev_sum = new_sum

    print(prev_sum)
    exit(0)


