from urlshortener.core import app
from string import digits, ascii_lowercase, ascii_uppercase
from math import floor

class IntEncoder(object):
    DICT = ascii_uppercase + digits + ascii_lowercase

    def __init__(self, dictionary = DICT):
        self.DICT = dictionary 

    def encode(self, num_to_encode, dictionary=DICT):
        if num_to_encode == 0:
            return dictionary[0]
        arr = []
        dict_len = len(dictionary)
        while num_to_encode:
            num_to_encode, remainder = divmod(num_to_encode, dict_len)
            arr.append(dictionary[remainder])
        arr.reverse()
        return ''.join(arr)


    def decode(self, string, dictionary=DICT):
        dict_len = len(dictionary)
        strlen = len(string)
        num = 0

        idx = 0
        for char in string:
            power = (strlen - (idx + 1))
            num += dictionary.index(char) * (dict_len ** power)
            idx += 1

        return num
