import re

# global variables
NUM_REGEX_PATTERN = "[0-9]+"
SPLIT_REGEX_PATTERN = ":|,|;"
BEGIN_VALUE = 0
BEGIN_POWER = 1


# function for day 2, puzzle 1
def get_puzzle_one_solution(filename):
    sum = BEGIN_VALUE
    max_cubes = {
        "red": "12",
        "green": "13",
        "blue": "14",
    }

    with open(filename) as puzzle_file:
        for line in puzzle_file:
            good_game = True
            line_array = re.split(SPLIT_REGEX_PATTERN, line)
            for array_value in line_array:
                # get game number
                if "Game" in array_value:
                    game_number = int(re.findall(NUM_REGEX_PATTERN, array_value)[0])
                # handle cubes
                for cube_key in max_cubes:
                    if cube_key in array_value:
                        cube_value = re.findall(NUM_REGEX_PATTERN, array_value)[0]
                        # if any cube color number exceeds max, game doesn't count
                        if int(cube_value) > int(max_cubes[cube_key]):
                            good_game = False
            # add if game is valid
            if good_game:
                sum += game_number
    return sum


# function for day 2, puzzle 2
def get_puzzle_two_solution(filename):
    sum = BEGIN_VALUE

    with open(filename) as puzzle_file:
        for line in puzzle_file:
            power = BEGIN_POWER
            num_cubes = {
                "red": BEGIN_VALUE,
                "green": BEGIN_VALUE,
                "blue": BEGIN_VALUE,
            }
            line_array = re.split(SPLIT_REGEX_PATTERN, line)
            # go through each cube value, skip index 0 because game number not needed
            for value in line_array[1:]:
                for cube_key in num_cubes:
                    if cube_key in value:
                        cube_num = re.findall(NUM_REGEX_PATTERN, value)[0]
                        cube_num_int = int(cube_num)
                        # if current cube value per color exceeds previous, update in dict
                        if cube_num_int > num_cubes[cube_key]:
                            num_cubes[cube_key] = cube_num_int
            # multiple them all
            for value in num_cubes.values():
                power *= value
            # add power to sum
            sum += power

    return sum


# get solutions
solution = get_puzzle_one_solution("day02_puzzle_input.txt")
print("Question 1 solution is: {}".format(solution))

solution = get_puzzle_two_solution("day02_puzzle_input.txt")
print("Question 2 solution is: {}".format(solution))