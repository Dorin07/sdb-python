import json
from domain.promotion import Promotion
from repository.in_memory_repository import InMemoryRepository


class PromotionService:
    def __init__(self, repository: InMemoryRepository):
        """
        Constructor of PromotionService class
        Upload data from JSON file
        """
        self.__repository = repository

        try:
            with open("data/promotion.json", "r") as promotion_file:
                json_f = json.load(promotion_file)
                promotion_f = json_f["promotion"]
                for promotion in promotion_f:
                    self.__repository.add(
                        Promotion(promotion["value"],
                                  promotion["codes"])
                    )
        except FileNotFoundError:
            print("Promotion don't found! -> promotion.json doesn't exist!")

    def add_promotion(self, promotion):
        """
        Add a promotion to the list
        :param promotion: The new promotion
        """
        self.__repository.add(promotion)

    def delete_promotion(self, value):
        """
        Delete a promotion after value
        :param value: Value after the promotion would be deleted from the list
        """
        position = self.__repository.find_position(Promotion(value, []))
        if position == -1:
            raise ValueError("The promotion does not exist!")
        self.__repository.delete(position)

    def get_all_promotions(self):
        """
        Returns all promotions
        :return: All promotions
        """
        return self.__repository.get_all()

    def update_promotion(self, value, new_promotion: Promotion):
        """
        Update a promotion after value, and modify the json file: promotion.json
        :param value: value of old promotion
        :param new_promotion: New promotion entity
        """
        position = self.__repository.find_position(Promotion(value, []))
        if position == -1:
            raise ValueError("The promotion does not exist!")
        else:
            self.__repository.update(new_promotion, position)

        json_file = open("data/promotion.json", "r")  # Open the JSON file for reading
        data = json.load(json_file)  # Read the JSON into the buffer
        promotion_f = data["promotion"]
        json_file.close()  # Close the JSON file

        # Save our changes to JSON file
        for promotion in promotion_f:
            if id == promotion["id"]:
                json_file = open("data/promotion.json", "w+")
                promotion["value"] = new_promotion.get_value()
                promotion["codes"] = new_promotion.get_codes()
                json_file.write(json.dumps(data))
                json_file.close()
