"""
A module for laptop management

Classes:
    AbstractLaptopManager
"""
from Exceptions.exceptions import TooManyCallsException
from decorators.laptop_decorator import count_of_arguments, limit_calls, logged
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

    def __init__(self, laptops: list[AbstractLaptop] = None):
        self.laptops = laptops if laptops else []

    def __len__(self):
        return len(self.laptops[::-1])

    def __getitem__(self, index):
        if index < 0:
            return self.laptops[0]
        if index <= len(self.laptops) - 1:
            return self.laptops[index]
        return self.laptops[len(self.laptops) - 1]

    def __iter__(self):
        return iter(self.laptops[::-1])

    @logged(TooManyCallsException, "file")
    @limit_calls(3)
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

    def find_laptops_with_ram_value(self, value: int) -> list[AbstractLaptop]:
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

    def find_gaming_laptops(self) -> list[GamingLaptop]:
        """
        Finds gaming laptops in the laptop manager.

        Returns
        -------
        List[GamingLaptop]
            A list of gaming laptops in the laptop manager.
        """

        return [laptop for laptop in self.laptops if isinstance(laptop, GamingLaptop)]

    # pylint: disable=line-too-long
    def laptop_status_list(self):
        """
           Returns a list of battery statuses for each laptop in the collection.

           Returns
           -------
           list[str]
               A list of battery statuses, indicating the battery status ("Low", "Medium", or "High")
               for each laptop in the collection.
           """
        return [laptop.battery_status() for laptop in self.laptops]

    def laptop_enumerate(self):
        """
        Enumerates and prints the laptops in the laptop manager.

        Returns the index and details of each laptop in the laptop manager.

        Returns
        -------
        None
        """
        return enumerate(self.laptops)

    @count_of_arguments
    def status_of_laptops_charge(self):
        """
        Prints the status of the laptops' battery charge.

        Prints the battery status of each laptop in the laptop manager.

        Returns
        -------
        None
        """
        return zip(self.laptops, self.laptop_status_list())

    def check_condition_all_any(self, value):
        """
        Checks if all objects in the manager list satisfy the given condition,
        and if at least one object satisfies the condition.

        Parameters
        ----------

        Returns
        -------
        dict
            A dictionary with keys "all" and "any" and corresponding boolean values.
        """
        all_satisfy = all(laptop.ram > value for laptop in self.laptops)
        any_satisfy = any(laptop.ram > value for laptop in self.laptops)
        return {"all": all_satisfy, "any": any_satisfy}
