"""
A module for managing sets of installed programs from a laptop manager.

Classes:
    SetManager
"""
from manager.laptop_manager import AbstractLaptopManager


class SetManager:
    """
       A class representing a set manager that iterates over installed programs of laptops in an
       AbstractLaptopManager.

       Attributes
       ----------
       manager : AbstractLaptopManager
           The AbstractLaptopManager instance to manage sets from.
    """

    def __init__(self, manager):
        self.manager = manager
        self.current_index = 0

    def __iter__(self):
        for laptop in self.manager:
            for set_item in laptop.installed_programs:
                yield set_item

    def __len__(self):
        length = 0
        for laptop in self.manager:
            length += len(laptop.installed_programs)
        return length

    def __getitem__(self, index):
        return self.manager[index].installed_programs

    def __next__(self):
        if self.current_index > len(self):
            raise StopIteration
        current_iteration = self.manager[self.current_index].installed_programs
        self.current_index += 1
        return current_iteration
