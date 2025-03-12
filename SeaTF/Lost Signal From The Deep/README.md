**Lost Signal from the Deep**

100 Pts

_A mysterious distress signal has been intercepted from a lost submarine built by the mechanical engineers at NITK. Can you recover the message?_
_The Electrical Engineers who were eavesdropping on random signals (as usual) were able to find some vague clues regarding the missing signal:_

_Files: submarine, q1.jpg_

This, much like a lot of other questions had finding a passphrase and inputing into steghide. 

I decompiled the program and found the `reconstruct_password` function which makes the password using 5 pieces of info. GPT did the work of reversing the password which had some XORing to do

```
The reconstruct_password function is XOR-decrypting different parts of the password using specific XOR keys.:

part1: XORs each byte with 0x3A (8 bytes)
part2: XORs each byte with 0x5F (4 bytes)
part3: XORs each byte with 0x3A (6 bytes)
part4: XORs the first two bytes with 0x5F5F
byte_4012: XORs a single byte with 0x5F
```

Python Script for finding the passphrase

```python
part1_encrypted = [ord('v'), 0x0A, 0x0F, ord('n'), ord('e'), 0x0E, ord('n'), ord('e')]
part2_encrypted = [0x1B, ord('l'), ord('l'), 0x0F]
part3_encrypted = [0x0F, 0x09, 0x0E, ord('e'), ord('i'), 0x09]
part4_encrypted = 0x0B1E
byte_4012_encrypted = 0x19

# XOR keys
xor_key_3A = 0x3A
xor_key_5F = 0x5F
xor_key_5F5F = 0x5F5F

# Decrypting parts
part1_decrypted = ''.join(chr(b ^ xor_key_3A) for b in part1_encrypted)
part2_decrypted = ''.join(chr(b ^ xor_key_5F) for b in part2_encrypted)
part3_decrypted = ''.join(chr(b ^ xor_key_3A) for b in part3_encrypted)
part4_decrypted = ''.join(chr((part4_encrypted ^ xor_key_5F5F) >> (8 * i) & 0xFF) for i in range(2))
byte_4012_decrypted = chr(byte_4012_encrypted ^ xor_key_5F)

# Concatenating the final password
final_password = part1_decrypted + part2_decrypted + part3_decrypted + part4_decrypted + byte_4012_decrypted

```

This gives us the passphrase `L05T_4T_D33P534_S3ATF`

Used this on `q1.jpg` using steghide.
`steghide extract -sf q1.jpg -p L05T_4T_D33P534_S3ATF`, which gave me the flag

Flag: SEATF{L05T_SU3M4RIN3_SIGN4L_4T_SUR4THK4L}






