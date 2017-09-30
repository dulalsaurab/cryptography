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
    #Though, I have incluced only etaoin, and its giving me accurate result all the time


    
    
'''We have give a hex encoded text, first we unhexlify function. Since the encryption is performed by xor each bit 
with one of the ascii character i.e. ranging from 0-255, we re-xor it to get the message back. Doing so, we will get
a big list i.e. list of list (big list in our case below). Now, we will pass each list to function 
robability_of_being_legit_string, and it will return our legit string. Voila!, you cracked it'''


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
