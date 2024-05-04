from Address import Address

class Mailing:
     def __init__(self, addressone: Address, addresstwo: Address, cost: int, track: str):
             self.addressone = addressone
             self.addresstwo = addresstwo
             self.cost = cost
             self.track = track