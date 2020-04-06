import re


class Range(object):

    def __init__(self, string = "a-zA-Z0-9"):

        self.__range = re.findall("(.-.)", string)

    def __iter__(self):

        self.__index = -1
        return self

    def __next__(self):

        self.__index += 1

        if self.__index < len(self.__range):
            return self.__range[self.__index].split("-")
        raise StopIteration


def get_charset_from_file(filename, excludes = ["\n", " "]):

    """
    Retorna uma lista com todos os caracteres de um arquivo
    """

    charset = []

    with open(filename) as file:

        for char in file.read():

            if not char in charset and not char in excludes: 
                charset.append(char)

    return charset


def get_charset_from_range(range_obj):

    """
    Recebe um objeto de Range e retorna uma lista de caracteres. 
    """

    if not isinstance(range_obj, Range):
        raise TypeError('The "range_obj" parameter must be an instance of Range.')

    charset = []

    for range_ in range_obj:

        start = ord(range_[0])
        stop = ord(range_[1])

        charset.extend([chr(char_id) for char_id in range(start, stop + 1)])

    return charset


def get_default_charset():

    """
    Retorna uma lista com os caracteres [A-Z a-z 0-9]
    """

    range_ = Range("A-Za-z0-9")
    return get_charset_from_range(range_)


    
