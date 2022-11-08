from magazine.Property import Property


class Flat(Property):
    def __init__(self, area: float, rooms: int,
                 price: float, address: str, floor: int):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f'This is a Flat on {self.address} street that costs' \
               f' {self.price} and is on {self.floor} floor'
