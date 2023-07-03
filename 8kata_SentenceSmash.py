def smash(words):
    sentence = ""
    for i in words:
        sentence = sentence + " " + i
        
    print (sentence.strip())
    return sentence.strip()

#Best solution:
#def smash(words):
#    print(" ".join(words))
#    return " ".join(words)

smash(['hello', 'world', 'this', 'is', 'great'])
    