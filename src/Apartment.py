from src.ResidentialBuilding import ResidentialBuilding


class Apartment(ResidentialBuilding):

    def __init__(self, price, square_meters, address, year_built, floor_number):
        super().__init__(price, square_meters, address, year_built)
        self._floor_number = floor_number

    def show_price(self):
        print(f"Wartość mieszkania o id: {self.get_id()} wynosi: {self._price}")

    def show_address(self):
        print(f"Adres mieszkania to: {self._address}")

    def show_square_meters(self):
        print(f"Powierzchnia mieszkania wynsoi: {self._square_meters}")

    def show_availability(self):
        if self.is_available():
            print('Mieszkanie jest dostępne/możliwe do kupienia')
        else:
            print('Mieszkanie jest sprzedane/niedostępne do kupienia')

    def show_basic_info(self):
        self.show_price()
        self.show_square_meters()
        self.show_availability()
        self.show_address()
        print(f"Rok budowy budynku: {self._year_built}")
        print(f"Numer piętra mieszkania: {self._floor_number}")
        print('Wybrana nieruchomość jest mieszkaniem\n')
