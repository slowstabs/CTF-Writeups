def reverse_obfuscation(byte):
    return ((byte & 0b00000011) << 6) | (byte >> 2)

def decrypt_flag(encrypted_hex, key=11):
    encrypted_bytes = bytes.fromhex(encrypted_hex)
    decrypted_bytes = bytearray(len(encrypted_bytes))

    for i, b in enumerate(encrypted_bytes):
        original_byte = reverse_obfuscation(b)  # Reverse obfuscate_output
        decrypted_bytes[i] = original_byte ^ (i % 5 + key)  # Reverse encrypt_flag

    return decrypted_bytes.decode()

# Given encrypted flag
encrypted_flag = "61A5B16925C11DA1F1B5B9F989F5417D95B995A9FDC5"

# Decrypt
flag = decrypt_flag(encrypted_flag)
print("Decrypted Flag:", flag)
