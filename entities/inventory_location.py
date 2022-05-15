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
        self.InventoryLocationID = -1
        self.InventoryLocationAbbreviation = abbreviation
        self.InventoryLocationName = name
        self.InventoryLocationAddress = address

    def get_id(self) -> int:
        return self.InventoryLocationID

    def set_id(self, record_id) -> None:
        self.InventoryLocationID = record_id

    def post(self, record_action='InsertOrUpdate', external_app=""):
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

        if external_app != "":
            data["mvInsertUpdateDeleteSourceApplication"] = external_app

        try:
            response = requests.post(url=config.INVENTORY_LOCATION_UPDATE_URL,
                                     json=data)

            entity_id = int(response.json()["entityID"])
            self.set_id(entity_id)

        except ... as err:
            print(err)

        return response.json()
