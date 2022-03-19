from src.SingleFamilyHouse import SingleFamilyHouse
from src.SemiDetachedHouse import SemiDetachedHouse
from src.Apartment import Apartment
from src.RealEstate import RealEstates
from src.Client import Client


def main():

    house = SingleFamilyHouse(400000, 150, 'ul. Miodowa 1, Sobótka', 2020, 2)
    house2 = SingleFamilyHouse(550000, 175, 'ul. Malinowa 4/6, Wrocław', 2018, 3)
    house3 = SingleFamilyHouse(330000, 120, 'Plac Niepodległości 22, Wrocław', 2014, 2)
    house4 = SemiDetachedHouse(200000, 95, 'ul. Kazimierza Wielkiego 2, Wrocław', 2022, 3)
    house5 = SemiDetachedHouse(220000, 105, 'ul. Kazimierza Wielkiego 2, Wrocław', 2022, 3, semi_detached_house=house4)
    house6 = Apartment(480000, 75, 'ul. Świętego Pawła, Starachowice', 2017, 9)
    houses = [house, house2, house3, house4, house5, house6]

    estate = RealEstates()
    for x in houses:
        estate.add_property(x)

    client = Client(estate)
    client.menu()


if __name__ == '__main__':
    main()
