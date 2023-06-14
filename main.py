from manager.laptop_manager import AbstractLaptopManager
from models.ultrabook import Ultrabook

if __name__ == '__main__':
    manager = AbstractLaptopManager()
    manager.add_laptop(Ultrabook())
    manager.add_laptop(Ultrabook())
    manager.add_laptop(Ultrabook())
    manager.add_laptop(Ultrabook())
    ultrabook = Ultrabook()
    ultrabook.replace_battery(2)
