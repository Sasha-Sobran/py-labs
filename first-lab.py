class Laptop:
    """
    A class to represent a laptop.
    ...

    Attributes
    ----------
    model : str
        model of the laptop.
    screen_size : float
        screen size of the laptop in inches.
    ram : int
        The amount of RAM in the laptop in gigabytes.
    storage : int
        The amount of storage in the laptop in gigabytes.
    battery_life : int
        The battery life of the laptop in hours.
    battery_charge : int
        The current battery charge of the laptop as a percentage.

    Methods
    -------
    add_ram(value):
        adds RAM to the laptop.
    add_storage(value):
        adds storage to the laptop.
    charge():
        charges Laptop.
    """

    MAX_BATTERY_CHARGE = 100
    instance = None

    def __init__(self, __model="UNKNOWN", __screen_size=15.6, __ram=8, __storage=256, __battery_life=5,
                 __battery_charge=0):
        self.__model = __model
        self.__screen_size = __screen_size
        self.__ram = __ram
        self.__storage = __storage
        self.__battery_life = __battery_life
        self.__battery_charge = __battery_charge

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        self.__model = value

    @property
    def screen_size(self):
        return self.__screen_size

    @screen_size.setter
    def screen_size(self, value):
        self.__screen_size = value

    @property
    def ram(self):
        return self.__ram

    @ram.setter
    def ram(self, value):
        self.__ram = value

    @property
    def storage(self):
        return self.__storage

    @storage.setter
    def storage(self, value):
        self.__storage = value

    @property
    def battery_life(self):
        return self.__battery_life

    @battery_life.setter
    def battery_life(self, value):
        self.__battery_life = value

    @property
    def battery_charge(self):
        return self.__battery_charge

    @battery_charge.setter
    def battery_charge(self, value):
        self.__battery_charge = value

    @staticmethod
    def get_instance():
        if Laptop.instance is None:
            Laptop.instance = Laptop()
        return Laptop.instance

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
        self.__ram += value

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
        self.__storage += value

    def charge(self):
        """
        Charges the laptop.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        if self.__battery_charge == Laptop.MAX_BATTERY_CHARGE:
            raise Exception("no reason to charge")
        else:
            self.__battery_charge = Laptop.MAX_BATTERY_CHARGE

    def __str__(self):
        attrs = {
            'model': self.__model,
            'screen_size': self.__screen_size,
            'ram': self.__ram,
            'storage': self.__storage,
            'battery_life': self.__battery_life,
            'battery_charge': self.__battery_charge
        }
        docstring = [f"{key.capitalize()}: {attrs[key]}" for key in attrs]
        return f"{self.__class__.__name__}({', '.join(docstring)})"


if __name__ == '__main__':

    laptop_list = [
        Laptop(),
        Laptop("Asus", 17, 16, 512, 10, 20),
        Laptop.get_instance(),
        Laptop.get_instance()
    ]

    for laptop in laptop_list:
        print(laptop)
