class Product:
    def __init__(self, id, name, company, price, amount):
        self.__id = id
        self.__name = name
        self.__company = company
        self.__price = price
        self.__amount = amount

    def get_id(self):
        return self.__id

    def set_id(self, value):
        self.__id = value

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_company(self):
        return self.__company

    def set_company(self, company):
        self.__company = company

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_amount(self):
        return self.__amount

    def set_amount(self, amount):
        self.__amount = amount

    def __repr__(self):
        return "Id: {0}, Name: {1}, Company: {2}, Price: {3}, Amount: {4}".format(self.__id, self.__name, self.__company,
                                                                                 self.__price,
                                                                                 self.__amount)

    def __str__(self):
        return "Id: {0}, Name: {1}, Company: {2}, Price: {3}, Amount: {4}".format(self.__id, self.__name, self.__company,
                                                                                 self.__price,
                                                                                 self.__amount)

    def __eq__(self, other):
        """
        Verify if two products are the same/equal
        :param other:
        :return:
        """
        return other.get_id() == self.__id
