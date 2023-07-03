def solution(string):
    reversed_string = ''
    for i in reversed(string):
        reversed_string = reversed_string + i 
    print(reversed_string)
    return reversed_string

solution('world')