from src.ResidentialBuilding import ResidentialBuilding


class DetachedHouse(ResidentialBuilding):

    def __init__(self, price, square_meters, address, year_built, floors):
        super().__init__(price, square_meters, address, year_built)
        self._floors = floors

    def show_price(self):
        print(f"Cena domu o id: {self._id} wynosi: {self._price}$")

    def show_square_meters(self):
        print(f"Powierzchnia domu wynosi: {self._square_meters} m^2")

    def show_availability(self):
        if self._availability:
            print('Dom jest dostępny/możliwy do kupienia')
        else:
            print('Dom jest niedostepny/sprzedany.')

    def show_address(self):
        print(f"Lokalizacja domu: {self._address}")

    def show_basic_info(self):
        pass
