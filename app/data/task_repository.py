from app.models import Product, ProductCreate

products: list[Product] = []
next_id = 1

def get_all_products():
    return products

def create_product(product_data: ProductCreate):
    global next_id
    product = Product(
        id=next_id,
        name=product_data.name,
        description=product_data.description,
        price=product_data.price,
        stock=product_data.stock
    )
    products.append(product)
    next_id += 1
    return product

def disable_product(product_id: int):
    for p in products:
        if p.id == product_id:
            p.available = False
            return p
    return None