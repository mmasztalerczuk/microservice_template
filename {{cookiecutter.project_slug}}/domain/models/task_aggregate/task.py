from domain.models.seedworks.entity import Entity


class Task(Entity):
    __slots__ = ['name']

    def __init__(self, name: str):
        self.name = name
