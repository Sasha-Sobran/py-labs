from models.business_laptop import BusinessLaptop
from models.gaming_laptop import GamingLaptop
from models.netbook import Netbook
from models.ultrabook import Ultrabook
from manager.laptop_manager import AbstractLaptopManager

if __name__ == '__main__':
    manager = AbstractLaptopManager()

    manager.add_laptop(Ultrabook("Dell XPS 13", 13.3, 16, 2048, 12, 15, 12, 1.2, 14.8))
    manager.add_laptop(Netbook("Asus VivoBook Flip 14 TP412FA", 14, 8, 512, 9, 15, 12, "Windows 10 Home", "HD"))
    manager.add_laptop(GamingLaptop("ASUS ROG Zephyrus G14", 14, 16, 1024, 10, 15, 2, 2, "NVIDIA GeForce RTX 2060"))
    manager.add_laptop(BusinessLaptop("Lenovo ThinkPad X1 Carbon Gen 9", 14, 16, 512, 20, 12, 25, 6, 3))
    manager.add_laptop(GamingLaptop())
    manager.add_laptop(Ultrabook())
    manager.add_laptop(Netbook())
    manager.add_laptop(BusinessLaptop())

    print("Laptops: ")
    for laptop in manager.laptops:
        print(laptop)

    print("Laptops with 8 ram:")
    for laptop in manager.find_laptops_with_ram_value(8):
        print(laptop)

    print("Gaming laptops: ")
    for laptop in manager.find_gaming_laptops():
        print(laptop)
