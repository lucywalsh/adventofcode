import re

def part_one():
    total = 0
    
    for i in range(len(lines)):
        line_digits = re.sub('\D', '', lines[i])
        if len(line_digits)==0:
            value=0
        elif len(line_digits)==1:
            value = line_digits+line_digits
        else:
            value = line_digits[0]+line_digits[-1]
        total = total+int(value)

    print("Total = ", total)

def part_two():
    total= 0
    words_to_digits = {'one':'1', 'two':'2', 'three': '3', 'four': '4', 'five': '5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    options = '|'.join(list(words_to_digits.keys())+list(words_to_digits.values()))
    digits = ['1','2','3','4','5','6','7','8','9','0']
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    options = '|'.join(digits+words)
    for i in range(len(lines)):
        line_digits = re.findall('(?=('+options+'))', lines[i])
        first_and_last = [line_digits[0],line_digits[-1]]
        value = ''
        for x in first_and_last:
            if x in words_to_digits:
                value+=words_to_digits[x]
            else:
                value+=x
        total+=int(value)
    print("Total = ",total)
        

if __name__ == "__main__":
    with open('./day1-input.txt', 'r') as file:
        lines = [line.rstrip() for line in file]
    part_one()
    part_two()
    
        
    


        
