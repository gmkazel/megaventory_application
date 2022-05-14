import requests
import config
import os
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.getenv("API_KEY")


class Product:
    ''' A class which represents a Product object
    '''

    def __init__(self,
                 sku: str,
                 description: str,
                 sales_price: float = 0.0,
                 purchase_price: float = 0.0) -> None:
        self.ProductSKU = sku
        self.ProductDescription = description
        self.ProductSellingPrice = sales_price
        self.ProductPurchasePrice = purchase_price

    def post(self, record_action='InsertOrUpdate'):
        data = {
            "APIKEY": APIKEY,
            "mvProduct": {
                "ProductSKU": self.ProductSKU,
                "ProductDescription": self.ProductDescription,
                "ProductSellingPrice": self.ProductSellingPrice,
                "ProductPurchasePrice": self.ProductPurchasePrice
            },
            "mvRecordAction": record_action
        }

        try:
            response = requests.post(url=config.PRODUCT_UPDATE_URL, json=data)
        except ... as err:
            print(err)

        return response.json()
