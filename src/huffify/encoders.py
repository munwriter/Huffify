from huffify.abstract import IEncoder


class MVPEncoder(IEncoder):
    def _build_bytes_string_from_table(
        self, encoding_table: dict[str, str], message: str
    ) -> str:
        bytes_string = "".join([encoding_table[char] for char in message])
        return bytes_string

    def _make_bytes_partition(self, bytes_string: str) -> bytearray:
        if not bytes_string:
            return bytearray()
        elif len(bytes_string) <= 8:
            byte = (int(bytes_string, 2),)
            return bytearray(byte)
        additional_len = len(bytes_string) % 8
        required_len = len(bytes_string) - additional_len
        encoded_stream = []
        for i in range(0, required_len, 8):
            encoded_stream.append(bytes_string[i : i + 8])
        if additional_len:
            encoded_stream.append(bytes_string[-additional_len:])
        print(encoded_stream)
        return bytearray(map(lambda x: int(x, 2), encoded_stream))

    def encode_string(self, encoding_table: dict[str, str], message: str) -> bytearray:
        bytes_string = self._build_bytes_string_from_table(encoding_table, message)
        encoded_message = self._make_bytes_partition(bytes_string)
        return encoded_message

    def decode_string(self, encoding_table: dict[str, str], encoded_message: bytearray) -> str:
        encoding_table = {code: char for char, code in encoding_table.items()}
        bytes_container: list[str] = []
        for byte in encoded_message:
            bytes_container.append(bin(byte)[2:])
        bytes_string = "".join(bytes_container)
        current_code = ""
        decoded_message = ""
        for num in bytes_string:
            current_code += num
            if encoding_table.get(current_code):
                decoded_message += encoding_table[current_code]
                current_code = ""

        return decoded_message
