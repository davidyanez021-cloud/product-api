from app.data.product_repository import get_all_products, create_product, disable_product

def list_products():
    return get_all_products()

def register_product(data):
    return create_product(data)

def deactivate_product(product_id):
    return disable_product(product_id)