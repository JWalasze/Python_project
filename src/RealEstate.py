from src.SingleFamilyHouse import SingleFamilyHouse
from src.SemiDetachedHouse import SemiDetachedHouse
from src.Apartment import Apartment


class RealEstates:

    def __init__(self):
        self._list_of_properties = []
        self._f_list_of_properties = []

    def add_property(self, estate_property):
        self._list_of_properties.append(estate_property)

    def del_property(self, key):
        for x in self._list_of_properties:
            if x.get_id() == key:
                self._list_of_properties.remove(x)

    def prepare_filtered_statistic(self, price_range, square_meters_range, year_built=None,
                                   city=None, property_type=None):
        self.filter_properties(price_range, square_meters_range, year_built, city, property_type)
        for x in self._f_list_of_properties:
            x.show_basic_info()
        self._f_list_of_properties = []

    def filter_properties(self, price_range, square_meters_range, year_built=None, city=None,
                          property_type=None):
        if property_type is not None:
            match property_type:
                case 'dom jednorodzinny':
                    for x in self._list_of_properties:
                        if isinstance(x, SingleFamilyHouse):
                            self._f_list_of_properties.append(x)
                case 'bliźniak':
                    for x in self._list_of_properties:
                        if isinstance(x, SemiDetachedHouse):
                            self._f_list_of_properties.append(x)
                case 'mieszkanie':
                    for x in self._list_of_properties:
                        if isinstance(x, Apartment):
                            self._f_list_of_properties.append(x)

        else:
            for x in self._list_of_properties:
                self._f_list_of_properties.append(x)

        temp_list_of_properties = self._f_list_of_properties.copy()
        for x in temp_list_of_properties:
            if x.price < price_range[0] or x.price > price_range[1]:
                self._f_list_of_properties.remove(x)

            elif x.square_meters < square_meters_range[0] or x.square_meters > square_meters_range[1]:
                self._f_list_of_properties.remove(x)

            elif (year_built is not None) and (x.year_built < year_built[0] or x.year_built > year_built[1]):
                self._f_list_of_properties.remove(x)

            elif (city is not None) and (city not in x.address):
                self._f_list_of_properties.remove(x)

    def show_properties(self):
        print(f"Lista nieruchomości według id: ")
        for x in self._list_of_properties:
            if x.is_available():
                print(f"Id: {x.get_id()}, price: {x.price}$, address: {x.address}")

    def show_filtered_properties(self):
        for x in self._f_list_of_properties:
            print(f"Id filtrowanych nieruchomości: {x.get_id()}")

    def sell_property(self, key_id):
        for x in self._list_of_properties:
            if x.get_id() == key_id:
                x.sell_building()

    def show_info_about_property(self, key_id):
        for x in self._list_of_properties:
            if x.get_id() == key_id:
                x.show_basic_info()

    def return_amount_of_properties(self):
        count = 0
        for x in self._list_of_properties:
            count += 1
        return count
