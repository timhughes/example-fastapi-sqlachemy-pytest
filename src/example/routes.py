from fastapi import APIRouter

from .routers import item

router = APIRouter()
router.include_router(item.router, tags=["item"], prefix="/item")
