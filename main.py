# cryptic encryption
import codecs
import string

import single_char_xor as scxc


# This function convert give decimal or hex number in binary
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
        #This is an recursive call, thus we don't
        #expect any value in gr(gavage for simplicity)

    return resultant_binary_dec, resultant_binary_hex


# This function xor two string of same length
# or a whole string with single char or num
# This function only operates with hex values,
# so trying other than hex will produce a garbage value
def XOR(string1=None, string2=None, type=None):
    # since the length are expected to be same,
    # we can run a loop through the length on any one sting
    xor_result = ''
    if type == 'E':  # for equal length
        for index, str1 in enumerate(string1):
            # This does a xor operation, since xor can only be done in number,
            # I have converted to corresponding value and subtracted it by 87 to get hex
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


def find_if_real_eng_message(decoded_text):
    decoded_message = ''
    # return true or false
    return


def sift_ciphers(encText):
    # it has a key range always from 0 - 25
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
        # The operator used below is similar to tertary operator ?:, its "a if condition b"
        hex_holder = str(chr(int(num % 16) + 87)
                         if int(num % 16) > 9
                         else int(num % 16)) + hex_holder
        # num%16 will be in range 10-15 if alpha
        # Thus adding 87 will give corresponding ascii letter

        num = int(num / 16)

    return hex_holder


def main():
    print('Answer for the first problem')
    shift_ciphers_decoded_text_list = \
        ['hjizt5xvi5wz5hvyz5amjh5adiydib5qpgizmvwdgdodzn5viy5rmdodib5zskgjdon',
         'suzawnafy2kgew2ygsd2af2lzw2hjwkwfuw2gx2sf2svnwjksjq2:sulanw2gj2hskkanw;',
         'ftgr3lrlmxfl3tkx3vhggxvmxw3mh3max3bgmxkgxm?3pabva3atl3twoxkltkbxl',
         'vobrgvoys.dfchcqczH.sghopzwgv.gvofsr.gsqfsh.ysm.igwbu.dipzwq;ysm.qfmdhcufodvm',
         'nayknz6hwuanP6pnwjoiep6zwpw6qoejc6odwnaz6oaynap6gau6ajoqna6ykjbezajpehepu6wjz6ejpacnepu']

    for encoded_text in shift_ciphers_decoded_text_list:
        print(sift_ciphers(encoded_text))
    print("\nAnswer for the second probelem")

    print("Enter your decimal number to convert to hex"+'\n')
    num_to_convert = input()
    try:
        isinstance(int(num_to_convert),int)
        print("You num is " + num_to_convert + " and its corresponding hex value is 0x" + num_to_hex(int(num_to_convert)) +'\n')
    except Exception as e:
        print(num_to_convert+ "is not a valid decimal number \n")

    print('Answer for the third problem')
    hex_string = '''576974686f75742072616e646f6d6e6573732c''' \
                 '2063727970746f67726170687920776f756c6' \
                 '420626520696d706f737369626c6520626563' \
                 '6175736520616c6c206f7065726174696f6e7' \
                 '320776f756c64206265636f6d652070726564' \
                 '69637461626c652c20616e642074686572656' \
                 '66f726520696e7365637572652e'''
    print(base64_encoding(hex_string))

    print('\nAnswer for the forth problem')
    print(XOR('1c0111001f010100061a024b53535009181c','686974207468652062756c6c277320657965','E'))

    print('\nAnswer for the fifth problem')
    encoded = '3a09060c0705060d1b1b48011b480e071d060c480d1e0d1a' \
              '111f000d1a0d480106480b1a11181c070f1a091800115248' \
              '0106481c000d480f0d060d1a091c01070648070e481b0d0b1' \
              'a0d1c48030d111b44480106480d060b1a11181c010706481' \
              'b0b000d050d1b444809060c480d1e0d06480106481c000d4' \
              '8091c1c090b031b480706480b1a11181c071b111b1c0d051b46'''

    print(scxc.__single_char_XOR_cypher(encoded))


if __name__ == '__main__':
    main()
