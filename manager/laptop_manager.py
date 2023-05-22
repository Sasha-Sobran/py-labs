from typing import List

from models.abstract_laptop import AbstractLaptop
from models.gaming_laptop import GamingLaptop


class AbstractLaptopManager:
    """
    A class representing a laptop manager.

    Attributes
    ----------
    laptops : List[AbstractLaptop]
        A list of AbstractLaptop objects.

    Methods
    -------
    add_laptop(laptop: AbstractLaptop)
        Adds a laptop to the laptop manager.
    find_laptops_with_ram_value(value: int) -> List[AbstractLaptop]
        Finds laptops with a specific RAM value.
    find_gaming_laptops() -> List[GamingLaptop]
        Finds gaming laptops in the laptop manager.
    """

    def __init__(self, laptops: List[AbstractLaptop] = None):
        self.laptops = laptops if laptops else []

    def add_laptop(self, laptop: AbstractLaptop):
        """
        Adds a laptop to the laptop manager.

        Parameters
        ----------
        laptop : AbstractLaptop
            The laptop to be added.

        Returns
        -------
        None
        """

        self.laptops.append(laptop)

    def find_laptops_with_ram_value(self, value: int) -> List[AbstractLaptop]:
        """
        Finds laptops with a specific RAM value.

        Parameters
        ----------
        value : int
            The RAM value to search for.

        Returns
        -------
        List[AbstractLaptop]
            A list of laptops with the specified RAM value.
        """

        return [laptop for laptop in self.laptops if laptop.ram == value]

    def find_gaming_laptops(self) -> List[GamingLaptop]:
        """
        Finds gaming laptops in the laptop manager.

        Returns
        -------
        List[GamingLaptop]
            A list of gaming laptops in the laptop manager.
        """

        return [laptop for laptop in self.laptops if isinstance(laptop, GamingLaptop)]
