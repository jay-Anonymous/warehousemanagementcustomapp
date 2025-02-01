import frappe
import unittest

class TestItem(unittest.TestCase):
    def test_item_creation(self):
        item = frappe.get_doc({
            "doctype": "Item",
            "item_code": "Test Item",
            "item_name": "Test Item Name",
            "stock_uom": "Nos",
            "is_stock_item": 1
        })
        item.insert()
        self.assertEqual(item.item_code, "Test Item")
        self.assertTrue(frappe.db.exists("Item", item.item_code))
