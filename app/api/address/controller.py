class AddressParser:
    def parse_address(self, address: str) -> dict:
        address_list = address.split()

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

        return [street, house_number]
