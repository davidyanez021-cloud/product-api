from fastapi import APIRouter
from app.models import ProductCreate
from app.services.product_service import list_products, register_product, deactivate_product
from app.utils.validators import validate_exists

router = APIRouter(prefix="/products")

@router.get("")
def get_products():
    return list_products()

@router.post("")
def create_product_endpoint(data: ProductCreate):
    return register_product(data)

@router.put("/{product_id}/disable")
def disable(product_id: int):
    product = deactivate_product(product_id)
    return validate_exists(product, "Producto no encontrado") 