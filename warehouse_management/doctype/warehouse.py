# warehouse.py

import frappe
from frappe.model.document import Document

class Warehouse(Document):
    def validate(self):
        # Logic for validating the warehouse
        if not self.warehouse_name:
            frappe.throw("Warehouse Name is required.")
        if not self.location:
            frappe.throw("Location is required.")
