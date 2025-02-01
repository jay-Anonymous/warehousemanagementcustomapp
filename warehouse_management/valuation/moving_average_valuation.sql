SELECT AVG(stock_value) AS moving_average
FROM stock_ledger_entry
WHERE item_code = %s
AND transaction_date <= %s;
