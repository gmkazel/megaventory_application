class Tax:
    ''' A class which represents a Tax object
    '''
    
    def __init__(self, name: str, description: str, value: float) -> None:
        self.TaxID = -1
        self.TaxName = name
        self.TaxDescription = description
        self.TaxValue = value