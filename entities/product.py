class Product:
    ''' A class which represents a Product object
    '''

    def __init__(self, sku: str, description: str, sales_price: float,
                 purchase_price: float) -> None:
        self.ProductID = -1
        self.ProductSKU = sku
        self.ProductDescription = description
        self.ProductSalesPrice = sales_price if sales_price else 0.0
        self.ProductPurchasePrice = purchase_price if purchase_price else 0.0