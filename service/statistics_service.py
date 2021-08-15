from service.product_service import ProductService
from service.promotion_service import PromotionService


class StatisticsService:
    def __init__(self, product_service: ProductService, promotion_service: PromotionService):
        self.__product_service = product_service
        self.__promotion_service = promotion_service

    def company_product(self):
        """
        Calculate the all the product from a company
        :return: All the products of the same company
        """
        products = self.__product_service.get_all_products()
        return products

    def smaller_price(self):
        """
        Sort the products descending to be able later to get only the products with a smaller price then
        the price we give.
        :return: The sorted list.
        """
        products = self.__product_service.get_all_products()
        sort = False
        while sort == False:
            sort = True
            for i in range(len(products) - 1):
                if products[i].get_price() < products[i + 1].get_price():
                    aux = products[i]
                    products[i] = products[i + 1]
                    products[i + 1] = aux
                    sort = False
        return products