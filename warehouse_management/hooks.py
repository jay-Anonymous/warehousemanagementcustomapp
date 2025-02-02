app_name = "warehouse_management"
app_title = "Warehouse Management"
app_publisher = "gathee"
app_description = "gathee"
app_email = "gathee@gmail.com"
app_license = "gpl-3.0"

# Apps
# ------------------
required_apps = []

# Each item in the list will be shown as an app in the apps page
add_to_apps_screen = [
    {
        "name": "warehouse_management",
        "logo": "/assets/warehouse_management/logo.png",
        "title": "Warehouse Management",
        "route": "/warehouse_management",
        "has_permission": "warehouse_management.api.permission.has_app_permission"
    }
]

# Includes in <head>
# ------------------
# include js, css files in header of desk.html
app_include_css = "/assets/warehouse_management/css/warehouse_management.css"
app_include_js = "/assets/warehouse_management/js/warehouse_management.js"
