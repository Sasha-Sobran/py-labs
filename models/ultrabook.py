from models.abstract_laptop import AbstractLaptop


class Ultrabook(AbstractLaptop):

    def __init__(self, model="UNKNOWN", screen_size=15.6, ram=8, storage=256, current_battery_life=20, battery_life=5,
                 battery_charge=0, weight=0, thickness=0):
        super().__init__(model, screen_size, ram, storage, current_battery_life, battery_life, battery_charge)
        self.weight = weight,
        self.thickness = thickness

    def replace_battery(self, capacity_in_hours):
        print("Sorry, but you can`t replace battery in Ultrabook")
