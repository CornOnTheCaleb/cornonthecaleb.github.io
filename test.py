from pwn import *

conn = remote("cornonthecaleb.github.io", 1337)
conn.send("Hello World!")
conn.close()
