import frappe
from warehouse_management.doctype.warehouse import Warehouse

def create_warehouse(data):
    warehouse_name = data.get('warehouse_name')
    warehouse = Warehouse({
        'warehouse_name': warehouse_name
    })
    warehouse.insert()
    return warehouse
