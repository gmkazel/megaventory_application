import itertools
import requests
import config
import os
from dotenv import load_dotenv
from . import inventory_location
from . import supplier_client
from . import tax
from . import discount

load_dotenv()

APIKEY = os.getenv("API_KEY")


class SalesOrder:
    ''' A class which represents a SalesOrder object
    '''

    id_iterator = itertools.count()

    def __init__(self, status: str, client: supplier_client.SupplierClient,
                 order_items_list: list,
                 location: inventory_location.InventoryLocation, tax: tax.Tax,
                 discount: discount.Discount) -> None:
        self.SalesOrderId = next(SalesOrder.id_iterator)
        self.SalesOrderNo = -1
        self.sales_order_status = status
        self.client = client
        self.order_items_list = order_items_list
        self.location = location
        self.tax = tax
        self.discount = discount

    def get_id(self) -> int:
        return self.SalesOrderId

    def set_id(self, record_id) -> None:
        self.SalesOrderId = record_id

    def value_without_tax_and_discount(self) -> float:
        ''' Calculate the value of the items of the desired order without the tax and the discount
        '''
        value = 0.0

        for product, quantity in self.order_items_list:
            value += product.ProductSellingPrice * quantity

        return value

    def total_order_value(self, tax: tax.Tax,
                          discount: discount.Discount) -> float:
        ''' Calculate the total value of the items of the desired order
        '''

        total_value = self.value_without_tax_and_discount()

        # if tax is given, apply it to the total value
        if tax is not None:
            total_value += (tax.TaxValue * 0.01) * total_value

        # if discount is given, apply it to the total value (with tax or with not, if tax was not given)
        if discount is not None:
            total_value -= (discount.DiscountValue * 0.01) * total_value

        return total_value

    def post(self, record_action='InsertOrUpdate', external_app=""):
        sales_order_details_list = []

        for product, quantity in self.order_items_list:
            sales_order_details = {}
            sales_order_details["SalesOrderRowProductSKU"] = product.ProductSKU
            sales_order_details["SalesOrderRowQuantity"] = quantity
            sales_order_details[
                "SalesOrderRowShippedQuantity"] = 0  # my assumption
            sales_order_details[
                "SalesOrderRowInvoicedQuantity"] = 0  # my assumption
            sales_order_details[
                "SalesOrderRowUnitPriceWithoutTaxOrDiscount"] = product.ProductSellingPrice
            sales_order_details[
                "SalesOrderTotalTaxAmount"] = product.ProductSellingPrice * (
                    self.tax.TaxValue * 0.01)
            sales_order_details[
                "SalesOrderRowTotalDiscountAmount"] = product.ProductSellingPrice * (
                    self.discount.DiscountValue * 0.01)
            sales_order_details["SalesOrderRowTotalAmount"] = (
                product.ProductSellingPrice + product.ProductSellingPrice *
                (self.tax.TaxValue * 0.01)) * (self.discount.DiscountValue *
                                               0.01)

            sales_order_details_list.append(sales_order_details)

        total_quantity = sum(x[1] for x in self.order_items_list)

        value_without_tax_and_discount = self.value_without_tax_and_discount()

        sales_order_amount_total_discount = value_without_tax_and_discount * (
            self.discount.DiscountValue * 0.01)
        sales_order_amount_total_tax = value_without_tax_and_discount * (
            self.tax.TaxValue * 0.01)

        sales_order_amount_grand_total = self.total_order_value(
            self.tax, self.discount)

        data = {
            "APIKEY": APIKEY,
            "mvSalesOrder": {
                "SalesOrderStatus":
                    self.sales_order_status,
                "SalesOrderId":
                    self.SalesOrderId,
                "SalesOrderClientId":
                    self.client.get_id(),
                "SalesOrderClientName":
                    self.client.get_name(),
                "SalesOrderInventoryLocationID":
                    self.location.get_id(),
                "SalesOrderTotalQuantity":
                    total_quantity,
                "SalesOrderAmountSubtotalWithoutTaxAndDiscount":
                    value_without_tax_and_discount,
                "SalesOrderAmountTotalDiscount":
                    sales_order_amount_total_discount,
                "SalesOrderAmountTotalTax":
                    sales_order_amount_total_tax,
                "SalesOrderAmountGrandTotal":
                    sales_order_amount_grand_total,
                "SalesOrderDetails":
                    sales_order_details_list
            },
            "mvRecordAction": record_action
        }

        if external_app != "":
            data["mvInsertUpdateDeleteSourceApplication"] = external_app

        try:
            response = requests.post(url=config.SALES_ORDER_UPDATE_URL,
                                     json=data)

            entity_id = int(response.json()["entityID"])
            self.set_id(entity_id)

            self.SalesOrderNo = int(
                response.json()["mvSalesOrder"]["SalesOrderNo"])

        except ... as err:
            print(err)

        return response.json()