import re


# function for day 3, puzzle 1
def get_puzzle_one_solution(filename):
    sum = 0

    file_content = open(filename, "r")
    file_content_list = file_content.readlines()

    for line_num, line in enumerate(file_content_list):
        for match in re.finditer("[0-9]+", line):
            start = match.start()-1 if match.start() != 0 else match.start()
            stop = match.end() if match.end() != len(line) else match.end()-1
            test_string = line[start] + line[stop]
            if line_num != 0:
                test_string += file_content_list[line_num-1][start:stop+1]
            if line_num != (len(file_content_list)-1):
                test_string += file_content_list[line_num+1][start:stop+1]
            if re.search("[^a-zA-Z0-9.\n]", test_string):
                sum += int(match.group())

    return sum

    # TODO: need the following:
        # how to get non-alphanumeric characters via regex
        # how to get both the index range of a number AND the number itself
            # can this be done in the same line?

    # iterate through each line
    # get number + index range of each number in line
    # for number index range, check if adjacent to a non-period symbol
        # check -1 of start and +1 of end of number range (in same line)
        # check -/+1 line and then each index of the number's index range AND -1 of lowest index (floor) and +1 of highest index (ceiling)
        # if any of the above is true, add to sum
    # return sum



# get solutions
solution = get_puzzle_one_solution("day03_puzzle_input.txt")
print("Question 1 solution is: {}".format(solution))

#solution = get_puzzle_two_solution("day02_puzzle_input.txt")
#print("Question 2 solution is: {}".format(solution))