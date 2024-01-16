import re


# function for day 4, puzzle 1
def get_puzzle_one_solution(filename):
    sum = 0

    with open(filename) as puzzle_file:
        for line in puzzle_file:
            matching_numbers = card_value = 0
            num_list = re.split(":|\|", line)[1:]
            winning_numbers = num_list[0].split()
            card_numbers = num_list[1].split()
            for num in winning_numbers:
                if num in card_numbers:
                    matching_numbers += 1
            if matching_numbers != 0:
                card_value = 1 if matching_numbers==1 else pow(2, matching_numbers-1)
            sum += card_value

    return sum

def get_puzzle_two_solution(filename):
    sum = 0

    puzzle_file = open(filename, "r")
    scratchcards = puzzle_file.readlines()

    scratchcard_matrix = [1] * len(scratchcards)

    for scratchcard_index, card in enumerate(scratchcards):
        sum += scratchcard_matrix[scratchcard_index]
        matching_numbers = 0
        num_list = re.split(":|\|", card)[1:]
        winning_numbers = num_list[0].split()
        card_numbers = num_list[1].split()
        for num in winning_numbers:
            if num in card_numbers:
                matching_numbers += 1
        for matrix_index in range(matching_numbers):
            matrix_index += 1
            scratchcard_matrix[scratchcard_index + matrix_index] += scratchcard_matrix[scratchcard_index]

    return sum



# get solutions
#solution = get_puzzle_one_solution("day4_puzzle_input.txt")
#print("Question 1 solution is: {}".format(solution))

solution = get_puzzle_two_solution("day4_puzzle_input.txt")
print("Question 2 solution is: {}".format(solution))
