# import zlib
import pickle

from huffify import HuffmanCodec

encoder = HuffmanCodec()
message = "qwertyuiopasdfghjklzxcvbnm" * 50
message = (
    19
    * """Python Encapsulation

Encapsulation is one of the fundamental concepts in object-oriented programming (OOP). It describes the idea of wrapping data and the methods that work on data within one unit. This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data. To prevent accidental change, an object`s variable can only be changed by an object’s method. Those types of variables are known as private variables.

A class is an example of encapsulation as it encapsulates all the data that is member functions, variables, etc."""
)
message = "aboba"
output = encoder.encode_data(message)
print(output)
print(encoder.decode(output))
encoder.print_encoding_table(message)

# # print(encoder.encode_data(message), encoder.get_encoding_table(message))
# import io

# with open("output00.txt", "tw", encoding="utf-8") as f:
#     f.write(message)
# # with open("output0.txt", "tw", encoding="utf-8") as f:
# #     f.write((encoder.encode_data(message)))
# with open("output1.txt", "bw") as f:
#     pickle.dump(data, f)
# # with open("output2.txt", "bw") as f:
# #     f.write(zlib.compress((encoder.encode_data(message).encode())))
# # with open("output3.txt", "bw") as f:
# #     f.write(zlib.compress(message.encode()))


# print(output)
# # def foo(a: int, b: list) -> list:
# #     a = 2
# #     b[0] = 2
# #     b = [3, 2, 1]
# #     return b

# # a = 5
# # b = [1, 2, 3]

# # print(foo(a, b))
# # print(a)
# # print(b)
