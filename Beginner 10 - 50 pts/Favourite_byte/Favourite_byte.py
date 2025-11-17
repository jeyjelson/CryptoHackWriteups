from pwn import xor

#given data in hex convert this to bytes
data = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

#use brute force to test all keys from 0 - 255
for key in range(0,256):
    new_data = xor(data, key)
    print(new_data.decode()) # print every decoded result

#find correct output in terminal

