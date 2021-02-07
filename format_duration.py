def format_duration(seconds):
    output = []
    minutes, seconds = divmod(seconds, 60)
    if seconds > 1:
        output.append((seconds, 'seconds'))
    elif seconds == 1:
        output.append((seconds, 'second'))
    
    if minutes >= 60:
        hours, minutes = divmod(minutes, 60)

    if minutes > 1:
        output.append((minutes, 'minutes'))
    elif minutes == 1:
        output.append((minutes, 'minute'))

        
    days, hours = divmod(hours, 24)
    years, days = divmod(days, 365)

    result_list = [(seconds, 'seconds')]
    result_list = [str(years) + ' years', str(days) + ' days', str(hours) + ' hours', str(minutes) + ' minutes', str(seconds), 'seconds']
    print(', '.join(result_list))

    #format_names = ('minute', 'second')
    ##format_values = divmod(seconds, 60)
    #list_to_print = []
    #for element in list(zip(format_names, format_values)):
    #    if element[1]>1:
    ##        list_to_print.append((element[0] + 's', element[1]))
    #    elif element[1] == 1:
    #        list_to_print.append((element[0], element[1]))
    #to_print = ''
    #for el in list_to_print:
    #    to_print = to_print + str(el[1]) + ' ' + el[0]

    #to_print = [element for element in  if element[1] != 0]
    #print(to_print)
    #minutes, seconds = divmod(seconds, 60)
    #to_print = divmod(seconds, 60)
    
    #print(list_to_print)
format_duration(120)
