def make_readable(seconds):
    hours = 0
    minutes_left = 0
    seconds_left = 0
    if seconds>59:
        minutes = seconds//60
        seconds_left = seconds - minutes * 60
        if minutes>59:
            hours = minutes//60
            minutes_left = minutes - hours * 60
        else:
            minutes_left=minutes
    else:
        seconds_left=seconds

    print(hours, ':', minutes_left,':', seconds_left)

make_readable(359999)