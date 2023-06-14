"""
Module for AbstractLaptop
"""
from abc import ABC, abstractmethod
from typing import final, Final

from Exceptions.exceptions import RedundantChargeException


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

    MAX_BATTERY_CHARGE: Final[int] = 100

    # pylint: disable=too-many-instance-attributes
    # pylint: disable=too-many-arguments
    def __init__(self, model="UNKNOWN", screen_size=15.6, ram=8, storage=256,
                 current_battery_life=20, battery_life=5, battery_charge=0, installed_programs=None):
        self.model = model
        self.screen_size = screen_size
        self.ram = ram
        self.storage = storage
        self.current_battery_life = current_battery_life
        self.battery_life = battery_life
        self.battery_charge = battery_charge
        self.installed_programs = installed_programs

    @final
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

    @final
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

    @final
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
            raise RedundantChargeException
        self.battery_charge = AbstractLaptop.MAX_BATTERY_CHARGE

    @abstractmethod
    def replace_battery(self, capacity_in_hours):
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

    def battery_status(self):
        """
        Returns the battery status of the laptop based on the current battery charge level.

        Returns
        -------
        str
            The battery status, which can be "Low", "Medium", or "High".
        """
        if self.battery_charge < 30:
            return "Need charge"
        if self.battery_charge < 70:
            return "Dont need charge"
        return "DONT NEED CHARGE"

    # pylint: disable=line-too-long
    def get_attributes_by_type(self, data_type=None):
        """
        Returns a dictionary with attributes and values of object based on the specified data type,
        or the entire dictionary if no data type is provided.

        Parameters
        ----------
        data_type : type, optional
            The data type to filter the attributes. Default is None.

        Returns
        -------
        dict
            A dictionary containing the attributes and values of the object that match the specified
             data type, or the entire dictionary if no data type is provided.
        """
        if data_type is not None:
            return {key: value for key, value in self.__dict__.items() if isinstance(value, data_type)}
        return self.__dict__

    def __str__(self):
        attrs = self.__dict__
        attribute_dictionary = [
            f"{key.replace('_Laptop', '').capitalize()}: {value}"
            for key, value in attrs.items()
        ]
        return f"{self.__class__.__name__}({', '.join(attribute_dictionary)})"
