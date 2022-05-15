import requests
import config
import os
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.getenv("API_KEY")


class Discount:
    ''' A class which represents a Discount object
    '''

    def __init__(self, name: str, value: float, description: str = "") -> None:
        self.DiscountID = -1
        self.DiscountName = name
        self.DiscountDescription = description
        self.DiscountValue = value

    def get_id(self) -> int:
        return self.DiscountID

    def set_id(self, record_id) -> None:
        self.DiscountID = record_id

    def post(self, record_action='InsertOrUpdate', external_app=""):
        data = {
            "APIKEY": APIKEY,
            "mvDiscount": {
                "DiscountName": self.DiscountName,
                "DiscountDescription": self.DiscountDescription,
                "DiscountValue": self.DiscountValue
            },
            "mvRecordAction": record_action
        }

        if external_app != "":
            data["mvInsertUpdateDeleteSourceApplication"] = external_app

        try:
            response = requests.post(url=config.DISCOUNT_UPDATE_URL, json=data)

            entity_id = int(response.json()["entityID"])
            self.set_id(entity_id)

        except ... as err:
            print(err)

        return response.json()
