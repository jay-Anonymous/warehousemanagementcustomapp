document.getElementById('warehouse-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const warehouseName = document.getElementById('warehouse-name').value;

    fetch('/api/method/warehouse_management.controllers.warehouse_controller.create_warehouse', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ warehouse_name: warehouseName }),
    })
    .then(response => response.json())
    .then(data => {
        alert('Warehouse created successfully: ' + data.name);
        document.getElementById('warehouse-form').reset();
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});
