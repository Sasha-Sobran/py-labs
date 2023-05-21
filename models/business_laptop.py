from models.abstract_laptop import AbstractLaptop


class BusinessLaptop(AbstractLaptop):

    def __init__(self, model="UNKNOWN", screen_size=15.6, ram=8, storage=256, current_battery_life=20, battery_life=5,
                 battery_charge=0, number_of_ports=0, warranty_in_years=0):
        super().__init__(model, screen_size, ram, storage, current_battery_life, battery_life, battery_charge)
        self.number_of_ports = number_of_ports,
        self.warranty_in_years = warranty_in_years

    def replace_battery(self, capacity_in_hours):
        if self.current_battery_life < capacity_in_hours:
            self.battery_life=capacity_in_hours
            self.current_battery_life = capacity_in_hours
        else:
            print("No reason to replace battery")
