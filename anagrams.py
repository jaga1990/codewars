def anagrams(word, words):
    word_sorted=sorted(word)
    anagrams=[wrd for wrd in words if sorted(wrd) == word_sorted]
    #print(anagrams)
    return anagrams

anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer'])