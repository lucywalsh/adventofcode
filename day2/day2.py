import re

def parse_lines(lines):
    games = []
    for line in lines:
        turns_raw = line.split(':')[1]
        turns = [turn.strip() for turn in turns_raw.split(';')]
        colours = ['red','green','blue']
        turns_parsed = []
        for turn in turns:
            colours_present = re.findall('|'.join(colours), turn)
            numbers = re.findall('[0-9]+', turn)
            turn_dict = dict(zip(colours_present, numbers))
            turns_parsed.append(turn_dict)
        games.append(turns_parsed)
    return games

def check_turn(turn, red_limit, green_limit, blue_limit):
    if 'red' in turn and int(turn['red']) > red_limit:
        return False
    if 'blue' in turn and int(turn['blue']) > blue_limit:
        return False
    if 'green' in turn and int(turn['green']) > green_limit:
        return False
    return True

def check_game(game, red_limit, green_limit, blue_limit):
    i=0
    while i < len(game):
        if not check_turn(game[i], red_limit, green_limit, blue_limit):
            return False
        i+=1
    return True

def part_one(lines):
    games = parse_lines(lines)

    total = 0
    
    for i in range(len(games)):
        if check_game(games[i], 12, 13, 14):
            total+=i+1
    print("Total:", total)

def find_min_cubes(game, colour):
    min_cubes = 0
    for turn in game:
        if colour in turn and int(turn[colour]) > min_cubes:
            min_cubes = int(turn[colour])
    return min_cubes

def part_two(lines):
    games = parse_lines(lines)
    powers = []
    for game in games:
        min_red = find_min_cubes(game, 'red')
        min_blue = find_min_cubes(game, 'blue')
        min_green = find_min_cubes(game, 'green')
        power = min_red*min_blue*min_green
        powers.append(power)
    print("Total = ", sum(powers))
        
    

if __name__ == "__main__":
    with open('./day2-input.txt','r') as file:
        lines = [line.rstrip() for line in file]
    part_two(lines)
