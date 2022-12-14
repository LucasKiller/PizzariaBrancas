from abc import ABC, abstractmethod
from shared.domain.enums.flavor_enum import FLAVOR
from shared.domain.enums.price_enum import PRICE
from src.shared.domain.entities.order import Order


class IPizzariaRepository(ABC):

    @abstractmethod
    def create_order(self, table: int, flavor: FLAVOR, price: PRICE) -> Order:
        pass