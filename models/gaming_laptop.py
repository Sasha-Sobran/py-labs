"""
A module for representing Gaming Laptop

Classes:
    GamingLaptop
"""
from models.abstract_laptop import AbstractLaptop


class GamingLaptop(AbstractLaptop):
    """
    A class representing a gaming laptop, inheriting from AbstractLaptop.

    Attributes
    ----------
    number_of_fans : int
        The number of fans in the laptop for cooling.
    graphics_processor : str
        The graphics processor used in the laptop.

    Methods
    -------
    replace_battery(capacity_in_hours)
        Method to replace the laptop's battery with a new one.
    """

    # pylint: disable=too-many-arguments
    def __init__(self, model="UNKNOWN", screen_size=15.6, ram=8, storage=256,
                 current_battery_life=20, battery_life=5, battery_charge=0,
                 number_of_fans=0, graphics_processor=""):
        super().__init__(model, screen_size, ram, storage, current_battery_life,
                         battery_life, battery_charge)
        self.number_of_fans = number_of_fans
        self.graphics_processor = graphics_processor
        self.installed_programs = {"Game 1", "Game 2", "Game 3", "Game 4"}

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
            print("No reason to replace battery")
