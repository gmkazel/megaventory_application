class SupplierClient:
    ''' A class which represents a SupplierClient object
    '''

    def __init__(self, type: str, name: str, email: str, shipping_address: str,
                 phone: str) -> None:
        self.SupplierClientID = -1
        self.SupplierClientType = type
        self.SupplierClientName = name
        self.SupplierClientEmail = email if email else ""
        self.SupplierClientShippingAddress = shipping_address if shipping_address else ""
        self.SupplierClientPhone = phone if phone else ""