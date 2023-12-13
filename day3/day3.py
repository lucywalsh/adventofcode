import re

def contains_special_char(string):
    special_characters = '!@#$%^&*()-+?_=,<>/'
    return any(char in special_characters for char in string)

def get_string_above(left_edge, right_edge, start_pos, end_pos, line_length, total_string):
    
    if start_pos < line_length:
        string_above = ""

    else:
        if left_edge:
            top_left = start_pos - line_length
        else:
            top_left = start_pos - line_length - 1
            
        if right_edge:
            top_right = end_pos - line_length
        else:
            top_right = end_pos - line_length + 1
        string_above = total_string[top_left:top_right]

    return string_above

def get_string_middle(left_edge, right_edge, start_pos, end_pos, line_length, total_string):

    if left_edge:
        middle_left = start_pos
    else:
        middle_left = start_pos - 1
    if right_edge:
        middle_right = end_pos
    else:
        middle_right = end_pos + 1

    return total_string[middle_left:middle_right]

def get_string_below(left_edge, right_edge, start_pos, end_pos, line_length, total_string):

    if end_pos > len(total_string)-line_length:
        string_below = ''
    else:
        if left_edge:
            bottom_left = start_pos+line_length
        else:
            bottom_left = start_pos+line_length - 1
        if right_edge:
            bottom_right = end_pos+line_length
        else:
            bottom_right = end_pos+line_length+1
        string_below = total_string[bottom_left:bottom_right]

    return string_below
    

def is_symbol_adjacent(start_pos, end_pos, line_length, total_string):
    left_edge = 1 if start_pos % line_length == 0 else 0
    right_edge = 1 if end_pos % line_length == 0 else 0
    
    string_above = get_string_above(left_edge, right_edge, start_pos, end_pos, line_length, total_string)
    string_middle = get_string_middle(left_edge, right_edge, start_pos, end_pos, line_length, total_string)
    string_below = get_string_below(left_edge, right_edge, start_pos, end_pos, line_length, total_string)
    
    if contains_special_char(string_above) or contains_special_char(string_middle) or contains_special_char(string_below):
        return True
    return False
            
def part_one(lines):
    line_length = len(lines[0])
    total_string = ''.join(lines)
    total = 0
    line_num = 0
    while line_num < len(lines):
        line = lines[line_num]
        numbers = re.finditer('[0-9]+',line)
        for match in numbers:
            start_pos = match.start()+line_num*line_length
            end_pos = match.end()+line_num*line_length
            number = total_string[start_pos:end_pos]
            if is_symbol_adjacent(start_pos, end_pos, line_length, total_string):
                total+=int(number)
        line_num+=1
    print("Total = ", total)        

if __name__== "__main__":
    with open('./day3-input.txt','r') as file:
        lines = [line.rstrip() for line in file]
    part_one(lines)
