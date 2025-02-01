# item.py

import frappe
from frappe.model.document import Document

class Item(Document):
    def validate(self):
        # Logic for validating the item
        if not self.item_name:
            frappe.throw("Item Name is required.")
        if self.stock_uom is None:
            frappe.throw("Stock UOM is required.")
