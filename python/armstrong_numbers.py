#CHECKER: one item in → True/False out
def is_armstrong(num):
    total = 0 
    # capture the string in a name so you can reuse it / number -> string, STORED in a name
    digits = str(num)
    # length of the string = how many digits
    digit_count = len(digits)
    # step through each character
    for char in digits:
        # Init-before / update-inside / use-after 
        total += int(char) ** digit_count
    return total == num


# WALKER: list in → filtered list out
def find_armstrong_numbers(numbers):
    # accumulator: initialize before the loop
    result = []
    # walk the list, one item at a time
    for number in numbers:
        # delegate the yes/no to the checker
        if is_armstrong(number):
            # collect the ones that pass
            result.append(number)        
    # hand back the filtered list, AFTER the loop
    return result
