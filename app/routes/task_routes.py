from fastapi import APIRouter, HTTPException
from app.models import ProductCreate
from app.services.product_service import list_products, register_product, deactivate_product

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
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return product