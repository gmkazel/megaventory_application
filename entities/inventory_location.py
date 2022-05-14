import requests
import config
import os
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.getenv("API_KEY")


class InventoryLocation:
    ''' A class which represents a InventoryLocation object
    '''

    def __init__(self, abbreviation: str, name: str, address: str = "") -> None:
        self.InventoryLocationAbbreviation = abbreviation
        self.InventoryLocationName = name
        self.InventoryLocationAddress = address

    def post(self, record_action='InsertOrUpdate'):
        data = {
            "APIKEY": APIKEY,
            "mvInventoryLocation": {
                "InventoryLocationAbbreviation":
                    self.InventoryLocationAbbreviation,
                "InventoryLocationName":
                    self.InventoryLocationName,
                "InventoryLocationAddress":
                    self.InventoryLocationAddress
            },
            "mvRecordAction": record_action
        }

        try:
            response = requests.post(url=config.INVENTORY_LOCATION_UPDATE_URL,
                                     json=data)
        except ... as err:
            print(err)

        return response.json()
