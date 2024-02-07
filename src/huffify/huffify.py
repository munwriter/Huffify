import heapq
from collections import Counter
from typing import Type

from huffify.abstract import Codec
from huffify.annotations import FinalDataSet
from huffify.heapNodes import LexicographicNode, Node


class HuffmanCodec(Codec):
    def __init__(self, lexicographic_mode: bool = False) -> None:
        if lexicographic_mode:
            self.__HeapNode = LexicographicNode
        else:
            self.__HeapNode = Node

    def _define_char_frequency(self, message: str) -> Counter[str]:
        return Counter(message)

    def print_encoding_table(self, message: dict[str, str]) -> None:
        # TODO add sys.stout
        encoding_table = self._get_encoding_table(message)
        encoding_table = dict(
            sorted(encoding_table.items(), key=lambda x: (len(x[1]), x[1]))
        )
        [print(_) for _ in self._format(encoding_table)]

    def _format(
        self, encoding_table: dict[str, str]
    ) -> list[str] | list[Type]:  # TODO - type hinting for empty list
        if not encoding_table:
            return []
        lines: list[str] = []
        for char, code in encoding_table.items():
            lines.append(f'"{char}" {code}')
        return lines

    def _get_encoding_table(self, message: str) -> dict[str, str]:
        chars_frequency = self._define_char_frequency(message)
        heap = [self.__HeapNode(key, chars_frequency[key]) for key in chars_frequency]
        heapq.heapify(heap)
        encoding_table = {char: "" for char in message}
        while len(heap) > 1:
            low = heapq.heappop(heap)
            hight = heapq.heappop(heap)
            for i in hight.char:
                encoding_table[i] += "0"
            for i in low.char:
                encoding_table[i] += "1"
            hight += low
            heapq.heappush(heap, hight)
        encoding_table = {char: encoding_table[char][::-1] for char in encoding_table}
        return encoding_table

    def _create_bytearray(self, bytes_string: str) -> bytearray:
        additional_bits = len(bytes_string) % 8
        if len(bytes_string) == 8:
            return bytearray((int(bytes_string, 2),))
        elif len(bytes_string) == 0:
            return bytearray()
        else:
            additional_bits = 8 - additional_bits
        bytes_string += additional_bits * "0"
        bytes_message = [
            bytes_string[i : i + 8] for i in range(0, len(bytes_string), 8)
        ]
        bytes_message[-1] = bytes_message[-1][:-additional_bits]
        return bytearray(map(lambda x: int(x, 2), bytes_message))

    def encode_data(self, message: str) -> FinalDataSet:
        encoding_table = self._get_encoding_table(message)
        encoded_message = "".join([encoding_table[char] for char in message])
        encoded_message = self._create_bytearray(encoded_message)
        data_set: FinalDataSet = {"table": encoding_table, "message": encoded_message}
        return data_set

    def decode(self, encoded_data: FinalDataSet) -> str:
        encoding_table, encoded_message = encoded_data.get("table"), encoded_data.get(
            "message"
        )
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
