from domain.promotion import Promotion
from domain.product import Product
from service.product_service import ProductService
from service.promotion_service import PromotionService
from service.statistics_service import StatisticsService


class ConsoleUI:
    def __init__(self, product_service: ProductService, promotion_service: PromotionService,
                 statistics_service: StatisticsService):
        """
        The constructor of the ConsoleUI class
        :param product_service: the service of the product entity service
        :param promotion_service: the service of the promotion entity service
        :param statistics_service: the service of statistics
        """
        self.__product_service = product_service
        self.__promotion_service = promotion_service
        self.__statistics_service = statistics_service

    def __add_product(self):
        """
        Add a new product on the list
        """
        id = input("Enter the id of the product: ")
        name = input("Enter the name of the product: ")
        company = input("Enter the company of the product: ")
        price = int(input("Enter the price of the product: "))
        amount = int(input("Enter the amount of the product: "))
        self.__product_service.add_product(Product(id, name, company, price, amount))
        print("Product added successfully!")

    def __delete_product(self):
        """
        Delete a product of the list after id
        """
        id = input("Barecode of the product you want to delete: ")
        self.__product_service.delete_product(id)
        print("Product deleted successfully!")

    def __print_all_products(self):
        """
        Print all the products on the list
        :return:
        """
        products = self.__product_service.get_all_products()
        for product in products:
            print(product)

    def __print_product_company(self):
        """
        Print all the products from a certain company
        """
        products = self.__statistics_service.company_product()
        company = input("Company you like to see the products: ")
        are_products = False
        for product in products:
            if product.get_company() == company:
                print(product)
                are_products = True
        if are_products == False:
            print("We don't have products from", company, "company")

    def __update_product(self):
        """
        Update a product after id
        """
        barecode = input("Barecode of the product you want to edit: ")
        new_barecode = input("Enter the new barecode of the product: ")
        new_name = input("Enter the new name of the product: ")
        new_company = input("Enter the new company of the product: ")
        new_price = int(input("Enter the new price of the product: "))
        new_amount = int(input("Enter the new amount of products: "))
        self.__product_service.update_product(barecode, Product(new_barecode, new_name, new_company, new_price, new_amount))
        print("Product updated successfully!")

    def __add_promotion(self):
        """
        Add a new promotion on the list
        """
        value = int(input("Value of promotion: "))
        n = int(input("Enter the numbers of the products you want to have this promotion: "))
        products = []
        for i in range(0, n):
            prod = input("Enter the barecode of the product: ")
            products.append(prod)
        self.__promotion_service.add_promotion(Promotion(value, products))
        print("Promotion added successfully!")

    def __buy_product(self):
        """
        Buy a product.
        :return: Buy an amount product and erase the quantity.
        """
        barecode = input("Please enter the barecode of the product: ")
        amount = int(input("Please insert the amount of the product: "))
        self.__product_service.buy_product(barecode, Product(" ", " ", " ", 0.0, amount))
        print("Products bought successfully!")

    def __print_smaller_price(self):
        """
        Returns the products which have a smaller price then a given price
        :return:
        """
        price = int(input("Please insert a price after which the others products you want to see: "))
        products = self.__statistics_service.smaller_price()
        are_products = False
        for product in products:
            if product.get_price() <= price:
                print(product)
                are_products = True
        if are_products == False:
            print("We don't have product which have a smaller price then", price)

    def __print_admin_menu(self):
        print("Options:\n"
              "1. Add a product\n"
              "2. Delete a product after barcode\n"
              "3. Update a product after barcode\n"
              "4. See all the products\n"
              "5. See all the products from a certain company\n"
              "6. Add a promotion for one or more products\n"
              "0. Back")

    def __print_customer_menu(self):
        print("Options:\n"
              "1. Buy a product\n"
              "2. See all the products\n"
              "3. See all the products with a smaller price then a given price\n"
              "0. Back")

    def __print_menu(self):
        print("Options:\n"
              "1. Admin\n"
              "2. Customer \n"
              "0. Exit")

    def run(self):
        while True:
            self.__print_menu()
            command = input("\nEnter the command ").strip()
            try:
                if command == '0':
                    break
                elif command == '1':
                    while True:
                        self.__print_admin_menu()
                        command_1 = input("\nEnter the command ").strip()
                        try:
                            if command_1 == '0':
                                break
                            elif command_1 == '1':
                                self.__add_product()
                            elif command_1 == '2':
                                self.__delete_product()
                            elif command_1 == '3':
                                self.__update_product()
                            elif command_1 == '4':
                                self.__print_all_products()
                            elif command_1 == '5':
                                self.__print_product_company()
                            elif command_1 == '6':
                                self.__add_promotion()
                            else:
                                print("Not a valid command!")
                        except Exception as ex:
                            print(ex)
                elif command == '2':
                    while True:
                        self.__print_customer_menu()
                        command_1 = input("\nEnter the command ").strip()
                        try:
                            if command_1 == '0':
                                break
                            elif command_1 == '1':
                                self.__buy_product()
                            elif command_1 == '2':
                                self.__print_all_products()
                            elif command_1 == '3':
                                self.__print_smaller_price()
                            else:
                                print("Not a valid command!")
                        except Exception as ex:
                            print(ex)
                else:
                    print("Not a valid command!")
            except Exception as ex:
                print(ex)
