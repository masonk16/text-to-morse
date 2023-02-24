from alphabet import morse_alphabet

message = input('Enter message to convert: \n').split()


def text_to_morse(message):
    """
    Takes a text based messaged and converts it to morse code.
    :param message: text to be converted.
    :return: translated morse message.
    """
    for word in message:
        morse_msg = ""
        for letter in word:
            morse_msg += morse_alphabet[letter.lower()] + " "

        return morse_msg


print(text_to_morse(message))
