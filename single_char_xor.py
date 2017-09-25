# Single byte XOR cipher.
# https://en.wikipedia.org/wiki/Etaoin_shrdlu

import binascii
import collections


def probability_of_being_legit_string(string):
    # According to english letter frequency table,
    # "etaoin shrdlu" is a most frequent english
    # letters in words -  from heigher to lower frequency of occurence

    return string.count(' ') + string.count('e') + string.count('t') + string.count('a') + string.count(
        'o') + string.count('i') + string.count('n')
    # Including all the “etaoin shrdul”, will maximize
    # the given function, and hence also the accuracy of the prediction.


def __single_char_XOR_cypher(encoded):
    # Given hex text
    nums = binascii.unhexlify(encoded)
    big_list = []
    for key in range(256):
        arr = ''
        for num in nums:
            arr = arr + chr(num ^ key)
        big_list.append(arr)
    return max(big_list, key=probability_of_being_legit_string)

    # There are 256 possibilities of characters i.e 2 hex digits i.e ff
