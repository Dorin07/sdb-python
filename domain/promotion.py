class Promotion:
    def __init__(self, value, codes):
        self.__value = value
        self.__codes = codes

    def get_value(self):
        return self.__value

    def set_value(self, value):
        self.__value = value

    def get_codes(self):
        return self.__codes

    def set_codes(self, codes):
        self.__codes = codes

    def __repr__(self):
        return "Value: {0}, Codes: {1}".format(self.__value, self.__codes)

    def __str__(self):
        return "Value: {0}, Codes: {1}".format(self.__value, self.__codes)

    def __eq__(self, other):
        """
        Verify if two promotions have the same value
        :param other:
        :return:
        """
        return other.get_value() == self.__value

