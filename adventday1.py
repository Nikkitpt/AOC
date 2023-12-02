import pandas as pd 

def txt_to_list_converter(document_path):
    """
    takes google doc and converts to string
    """
    with open(document_path, 'r') as file:
        lines = file.readlines()
    lines = [line.strip() for line in lines]
    return lines

    

def part_one(calibration_value):
    # calibration_value = ['1abc2',"pqr3stu8vwx","a1b2c3d4e5f","treb7uchet"]

    total = 0
    for x in calibration_value:
        each_index = list(x)

        digits = ""
        for y in each_index: 
            if y.isdigit() == True:
                digits = y
                # print(digits)
                break
        for y in reversed(each_index):
            if y.isdigit() == True:
                # print(y)
                digits = digits + y 
                break
        total = total + int(digits)
        print(total)
       

def word_to_integer(word):
    word_mapping = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four' : '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight':'8',
        'nine': '9',
    }
    lowercased_word = word.lower()

    return word_mapping.get(lowercased_word, None)



def part_two(calibration_value):
    #calibration_value = ["nineeight6mkvbfour6four","oneight"]
    string_substring = ["one","two","three","four", "five", "six", "seven", "eight","nine"]
    num_substring = ["1","2","3","4","5","6","7","8","9"]
    total = 0

    for x in calibration_value:
        # print(x)
        subs = []
        digits = ""
        for substring in string_substring:
            index = x.find(substring)
            while index != -1:
                found = {"index": index, "substring": substring}
                print(found)
                subs.append(found)
                index = x.find(substring, index + 1)

        
        for index, value in enumerate(x):
            if value.isdigit():
                found = {"index": index, "substring": value}
                subs.append(found)
                print(found)
    

        sorted_list = sorted(subs, key=lambda x: x['index'])
        first_digit = sorted_list[0]["substring"]
        last_digit = sorted_list[-1]["substring"]

        if first_digit.isdigit() != True:
            first_digit= word_to_integer(first_digit)
        if last_digit.isdigit() != True:
            last_digit = word_to_integer(last_digit)
        
        digits = first_digit + last_digit

        total = total + int(digits)
        print(x, digits)
        
    print(total)
 


    
calibration_value = txt_to_list_converter("adventday1.txt")
part_one(calibration_value)
part_two(calibration_value)


