from fastapi import APIRouter

from schemas.address import AddressRequestModel, AddressResponseModel

router = APIRouter()


@router.post("/address/", response_model=AddressResponseModel, tags=["auth"])
def login(address: AddressRequestModel) -> AddressResponseModel:
    full_address = address

    address_list = full_address.address.split()

    i_position = None
    digit = None

    # Use a for-else loop to avoid needing a separate flag variable
    for index, element in enumerate(address_list):
        if any(char.isdigit() for char in element):
            i_position = index
            digit = element
            break
    else:
        # When no digits are found in address
        print("Invalid address.")
        exit()

    if i_position == 0:
        house_number = digit
        street = " ".join(address_list[1:])

    elif i_position == 1 and len(address_list) > 2:
        street = " ".join(address_list[:2])
        house_number = " ".join(address_list[2:])

    else:
        street = " ".join(address_list[:i_position])
        house_number = " ".join(address_list[i_position:])

    # Use rstrip() to remove trailing commas
    street = street.rstrip(",")
    house_number = house_number.rstrip(",")

    print(f"street: {street}")
    print(f"house_number: {house_number}")

    return AddressResponseModel(
        address={"street": street, "house_number": house_number}
    )
