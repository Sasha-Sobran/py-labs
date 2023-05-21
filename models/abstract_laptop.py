from abc import ABC, abstractmethod


class AbstractLaptop(ABC):
    MAX_BATTERY_CHARGE = 100

    def __init__(self, model="UNKNOWN", screen_size=15.6, ram=8, storage=256, current_battery_life=20, battery_life=5,
                 battery_charge=0):
        self.model = model
        self.screen_size = screen_size
        self.ram = ram
        self.storage = storage
        self.current_battery_life = current_battery_life
        self.battery_life = battery_life
        self.battery_charge = battery_charge

    def add_ram(self, value):
        """
        Adds Ram to the laptop.

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
        adds storage to the laptop.

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
        if self.battery_charge == AbstractLaptop.MAX_BATTERY_CHARGE:
            raise Exception("no reason to charge")
        else:
            self.battery_charge = AbstractLaptop.MAX_BATTERY_CHARGE

    @classmethod
    @abstractmethod
    def replace_battery(cls, capacity_in_hours):
        pass

    def __str__(self):
        attrs = self.__dict__
        attribute_dictionary = [f"{key.replace('_Laptop', '').capitalize()}: {attrs[key]}" for key in attrs]
        return f"{self.__class__.__name__}({', '.join(attribute_dictionary)})"
