
def decodeMorse(morse_code):    
    letter_to_morse = {
        'A': '.-',              
        'B': '-...',           
        'C': '-.-.',           
        'D': '-..',            
        'E': '.',              
        'F': '..-.',            
        'G': '--.',             
        'H': '....',            
        'I': '..',              
        'J': '.---',            
        'K': '-.-',             
        'L': '.-..',            
        'M': '--',              
        'N': '-.',              
        'O': '---',             
        'P': '.--.',            
        'Q': '--.-',            
        'R': '.-.',             
        'S': '...',             
        'T': '-',               
        'U': '..-',             
        'V': '...-',            
        'W': '.--',             
        'X': '-..-',            
        'Y': '-.--',            
        'Z': '--..',            
        '0': '-----',           ',': '--..--',
        '1': '.----',           '.': '.-.-.-',
        '2': '..---',           '?': '..--..',
        '3': '...--',           ';': '-.-.-.',
        '4': '....-',           ':': '---...',
        '5': '.....',           "'": '.----.',
        '6': '-....',           '-': '-....-',
        '7': '--...',           '/': '-..-.',
        '8': '---..',           '(': '-.--.-',
        '9': '----.',           ')': '-.--.-',
        ' ': ' ',               '_': '..--.-',
        '!': '-.-.--',                'SOS': '...---...'}
    
    morse_to_letter = {v: k for k, v in letter_to_morse.items()}
    
    morse_decoded = ''
    code_splitted_to_words = morse_code.split('   ')
    for word in code_splitted_to_words:
        word_splitted_to_letters = word.split()
        word = ''
        for letter in word_splitted_to_letters:
            word = word + morse_to_letter[letter]
        morse_decoded = morse_decoded + ' ' + word
    return morse_decoded.strip()

    


decodeMorse('...---...')