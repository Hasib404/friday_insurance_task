class AddressParser:
    def parse_address(self, address: str) -> dict:
        address_list = address.split()

        i_position = None
        digit = None

        for index, element in enumerate(address_list):
            if any(char.isdigit() for char in element):
                i_position = index
                digit = element
                break

        if i_position == 0:
            housenumber = digit
            street = " ".join(address_list[1:])

        elif i_position == 1 and len(address_list) > 2:
            street = " ".join(address_list[:2])
            housenumber = " ".join(address_list[2:])

        else:
            street = " ".join(address_list[:i_position])
            housenumber = " ".join(address_list[i_position:])

        # Remove trailing commas
        street = street.rstrip(",")
        housenumber = housenumber.rstrip(",")

        address = {"street": street, "housenumber": housenumber}

        return address
