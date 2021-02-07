def word_pattern(word):
    letters_dict = {}
    last_idx = 0
    final_word = ""
    for letter in word.lower():
        if letter in letters_dict: 
            final_word += str(letters_dict[letter]) + "."
        else:
            final_word = final_word + str(last_idx) + "."
            letters_dict[letter] = last_idx
            last_idx += 1
    return final_word[:-1]
word_pattern("helLo")

