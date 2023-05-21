from typing import List

from models.abstract_laptop import AbstractLaptop
from models.gaming_laptop import GamingLaptop


class AbstractLaptopManager:
    def __init__(self, laptops: List[AbstractLaptop] = None) -> None:
        self.laptops = laptops if laptops else []

    def add_laptop(self, laptop: AbstractLaptop):
        self.laptops.append(laptop)

    def find_laptops_with_ram_value(self, value: int) -> List[AbstractLaptop]:
        return [laptop for laptop in self.laptops if laptop.ram == value]

    def find_gaming_laptops(self) -> List[GamingLaptop]:
        return [laptop for laptop in self.laptops if isinstance(laptop, GamingLaptop)]
