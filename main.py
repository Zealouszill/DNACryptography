"""

Created Friday April 26, 2019

@author: spencer.stewart
"""


random_binary = "011100111011011010001010110001101011010000000110000100010111100010011011111001011101000011100000111010110010100111010111100001010111100110000001110011110001100101010000001101010111001010010011010001011100000110000110010001100011111011100111010000001011101011001110000011111010001110111100010000101101110001100101000110110111000000010101010000110110001110011001010101011011010111101111001101110011101011100100010111100001000011100110011011101000011000101011110110011111111101011110110110011011011001101001010000111011100101000010111100100101100101101001100011010111101010100000100010110101001111100011110010110100101000110110011100010111100001001110101100010100011010101111110101100010000111011101111000010111110110111110010101000001111100110011100010001001111100100010000011110101000000001000"

def binToString(binary):

    n = int(binary, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()



def stringToBin(string):

    return ''.join(format(ord(i), 'b').zfill(8) for i in string)

def encrypt(string):

    string = stringToBin(string)

    temp_string = ""

    for each_bit in range(len(string)):
        print("This is each_bit", temp_string)
        temp_string += str(xor(string[each_bit], random_binary[each_bit]))

    print("This is temp_string", temp_string)

    return temp_string

def decrypt(encrypted_message):

    temp_string = ""

    for each_bit in range(len(encrypted_message)):
        temp_string += str(xor(encrypted_message[each_bit], random_binary[each_bit]))

    return binToString(temp_string)


def xor(first_bit, second_bit):

    if first_bit == second_bit:
        return 0
    else:
        return 1

##############################################################
#                            Tests                           #
##############################################################

def test_encryption_decryption():

    test_string = "This is the sentence"

    assert decrypt(encrypt(test_string)) == "This is the sentence"


def test_bin_to_string():

    # This binary code below is: This is the sentence
    testBinary = "010101000110100001101001011100110010000001101001011100110010000001110100011010000110010" \
                 "1001000000111001101100101011011100111010001100101011011100110001101100101"

    assert binToString(testBinary) == "This is the sentence"


def test_string_to_bin():

    # This is the sentence to be converted into binary.
    test_string = "This is the sentence"

    assert stringToBin(test_string) == "01010100011010000110100101110011001000000110100101110011001000000111" \
                                       "01000110100001100101001000000111001101100101011011100111010001100101" \
                                       "011011100110001101100101"

