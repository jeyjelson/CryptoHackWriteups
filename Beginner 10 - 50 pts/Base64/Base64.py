import base64
# decode to bytes first
bytes_of_string = bytes. fromhex("72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
)
# print decoded bytes to base64
print(base64.b64encode(bytes_of_string))