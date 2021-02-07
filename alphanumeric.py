def alphanumeric(password):
    password_to_str = str(password)
    allowed_chars = ["1","2","3","4","5","6","7","8","9","0","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    set_from_password=set(list(password_to_str.upper()))
    #print(password.isalnum())
    print(set_from_password.issubset(set(allowed_chars)) and len(password_to_str)>=1)
    return set_from_password.issubset(set(allowed_chars)) and len(password_to_str)>=1
    
alphanumeric(123)