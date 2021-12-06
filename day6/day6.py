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
    parser = argparse.ArgumentParser(description="Day 6: Lantern fish")
    parser.add_argument("-d", "--days", type=int, default=80, help="number of days")
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
    
    fish_lives = None
    for line in lines:
        fish_lives = [int(val) for val in line.split(',')]
    print("Answer for # days(", args.days, "):", better_solution(fish_lives, args.days))
    print
    exit(0)


