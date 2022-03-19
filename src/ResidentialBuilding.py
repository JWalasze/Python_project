from abc import ABC, abstractmethod


class ResidentialBuilding(ABC):

    id = 0

    def __init__(self, price, square_meters, address, year_built):
        self._price = price
        self._square_meters = square_meters
        self._address = address
        self._year_built = year_built
        self._availability = True
        ResidentialBuilding.id += 1
        self._id = ResidentialBuilding.id

    @abstractmethod
    def show_price(self):
        pass

    @abstractmethod
    def show_square_meters(self):
        pass

    def is_available(self):
        if self._availability:
            return True
        else:
            return False

    @abstractmethod
    def show_availability(self):
        pass

    @abstractmethod
    def show_address(self):
        pass

    @abstractmethod
    def show_basic_info(self):
        pass

    def change_price(self, value, up_or_down):
        if up_or_down == 'up':
            self._price += self._price * value / 100
        elif up_or_down == 'down':
            self._price -= self._price * value / 100
        else:
            print('Operacja zmiany ceny nie powiodła się!')

    def change_availability(self):
        if self._availability:
            self._availability = False
        else:
            self._availability = True

    def sell_building(self):
        self.change_availability()

    @property
    def price(self):
        return self._price

    @property
    def square_meters(self):
        return self._square_meters

    @property
    def address(self):
        return self._address

    @property
    def year_built(self):
        return self._year_built

    def get_id(self):
        return self._id
