import re


# function for day 4, puzzle 1
def get_puzzle_one_solution(filename):
    steps = 0

    puzzle_file = open(filename, "r")
    file_info = puzzle_file.readlines()

    directions = file_info[0].strip()
    network_dict = create_network_dict(file_info[2:])

    index = 0
    found = False
    current_key = "AAA"

    while not found:
        print("index: {}".format(index))
        direction_choice = 0 if directions[index] == "L" else 1
        current_key = network_dict.get(current_key)[direction_choice]
        steps += 1
        if current_key == "ZZZ":
            print("if stmt 1")
            found = True

        if index == len(directions)-1:
            print("if stmt 2")
            index = 0
        else:
            index += 1

    return steps

def create_network_dict(data):
    return_dict = {}

    for line in data:
        line = re.sub("[=,(,),\,]", "", line.strip())
        line = re.split("\s+", line)

        return_dict[line[0]] = [line[1], line[2]]

    return return_dict

def create_network_dict_and_list(data):
    return_dict = {}
    return_list = []

    for line in data:
        line = re.sub("[=,(,),\,]", "", line.strip())
        line = re.split("\s+", line)

        return_dict[line[0]] = [line[1], line[2]]

        if line[0].endswith("A"):
            return_list.append(line[0])

    return return_dict, return_list

def get_puzzle_two_solution(filename):
    steps = 0

    puzzle_file = open(filename, "r")
    file_info = puzzle_file.readlines()

    directions = file_info[0].strip()

    network_dict, current_keys = create_network_dict_and_list(file_info[2:])

    index = 0
    all_z = False

    while not all_z:
        direction_choice = 0 if directions[index] == "L" else 1

        print("current_keys: {}".format(current_keys))

        next_keys_list = []
        for key in current_keys:
            next_key = network_dict.get(key)[direction_choice]
            next_keys_list.append(next_key)

        current_keys = next_keys_list
        steps += 1

        if all(key.endswith("Z") for key in current_keys):
            all_z = True

        if index == len(directions) - 1:
            index = 0
        else:
            index += 1

    return steps


# get solutions
#solution = get_puzzle_one_solution("day08_puzzle_input.txt")
#print("Question 1 solution is: {}".format(solution))

solution = get_puzzle_two_solution("day08_puzzle_input.txt")
print("Question 2 solution is: {}".format(solution))