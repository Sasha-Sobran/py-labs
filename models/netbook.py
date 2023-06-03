"""
A module for representing Netbook

Classes:
    Netbook
"""
from Exceptions.exceptions import RedundantChargeException
from models.abstract_laptop import AbstractLaptop


class Netbook(AbstractLaptop):
    """
    A class representing a netbook, inheriting from AbstractLaptop.

    Attributes
    ----------
    operating_system : str
        The operating system installed on the netbook.
    web_cam : str
        Indicates the availability of a web camera in the netbook.

    Methods
    -------
    replace_battery(capacity_in_hours)
        Method to replace the laptop's battery with a new one.
    """

    # pylint: disable=too-many-arguments
    def __init__(self, model="UNKNOWN", screen_size=15.6, ram=8, storage=256,
                 current_battery_life=20, battery_life=5, battery_charge=0,
                 operating_system="", web_cam=""):
        super().__init__(model, screen_size, ram, storage, current_battery_life,
                         battery_life, battery_charge)
        self.operating_system = operating_system
        self.web_cam = web_cam
        self.installed_programs = {"Program A", "Program B", "Program C", "Program D"}

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
