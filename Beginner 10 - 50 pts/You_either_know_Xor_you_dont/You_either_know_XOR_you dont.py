from pwn import xor
# given message 
message = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"

#first lets convert it to bytes from hex
message_in_bytes = bytes.fromhex(message)

#the question tells us that "Remember the flag format and how it might help you in this challenge!"

start = b"crypto{"

#now since we have both bytes lets xor them to get the message
print(xor(message_in_bytes, start).decode())

# myXORke+y_Q is the output we get, but this si not the flag so we can try input this again
new_start = b"myXORke+y_Q"

print(xor(message_in_bytes, new_start).decode())

# this gives start of flag but the remaining is wrong so we can deduce that myXORke+y_Q is actually just myXORkey

final_start = b"myXORkey"

print(xor(message_in_bytes, final_start).decode())
# we get the final answer