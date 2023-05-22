from abc import ABC, abstractmethod


class AbstractLaptop(ABC):
    """
    A base abstract class representing a generic laptop.

    Attributes
    ----------
    MAX_BATTERY_CHARGE : int
        The maximum battery charge level for the laptop.

    Methods
    -------
    add_ram(value)
        Adds RAM to the laptop.
    add_storage(value)
        Adds storage to the laptop.
    charge()
        Charges the laptop's battery to the maximum level.
    replace_battery(capacity_in_hours)
        Abstract method to replace the laptop's battery with a new one.
    """

    MAX_BATTERY_CHARGE = 100

    def __init__(self, model="UNKNOWN", screen_size=15.6, ram=8, storage=256,
                 current_battery_life=20, battery_life=5, battery_charge=0):
        self.model = model
        self.screen_size = screen_size
        self.ram = ram
        self.storage = storage
        self.current_battery_life = current_battery_life
        self.battery_life = battery_life
        self.battery_charge = battery_charge

    def add_ram(self, value):
        """
        Adds RAM to the laptop.

        Parameters
        ----------
        value : int
            Indicates by how much to increase the RAM.

        Returns
        -------
        None
        """
        self.ram += value

    def add_storage(self, value):
        """
        Adds storage to the laptop.

        Parameters
        ----------
        value : int
            Indicates by how much to increase the storage.

        Returns
        -------
        None
        """
        self.storage += value

    def charge(self):
        """
        Charges the laptop's battery to the maximum level.

        Raises
        ------
        Exception
            If there is no reason to charge the battery (battery charge is already at maximum).

        Returns
        -------
        None
        """
        if self.battery_charge == AbstractLaptop.MAX_BATTERY_CHARGE:
            raise Exception("No reason to charge")
        self.battery_charge = AbstractLaptop.MAX_BATTERY_CHARGE

    @classmethod
    @abstractmethod
    def replace_battery(cls, capacity_in_hours):
        """
        Abstract method to replace the laptop's battery with a new one.

        Parameters
        ----------
        capacity_in_hours : int
            The capacity of the new battery in hours.

        Returns
        -------
        None
        """

    def __str__(self):
        attrs = self.__dict__
        attribute_dictionary = [
            f"{key.replace('_Laptop', '').capitalize()}: {value}"
            for key, value in attrs.items()
        ]
        return f"{self.__class__.__name__}({', '.join(attribute_dictionary)})"
