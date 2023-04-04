from typing import Optional
from pydantic import BaseModel


# Define Request Model
class AddressRequestModel(BaseModel):
    address: str


# Define Response Model
class AddressResponseModel(BaseModel):
    street: str
    housenumber: Optional[str] = None
