document.getElementById('item-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const itemName = document.getElementById('item-name').value;

    fetch('/api/method/warehouse_management.controllers.item_controller.create_item', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ item_name: itemName }),
    })
    .then(response => response.json())
    .then(data => {
        alert('Item created successfully: ' + data.name);
        document.getElementById('item-form').reset();
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});
