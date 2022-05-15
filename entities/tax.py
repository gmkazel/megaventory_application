import requests
import config
import os
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.getenv("API_KEY")


class Tax:
    ''' A class which represents a Tax object
    '''

    def __init__(self, name: str, value: float, description: str = "") -> None:
        self.TaxID = -1
        self.TaxName = name
        self.TaxDescription = description
        self.TaxValue = value

    def get_id(self) -> int:
        return self.TaxID

    def set_id(self, record_id) -> None:
        self.TaxID = record_id

    def post(self, record_action='InsertOrUpdate', external_app=""):
        data = {
            "APIKEY": APIKEY,
            "mvTax": {
                "TaxName": self.TaxName,
                "TaxDescription": self.TaxDescription,
                "TaxValue": self.TaxValue
            },
            "mvRecordAction": record_action
        }

        if external_app != "":
            data["mvInsertUpdateDeleteSourceApplication"] = external_app

        try:
            response = requests.post(url=config.TAX_UPDATE_URL, json=data)

            entity_id = int(response.json()["entityID"])
            self.set_id(entity_id)

        except ... as err:
            print(err)

        return response.json()
