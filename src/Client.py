

def show_menu():
    print('a -> Sprawdź dostępne nieruchomości')
    print('b -> Filtruj nieruchomości')
    print('c -> Kup wybraną nieruchomość')
    print('d -> Zakończ korzystanie')


class Client:
    def __init__(self, properties):
        self._properties = properties

    def show_available_property(self):
        self._properties.show_properties()

    def filter_available_properties(self, price_range, square_meters_range, year_built=None,
                                    city=None, property_type=None):
        self._properties.prepare_filtered_statistic(price_range, square_meters_range, year_built, city, property_type)

    def buy_property(self, key_id):
        print(f"Udało ci się kupić nieruchomość o id: {key_id}")
        print(f"Szczegółowy opis mieszkania: ")
        self._properties.show_info_about_property(key_id)
        self._properties.sell_property(key_id)

    def menu(self):
        print('\n')
        show_menu()
        var = input('Wybierz opcję z podanych -> ')
        print('\n')
        while var != 'd':
            match var:
                case 'a':
                    self.show_available_property()
                case 'b':
                    price_down = int(input("Wprowadź dolną granicę ceny: "))
                    price_up = int(input("Wprowadź górną granicę ceny: "))
                    m_down = int(input("Wprowadź dolną granicę wymiarów nieruchomości w m^2: "))
                    m_up = int(input("Wprowadź górną granicę wymiarów nieruchomości w m^2: "))
                    print("Podaj zakres lat powstania nieruchomośc")
                    d = int(input("Podaj dolny zakres: "))
                    d1 = int(input("Podaj górny zakres: "))
                    city = input("Podaj nazwę miasta: ")
                    d2 = input("Podaj ty nieruchomości (dom jednorodzinny, bliźniak, mieszkanie): ")
                    print('Oto wyniki wyszukiwań:')
                    self.filter_available_properties([price_down, price_up], [m_down, m_up], [d, d1], city, d2)
                case 'c':
                    var = int(input("Podaj id wybranego mieszkania: "))
                    self.buy_property(var)
                case 'd':
                    print('Koniec działania programu...')

            print('\n')
            show_menu()
            var = input('Wybierz opcję z podanych: ')
            print('\n')
