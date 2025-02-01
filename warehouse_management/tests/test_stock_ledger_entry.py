import frappe
import unittest

class TestStockLedgerEntry(unittest.TestCase):
    def test_stock_ledger_entry_creation(self):
        stock_entry = frappe.get_doc({
            "doctype": "Stock Ledger Entry",
            "item_code": "Test Item",
            "warehouse": "Test Warehouse",
            "quantity": 10,
            "transaction_date": "2023-01-01"
        })
        stock_entry.insert()
        self.assertEqual(stock_entry.item_code, "Test Item")
        self.assertTrue(frappe.db.exists("Stock Ledger Entry", stock_entry.name))
