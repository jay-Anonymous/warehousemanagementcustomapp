# stock_ledger_entry_controller.py

import frappe
from warehouse_management.doctype.stock_ledger_entry import StockLedgerEntry

def create_stock_ledger_entry(data):
    stock_ledger_entry = StockLedgerEntry(data)
    stock_ledger_entry.insert()
    return stock_ledger_entry
