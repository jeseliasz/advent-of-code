import re


# global variables
BEGIN_SUM = 0
TEXT_TO_NUM_DICT = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


# function for day 1, puzzle 1
def get_puzzle_one_sum(filename):
    sum = BEGIN_SUM
    regex_pattern = "[^0-9]+"
    # open file
    with open(filename) as puzzle_file:
        # read line by line
        for line in puzzle_file:
            # parse numbers from each line using regex
            num_str = re.sub(regex_pattern, "", line)
            num_int, num_len = int(num_str), len(num_str)
            # default value
            number = num_int
            # handle case for one number in line
            if num_len == 1:
                number = (num_int * 10) + num_int
            # handle case for more than two numbers in line
            elif num_len > 2:
                number = int(num_str[0] + num_str[-1])
            # add
            sum += number

    return sum

# function for day 1, puzzle 2
def get_puzzle_two_sum(filename):
    sum = BEGIN_SUM
    regex_pattern = "(?=(" + '|'.join(TEXT_TO_NUM_DICT) + "|[0-9]))"

    with open(filename) as puzzle_file:
        # read line by line
        for line in puzzle_file:
            # parse numbers from each line using regex
            num_list = re.findall(regex_pattern, line)
            num_list_len = len(num_list)
            # handle case for one number in line
            if num_list_len == 1:
                num_value = num_list[0]
                num_int = int(num_value)
                number = (num_int * 10) + num_int
                sum += number
            # handle more than two numbers in line
            elif num_list_len > 2:
                num_list = [num_list[0], num_list[-1]]
                sum += handle_two_plus_list_len(num_list)
            # handle exactly two numbers in line
            elif num_list_len == 2:
                sum += handle_two_plus_list_len(num_list)

    return sum

# helper function for day 1, puzzle 2
def handle_two_plus_list_len(num_list):
    num_str = ""
    for num in num_list:
        if len(num) > 1:
            num = TEXT_TO_NUM_DICT[num]
        num_str += num
    number = int(num_str)
    return number


# get solutions
puzzle_one_sum = get_puzzle_one_sum("day01_puzzle_input.txt")
print("Solution for puzzle 1: {}".format(puzzle_one_sum))

puzzle_two_sum = get_puzzle_two_sum("day01_puzzle_input.txt")
print("Solution for puzzle 2: {}".format(puzzle_two_sum))
