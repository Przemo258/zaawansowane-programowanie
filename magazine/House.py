from magazine.Property import Property


class House(Property):
    def __init__(self, area: float, rooms: int,
                 price: float, address: str, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f'This is a House on {self.address} street that' \
               f' costs {self.price} with an plot {self.plot}'
