def obfuscate(text: str) -> str:
    """This function obfuscates the text parsed into the text argument in the 
    following manner: Every instance of the word 'the' is changed to 'and' and 'and'
    to 'the'. Every third letter becomes uppercase.Reverse the letters in every fifth word.
    Apply a shift cypher with key 1 to encrypt every other word"""

    if type(text) != str:  # Here error checking is handled
        print('Please enter a string as an argument')
        return None

    lowertext = text.lower()
    text_array = list(lowertext.split())
    cypher = {'a': 'b', 'b': 'c', 'c': 'd', 'd': 'e', 'e': 'f', 'f': 'g', 'g': 'h', 'h': 'i', 'i': 'j',
              'j': 'k', 'k': 'l', 'l': 'm', 'm': 'n', 'n': 'o', 'o': 'p', 'p': 'q', 'q': 'r', 'r': 's', 's': 't',
              't': 'u', 'u': 'v', 'v': 'w', 'w': 'x', 'x': 'y', 'y': 'z', 'z': 'a', 'A': 'B', 'B': 'C', 'C': 'D', 'D': 'E', 'E': 'F', 'F': 'G', 'G': 'H', 'H': 'I', 'I': 'J',
              'J': 'K', 'K': 'L', 'L': 'M', 'M': 'N', 'N': 'O', 'O': 'P', 'P': 'Q', 'Q': 'R', 'R': 'S', 'S': 'T',
              'T': 'U', 'U': 'V', 'V': 'W', 'W': 'X', 'X': 'Y', 'Y': 'Z', 'Z': 'A'}
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    upperalphabet = alphabet.capitalize()
    # Here the word 'and' is replaced with 'the' and 'the' with 'and'
    for index in range(len(text_array)):
        if text_array[index] == 'the':
            text_array[index] = 'and'
        elif text_array[index] == 'and':
            text_array[index] = 'the'

    # Here a string to handle the upper method is created
    newstring1 = str(''.join(text_array))
    newstring2 = ''
    # Here every third value is turned into an uppercase value
    for i in range(1, len(newstring1)+1):
        if i % 3 == 0:
            newstring2 += newstring1[i-1].upper()
        else:
            newstring2 += newstring1[i-1].lower()

    newlist = newstring2.split()
    for i in range(1, len(newlist)):  # Here every fifth word is reversed
        if i % 5 == 0 and i != 0:
            newlist[i-1] = newlist[i-1][::-1]

    for word in range(0, len(newlist)):
        if word % 2 == 0 and word != 0:
            charlist = list(newlist[word-1])
            wordhold = ''
            for char in charlist:
                wordhold += cypher[char]
            newlist[word-1] = wordhold
    finalstring = ' '.join(newlist)
    return finalstring
