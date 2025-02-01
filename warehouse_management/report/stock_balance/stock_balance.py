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
        {"label": _("Balance Quantity"), "fieldname": "balance_quantity", "fieldtype": "Float", "width": 100},
        {"label": _("As of Date"), "fieldname": "as_of_date", "fieldtype": "Date", "width": 100},
    ]

def get_data(filters):
    conditions = ""
    if filters.get("item_code"):
        conditions += " AND item_code = %(item_code)s"
    
    query = f"""
        SELECT item_code, warehouse, SUM(quantity) AS balance_quantity, %(as_of_date)s AS as_of_date
        FROM `tabStock Ledger Entry`
        WHERE transaction_date <= %(as_of_date)s {conditions}
        GROUP BY item_code, warehouse
    """
    return frappe.db.sql(query, filters, as_dict=True)
