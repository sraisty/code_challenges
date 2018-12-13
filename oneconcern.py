# ({[]})

# Code Example:  Sue Raisty
# function (string)
# string has 3 types of brakcets
# return true if brackets match

# [] - True 
# [()} - False
# ([]) - True
# ([]{}) - True

# stack: 

def matching_brackets(str):
    stack = []
    # while chars in str
    for c in str:
        # if open, push on stack
        if c == '(' or c == '[' or c == '{':
            stack.append(c)
        else:
            if stack == []:
                return False
            # if close bracket type, pop stack and compare 
            open_char = stack.pop()
            #     if different kind of bracket, return Falase
            if c == ')' and open_char != '(':
                return False
            if c == ']' and open_char != '[':
                return False
            if c == '}' and open_char != '{':
                return False
        #   if same kind of bracket, keep going to next char

    # no more characters in string.

    # if stack is empty return True
    if stack == []:
        return True
    # if not return False
    return False


