from huffify.encoders import MVPEncoder
from huffify.huffify import HuffmanCodec

encoder = MVPEncoder()
codec = HuffmanCodec()
message = "banana"
table = codec._get_encoding_table(message)
print(table)
codec.encode(message)
a = encoder.encode_string(table, message)
print(a)
for _ in a:
    print(bin(_)[2:])
