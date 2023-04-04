from fastapi import APIRouter, HTTPException

from api.address.controller import AddressParser
from schemas.address import AddressRequestModel, AddressResponseModel

router = APIRouter()


@router.post("/address/", response_model=AddressResponseModel, tags=["address"])
def extract_address(address: AddressRequestModel) -> AddressResponseModel:
    full_address = address.address

    if len(full_address.split()) < 2:
        raise HTTPException(
            status_code=400, detail="Address should contain at least 2 words"
        )

    if not any(char.isdigit() for char in full_address):
        raise HTTPException(
            status_code=400, detail="Address should contain at least one digit"
        )

    if not any(char.isalpha() for char in full_address):
        raise HTTPException(
            status_code=400, detail="Address should contain some alphabetic characters"
        )

    parser = AddressParser()
    result = parser.parse_address(full_address)

    if not result or not result.get("street") or not result.get("housenumber"):
        raise HTTPException(
            status_code=400,
            detail="Unable to extract street and/or house number from address",
        )

    return AddressResponseModel(
        street=result["street"], housenumber=result["housenumber"]
    )
