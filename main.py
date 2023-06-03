from models.netbook import Netbook
from models.ultrabook import Ultrabook

if __name__ == '__main__':
    ultrabook = Netbook()
    ultrabook2 = Netbook()
    ultrabook.replace_battery(39)
    ultrabook2.replace_battery(1)
