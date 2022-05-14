from entities.product import Product
from entities.supplier_client import SupplierClient
from entities.inventory_location import InventoryLocation
from entities.tax import Tax
from entities.discount import Discount


def main():

    # Create the desired dummy objects

    product = Product('1112256', 'Nike shoes', 99.99, 44.99)
    client = SupplierClient('Client', 'babis', 'babis@exampletest.com',
                            'Example 8, Athens', '1235698967')
    inventory_location = InventoryLocation('Test', 'Test Project Location',
                                           'Example 20, Athens')
    tax = Tax('VAT', 24, 'VAT GR')
    discount = Discount('Loyalty', 50, 'Loyalty Customer Discount')

    # Insert the above objects to my account

    product_response = product.post()
    client_response = client.post()
    inventory_location_response = inventory_location.post()
    tax_response = tax.post()
    discount_response = discount.post()


if __name__ == "__main__":
    main()