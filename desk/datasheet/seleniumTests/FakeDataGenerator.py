# from abc import ABC, abstractmethod
from faker import Faker


class FakeDataGenerator(Faker):
    # , Faker
    # @abstractmethod
    def __init__(self) -> None:
        """
        Initialize Faker() in localization eng
        :return: object faker
        :rtype: None
        """
        super().__init__(['en_US'])

    def fake_name(self) -> None:
        return self.name()

    def __del__(self):
        pass
