import frappe
from warehouse_management.doctype.item import Item

def create_item(data):
    item_name = data.get('item_name')
    item = Item({
        'item_name': item_name
    })
    item.insert()
    return item
