def narcissistic(value):
    power = len(str(value))
    #print([int(i)**power for i in str(value)])
    return sum([int(i)**power for i in str(value)]) == value
narcissistic(371)

