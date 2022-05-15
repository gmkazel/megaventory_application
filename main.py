from entities.product import Product
from entities.supplier_client import SupplierClient
from entities.inventory_location import InventoryLocation
from entities.tax import Tax
from entities.discount import Discount
from entities.sales_order import SalesOrder


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
    #print(product_response)

    client_response = client.post()
    #print(client_response)

    inventory_location_response = inventory_location.post()
    #print(inventory_location_response)

    tax_response = tax.post()
    #print(tax_response)

    discount_response = discount.post()
    #print(discount_response)

    # Create a sales order using the entities inserted, and insert it to my account

    order_items_list = [(product, 1)]
    sales_order = SalesOrder('Verified', client, order_items_list,
                             inventory_location, tax, discount)

    sales_order_response = sales_order.post()
    #print(sales_order_response)

    print(
        "The Total Value of the Sales Order after applying the Tax and Discount is:",
        "{:.2f}".format(sales_order.total_order_value(tax, discount)))


if __name__ == "__main__":
    main()