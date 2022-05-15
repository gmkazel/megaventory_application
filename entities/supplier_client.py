import requests
import config
import os
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.getenv("API_KEY")


class SupplierClient:
    ''' A class which represents a SupplierClient object
    '''

    def __init__(self,
                 sc_type: str,
                 name: str,
                 email: str = "",
                 shipping_address: str = "",
                 phone: str = "") -> None:
        self.SupplierClientID = -1
        self.SupplierClientType = sc_type
        self.SupplierClientName = name
        self.SupplierClientEmail = email
        self.SupplierClientShippingAddress = shipping_address
        self.SupplierClientPhone = phone

    def get_name(self) -> str:
        return self.SupplierClientName

    def get_id(self) -> int:
        return self.SupplierClientID

    def set_id(self, record_id) -> None:
        self.SupplierClientID = record_id

    def post(self, record_action='InsertOrUpdate', external_app=""):
        data = {
            "APIKEY": APIKEY,
            "mvSupplierClient": {
                "SupplierClientType":
                    self.SupplierClientType,
                "SupplierClientName":
                    self.SupplierClientName,
                "SupplierClientEmail":
                    self.SupplierClientEmail,
                "SupplierClientShippingAddress1":
                    self.SupplierClientShippingAddress,
                "SupplierClientPhone1":
                    self.SupplierClientPhone
            },
            "mvRecordAction": record_action
        }

        if external_app != "":
            data["mvInsertUpdateDeleteSourceApplication"] = external_app

        try:
            response = requests.post(url=config.SUPPLIER_CLIENT_UPDATE_URL,
                                     json=data)

            entity_id = int(response.json()["entityID"])
            self.set_id(entity_id)

        except ... as err:
            print(err)

        return response.json()
