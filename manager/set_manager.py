from manager.laptop_manager import AbstractLaptopManager


class SetManager:
    def __init__(self, manager: AbstractLaptopManager):
        self.manager = manager
        self.current_index = -1

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
        self.current_index += 1
        return self.manager[self.current_index].installed_programs
