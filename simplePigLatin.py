def pig_it(phrase):
    list_of_punctuation_marks = [",",".","?","!"]
    string_to_add = "ay"
    list_of_words = phrase.split()
    output_list = [word[1:] + word[0] + string_to_add if word not in list_of_punctuation_marks else word for word in list_of_words]
    print(' '.join(output_list))

pig_it('Hello world !')