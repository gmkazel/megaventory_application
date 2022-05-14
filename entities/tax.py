import requests
import config
import os
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.getenv("API_KEY")


class Tax:
    ''' A class which represents a Tax object
    '''

    def __init__(self, name: str, value: int, description: str = "") -> None:
        self.TaxName = name
        self.TaxDescription = description
        self.TaxValue = value

    def post(self, record_action='InsertOrUpdate'):
        data = {
            "APIKEY": APIKEY,
            "mvTax": {
                "TaxName": self.TaxName,
                "TaxDescription": self.TaxDescription,
                "TaxValue": self.TaxValue
            },
            "mvRecordAction": record_action
        }

        try:
            response = requests.post(url=config.TAX_UPDATE_URL, json=data)
        except ... as err:
            print(err)

        return response.json()
