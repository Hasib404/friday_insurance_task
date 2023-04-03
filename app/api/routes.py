from fastapi import APIRouter

from .address import extract_address

router = APIRouter()
router.include_router(extract_address.router)
