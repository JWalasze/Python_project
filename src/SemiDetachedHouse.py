from src.DetachedHouse import DetachedHouse


class SemiDetachedHouse(DetachedHouse):

    def __init__(self, price, square_meters, address, year_built, floors, semi_detached_house=None):
        super().__init__(price, square_meters, address, year_built, floors)
        if self.__class__ == SemiDetachedHouse and semi_detached_house is not None:
            self._other_half = semi_detached_house
            semi_detached_house._other_half = self

    def show_basic_info(self):
        super().show_price()
        super().show_square_meters()
        super().show_availability()
        super().show_address()
        print(f"Rok budowy: {self._year_built}")
        print(f"Ilość pięter: {self._floors}")
        print('Wybrany dom jest wielorodzinny/bliźniak')
        if self._other_half is not None:
            if self._other_half.is_available():
                print('Druga część bliźniaka jest dostępna\n')
            else:
                print('Druga część bliźniaka jest niedostepna/sprzedana\n')
