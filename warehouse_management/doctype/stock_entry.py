# stock_entry.py

import frappe
from frappe.model.document import Document

class StockEntry(Document):
    def validate(self):
        # Logic for validating the stock entry
        if not self.item_code:
            frappe.throw("Item Code is required.")
        if self.quantity < 0:
            frappe.throw("Quantity cannot be negative.")
        if not self.warehouse:
            frappe.throw("Warehouse is required.")
