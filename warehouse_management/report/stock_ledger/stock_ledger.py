import frappe
from frappe import _

def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data

def get_columns():
    return [
        {"label": _("Item Code"), "fieldname": "item_code", "fieldtype": "Data", "width": 150},
        {"label": _("Warehouse"), "fieldname": "warehouse", "fieldtype": "Data", "width": 150},
        {"label": _("Quantity"), "fieldname": "quantity", "fieldtype": "Float", "width": 100},
        {"label": _("Transaction Date"), "fieldname": "transaction_date", "fieldtype": "Date", "width": 100},
    ]

def get_data(filters):
    conditions = ""
    if filters.get("item_code"):
        conditions += " AND item_code = %(item_code)s"
    
    query = f"""
        SELECT item_code, warehouse, quantity, transaction_date
        FROM `tabStock Ledger Entry`
        WHERE 1=1 {conditions}
        ORDER BY transaction_date
    """
    return frappe.db.sql(query, filters, as_dict=True)
