import frappe
from warehouse_management.doctype.stock_entry import StockEntry

def create_stock_entry(data):
    stock_entry_name = data.get('stock_entry_name')
    stock_entry = StockEntry({
        'stock_entry_name': stock_entry_name
    })
    stock_entry.insert()
    return stock_entry
