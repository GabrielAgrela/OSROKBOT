def calculate_offset(base_address, absolute_address):
    return absolute_address - base_address

if __name__ == "__main__":
    base_address = 0x7ff75a3e  # Replace with your base address
    absolute_address1 = 0x24124CF68C0  # Replace with the actual address from run 1
    absolute_address2 = 0x2C179158778  # Replace with the actual address from run 2

    offset1 = calculate_offset(0x2C91C839910, 0x2C91A285E00)
    offset2 = calculate_offset(0x4C75E839910, 0x4C75C285E00)
    offset3 = calculate_offset(0x47276839910, 0x1AC24B1F5C0)

    print(f"Offset for run 1: {hex(offset1)}")
    print(f"Offset for run 2: {hex(offset2)}")
    #print(f"Offset for run 3: {hex(offset3)}")
