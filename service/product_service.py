import json
from domain.product import Product
from repository.in_memory_repository import InMemoryRepository


class ProductService:
    def __init__(self, repository: InMemoryRepository):
        """
        Constructor of ProductService class
        Upload data from JSON file
        """
        self.__repository = repository

        try:
            with open("data/product.json", "r") as product_file:
                json_f = json.load(product_file)
                product_f = json_f["product"]
                for product in product_f:
                    self.__repository.add(
                        Product(product["id"],
                                product["name"],
                                product["company"],
                                product["price"],
                                product["amount"])
                    )
        except FileNotFoundError:
            print("Product don't found! -> product.json doesn't exist!")

    def add_product(self, product):
        """
        Add a product to the list
        :param product: The new product
        """
        self.__repository.add(product)

    def delete_product(self, id):
        """
        Delete a product after id
        :param id: id after the product will be delete
        """
        position = self.__repository.find_position(Product(id, " ", " ", 0.0, 0.0))
        if position == -1:
            raise ValueError("The product does not exist!")
        self.__repository.delete(position)

    def get_all_products(self):
        """
        Returns all products to the ConsoleUI
        :return: the list of all products
        """
        return self.__repository.get_all()

    def update_product(self, id, new_product: Product):
        """
        Update a product, and modify the json file: product.json
        :param id: The id after product will be  update
        :param new_product: The new data of product
        :return: None
        """
        position = self.__repository.find_position(Product(id, " ", " ", 0.0, 0.0))
        if position == -1:
            raise ValueError("The product does not exist!")
        else:
            self.__repository.update(new_product, position)

        json_file = open("data/product.json", "r")  # Open the JSON file for reading
        data = json.load(json_file)  # Read the JSON into the buffer
        product_f = data["product"]
        json_file.close()  # Close the JSON file

        # Save our changes to JSON file
        for product in product_f:
            if id == product["id"]:
                json_file = open("data/product.json", "w+")
                product["id"] = new_product.get_id()
                product["name"] = new_product.get_name()
                product["company"] = new_product.get_company()
                product["price"] = new_product.get_price()
                product["amount"] = new_product.get_amount()
                json_file.write(json.dumps(data))
                json_file.close()

    def buy_product(self, id, new_product: Product):
        """
        Update a product after the customer bought it, and modify the json file: product.json
        :param id: The id after product will be bought
        :param new_product: The new data of product, the new amount
        :return: None
        """
        position = self.__repository.find_position(Product(id, " ", " ", 0.0, 0.0))
        if position == -1:
            raise ValueError("The product does not exist!")
        else:
            products = self.get_all_products()
            id = products[position].get_id()
            name = products[position].get_name()
            company = products[position].get_company()
            price = products[position].get_price()
            amount = products[position].get_amount()
            new_amount = new_product.get_amount()
            new_product.set_id(id)
            new_product.set_name(name)
            new_product.set_company(company)
            new_product.set_price(price)
            new_product.set_amount(amount-new_amount)
            if(amount < new_amount):
                raise ValueError("Insufficient amount of product!")
            else:
                self.__repository.update(new_product, position)

        json_file = open("data/product.json", "r")  # Open the JSON file for reading
        data = json.load(json_file)  # Read the JSON into the buffer
        product_f = data["product"]
        json_file.close()  # Close the JSON file

        # Save our changes to JSON file
        for product in product_f:
            if id == product["id"]:
                json_file = open("data/product.json", "w+")
                product["id"] = new_product.get_id()
                product["name"] = new_product.get_name()
                product["company"] = new_product.get_company()
                product["price"] = new_product.get_price()
                product["amount"] = new_product.get_amount()
                json_file.write(json.dumps(data))
                json_file.close()
