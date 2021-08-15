from repository.in_memory_repository import InMemoryRepository
from service.product_service import ProductService
from service.promotion_service import PromotionService
from service.statistics_service import StatisticsService
from ui.console_ui import ConsoleUI

if __name__ == '__main__':

    product_repository = InMemoryRepository()
    promotion_repository = InMemoryRepository()

    product_service = ProductService(product_repository)
    promotion_service = PromotionService(promotion_repository)
    statistics_service = StatisticsService(product_service, promotion_service)
    console_ui = ConsoleUI(product_service, promotion_service, statistics_service)
    console_ui.run()