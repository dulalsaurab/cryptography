import codecs
import string
import single_char_xor as scxc


# This function converts given decimal or hex number in binary
def binary_conversion(decimal=None, hex=None):
    resultant_binary_dec = ''
    resultant_binary_hex = ''
    if decimal:
        while (decimal > 0):
            resultant_binary_dec = str((decimal % 2)) + resultant_binary_dec
            decimal = int(decimal / 2)

    if hex:
        resultant_binary_hex, gr = binary_conversion(int(hex, 16),
                                                     '')
        # This is a recursive call, thus we don't
        # expect any value in gr(garvage for simplicity)

    return resultant_binary_dec, resultant_binary_hex


# This function xor two string of same length
# or a whole string with single char or num
# This function only operates with hex values,
# So, trying other than hex will produce a garbage output
def XOR(string1=None, string2=None, type=None):
    # Length of strings are expected to be same,
    # we can run a loop through the length of any one sting
    xor_result = ''
    if type == 'E':  # for equal length
        for index, str1 in enumerate(string1):
            # This does a xor operation, xor can only operate in number,
            # So, I have converted to corresponding char value to ascii and subtracted it by 87 to get hex
            xor_buf = ((ord(str1) - 87)
                       if str1.isalpha()
                       else (int(str1))) ^ (
                            (ord(string2[index]) - 87)
                       if string2[index].isalpha()
                       else (int(string2[index])))

            if xor_buf > 9 and xor_buf < 16:
                xor_result = xor_result + (chr(xor_buf + 87))
            else:
                xor_result = xor_result + str(xor_buf)
        return xor_result

    elif type == 'S':  # with single character or number
        for index, str1 in enumerate(string1):
            xor_buf = ((ord(str1) - 87) if str1.isalpha() else (int(str1))) ^ (
                (ord(string2) - 87) if string2.isalpha() else (int(string2)))
            if xor_buf > 9 and xor_buf < 16:
                xor_result = xor_result + chr(xor_buf + 87)
            else:
                print(xor_result)
                xor_result = xor_result + str(xor_buf)

        return xor_result

# hex to base 64 encoding
def base64_encoding(hex_string):
    base64_encoded_value = codecs.encode(codecs.decode
                                         (hex_string, 'hex'), 'base64').decode()
    return base64_encoded_value

def sift_ciphers(encText):
    # it has a key ranging from 0 - 25
    # letter are converted to number such as A =1, B = 2
    decoded__list = []
    for key in range(0, 26):
        dec_text = ''
        for letter in encText:
            if letter.isalpha():
                # Convert letter to ascii and map it to range(0,26)
                # find modulo 26, and again convert it to char
                dec_text = dec_text + str(chr((((ord(letter) - 97) + key) % 26) + 97))
            else:
                dec_text = dec_text + ' '
        decoded__list.append(dec_text)
    return max(decoded__list, key=scxc.probability_of_being_legit_string)
    # predection using word frequency table


def num_to_hex(num):
    # hex system has 16 numbers starting from 0-9 & a-f
    hex_holder = ''

    while (num > 0):
        # The operator used below is similar to tertary operator ?:, its similar to "a if condition b"
        hex_holder = str(chr(int(num % 16) + 87)
                         if int(num % 16) > 9
                         else int(num % 16)) + hex_holder
        # num%16 will be in range 10-15, if alpha
        # Thus adding 87 will give corresponding ascii letter

        num = int(num / 16)

    return hex_holder

