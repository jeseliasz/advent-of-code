import re


# function for day 4, puzzle 1
def get_puzzle_one_solution(filename):
    # this is going to be a bell curve, so you only need half the data and *2 in the end
    # # # you don't even need to calculate all of it, actually... you only need to figure out at which point you beat the distance
    # # # and num-(index*2) --> this way, you don't even need to account for odd/even
    # # # the only thing to watch out for is that you have indices/len correct because that always bites you in the ass
    mult = 1

    puzzle_file = open(filename, "r")
    file_info = puzzle_file.readlines()

    # one line list creation even though it's messy
    times = [ int(time) for time in re.split("\s+", file_info[0].strip())[1:] ]
    distances = [ int(dist) for dist in re.split("\s+", file_info[1].strip())[1:] ]

    # you can also do this using bubble search or something
    for index, time in enumerate(times):
        distance_to_beat = distances[index]
        total_games = time + 1
        for num in range(total_games):
            travel_time = time - num
            total_distance = num * travel_time
            if total_distance > distance_to_beat:
                games_won = total_games - (num * 2)
                mult *= games_won
                break

    return mult

def get_puzzle_two_solution(filename):
    puzzle_file = open(filename, "r")
    file_info = puzzle_file.readlines()

    # one line list creation even though it's messy
    time = int(re.split(":", file_info[0].replace(" ",""))[1])
    distance_to_beat = int(re.split(":", file_info[1].replace(" ",""))[1])

    # you can also do this using bubble search or something
    total_games = time + 1
    for num in range(total_games):
        travel_time = time - num
        total_distance = num * travel_time
        if total_distance > distance_to_beat:
            games_won = total_games - (num * 2)
            break

    return games_won



# get solutions
#solution = get_puzzle_one_solution("day06_puzzle_input.txt")
#print("Question 1 solution is: {}".format(solution))

solution = get_puzzle_two_solution("day06_puzzle_input.txt")
print("Question 2 solution is: {}".format(solution))
