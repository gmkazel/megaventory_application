import requests
import config
import os
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.getenv("API_KEY")


class Discount:
    ''' A class which represents a Discount object
    '''

    def __init__(self, name: str, value: int, description: str = "") -> None:
        self.DiscountName = name
        self.DiscountDescription = description
        self.DiscountValue = value

    def post(self, record_action='InsertOrUpdate'):
        data = {
            "APIKEY": APIKEY,
            "mvDiscount": {
                "DiscountName": self.DiscountName,
                "DiscountDescription": self.DiscountDescription,
                "DiscountValue": self.DiscountValue
            },
            "mvRecordAction": record_action
        }

        try:
            response = requests.post(url=config.DISCOUNT_UPDATE_URL, json=data)
        except ... as err:
            print(err)

        return response.json()
