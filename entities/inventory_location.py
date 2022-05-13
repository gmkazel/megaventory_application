class InventoryLocation:
    ''' A class which represents a InventoryLocation object
    '''

    def __init__(self, abbreviation: str, name: str, address: str) -> None:
        self.InventoryLocationID = -1
        self.InventoryLocationAbbreviation = abbreviation
        self.InventoryLocationName = name
        self.InventoryLocationAddress = address if address else ""