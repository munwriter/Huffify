a = "110011101"


# print(a[:-9])
def _create_bytearray(bytes_string: str) -> bytearray:
    additional_bits = len(bytes_string) % 8
    if len(bytes_string) == 8:
        return bytearray((int(bytes_string, 2),))
    elif len(bytes_string) == 0:
        return bytearray()
    else:
        additional_bits = 8 - additional_bits
    bytes_string += additional_bits * "0"
    bytes_message = [bytes_string[i : i + 8] for i in range(0, len(bytes_string), 8)]
    bytes_message[-1] = bytes_message[-1][:-additional_bits]
    return bytearray(map(lambda x: int(x, 2), bytes_message))


print(next(iter(_create_bytearray("101101111"))))
