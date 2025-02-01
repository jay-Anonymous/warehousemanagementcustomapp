import frappe
from frappe.model.document import Document

class StockLedgerEntry(Document):
    def validate(self):
        # Add validation logic here
        pass
