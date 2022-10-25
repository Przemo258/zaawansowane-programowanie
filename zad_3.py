class Property:
    def __init__(self, area: float, rooms: int, price: float, address: str):
        self.address = address
        self.price = price
        self.rooms = rooms
        self.area = area


class House(Property):
    def __init__(self, area: float, rooms: int,
                 price: float, address: str, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f'This is a House on {self.address} street that' \
               ' costs {self.price} with an plot {self.plot}'


class Flat(Property):
    def __init__(self, area: float, rooms: int,
                 price: float, address: str, floor: int):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f'This is a Flat on {self.address} street that costs' \
               ' {self.price} and is on {self.floor} floor'


house = House(51, 3, 50000, 'Katowicka 3', 2000)
flat = Flat(40, 2, 80000, 'Gliwicka 15', 1)

print(house)
print(flat)
