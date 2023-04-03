from fastapi import APIRouter

from api.address.controller import AddressParser
from schemas.address import AddressRequestModel, AddressResponseModel

router = APIRouter()


@router.post("/address/", response_model=AddressResponseModel, tags=["address"])
def extract_address(address: AddressRequestModel) -> AddressResponseModel:
    full_address = address.address

    parser = AddressParser()
    result = parser.parse_address(full_address)
    return AddressResponseModel(
        address={"street": result[0], "house_number": result[1]}
    )
