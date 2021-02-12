def valid_parentheses(string):
    no_of_left = 0
    no_of_right = 0
    if string.count('(') != string.count(')'): 
        return False
    if string.find('(') > string.find(')') or string.rfind('(') > string.rfind(')'): 
        return False
    
    for char in string:
        if char == '(':
            no_of_left += 1
        elif char == ')':
            no_of_right += 1
        if no_of_right > no_of_left: 
                return False
    return True
valid_parentheses('hi(hi)()')



# def valid_parentheses(string):
#     cnt = 0
#     for char in string:
#         if char == '(': cnt += 1
#         if char == ')': cnt -= 1
#         if cnt < 0: return False
#     return True if cnt == 0 else False