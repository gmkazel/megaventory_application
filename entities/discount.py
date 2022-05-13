class Discount:
    ''' A class which represents a Discount object
    '''

    def __init__(self, name: str, description: str, value: float) -> None:
        self.DiscountID = -1
        self.DiscountName = name
        self.DiscountDescription = description
        self.DiscountValue = value