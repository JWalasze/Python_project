from src.DetachedHouse import DetachedHouse


class SingleFamilyHouse(DetachedHouse):

    def __init__(self, price, square_meters, address, year_built, floors):
        super().__init__(price, square_meters, address, year_built, floors)

    def show_basic_info(self):
        super().show_price()
        super().show_square_meters()
        super().show_availability()
        super().show_address()
        print(f"Rok budowy: {self._year_built}")
        print(f"Ilość pięter: {self._floors}")
        print('Wybrany dom jest jednorodzinny\n')
