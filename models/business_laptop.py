"""
A module for representing Business Laptop

Classes:
    BusinessLaptop
"""
from Exceptions.exceptions import RedundantChargeException
from models.abstract_laptop import AbstractLaptop


class BusinessLaptop(AbstractLaptop):
    """
    A class representing a business laptop, inheriting from AbstractLaptop.

    Attributes
    ----------
    number_of_ports : int
        The number of ports available on the laptop.
    warranty_in_years : int
        The warranty period of the laptop in years.

    Methods
    -------
    replace_battery(capacity_in_hours)
        Method to replace the laptop's battery with a new one.
    """

    # pylint: disable=too-many-arguments
    def __init__(self, model="UNKNOWN", screen_size=15.6, ram=8, storage=256,
                 current_battery_life=20, battery_life=5, battery_charge=0,
                 number_of_ports=0, warranty_in_years=0):
        super().__init__(model, screen_size, ram, storage, current_battery_life,
                         battery_life, battery_charge)
        self.number_of_ports = number_of_ports
        self.warranty_in_years = warranty_in_years
        self.installed_programs = {"Program 1", "Program 2", "Program 3", "Program 4"}

    def replace_battery(self, capacity_in_hours):
        """
        Method to replace the laptop's battery with a new one.

        Parameters
        ----------
        capacity_in_hours : int
            The capacity of the new battery in hours.

        Returns
        -------
        None
        """

        if self.current_battery_life < capacity_in_hours:
            self.battery_life = capacity_in_hours
            self.current_battery_life = capacity_in_hours
        else:
            raise RedundantChargeException()
