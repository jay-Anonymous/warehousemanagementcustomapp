import frappe
import unittest

class TestStockEntry(unittest.TestCase):
    def test_stock_entry_creation(self):
        stock_entry = frappe.get_doc({
            "doctype": "Stock Entry",
            "item_code": "Test Item",
            "warehouse": "Test Warehouse",
            "quantity": 5,
            "transaction_type": "Receipt"
        })
        stock_entry.insert()
        self.assertEqual(stock_entry.item_code, "Test Item")
        self.assertTrue(frappe.db.exists("Stock Entry", stock_entry.name))
