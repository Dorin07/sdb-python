class InMemoryRepository:
    def __init__(self):
        self.__entities = []

    def add(self, new_entity):
        for entity in self.__entities:
            if entity == new_entity:
                raise ValueError("The entity already exist!")
        self.__entities.append(new_entity)

    def delete(self, position):
        del self.__entities[position]

    def update(self, new_entity, position):
        self.__entities[position] = new_entity

    def get_all(self):
        return self.__entities

    def find_position(self, entity):
        for i in range(len(self.__entities)):
            if entity == self.__entities[i]:
                return i
        return -1