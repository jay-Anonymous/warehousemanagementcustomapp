document.getElementById('stock-entry-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const stockEntryName = document.getElementById('stock-entry-name').value;

    fetch('/api/method/warehouse_management.controllers.stock_entry_controller.create_stock_entry', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ stock_entry_name: stockEntryName }),
    })
    .then(response => response.json())
    .then(data => {
        alert('Stock Entry created successfully: ' + data.name);
        document.getElementById('stock-entry-form').reset();
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});
