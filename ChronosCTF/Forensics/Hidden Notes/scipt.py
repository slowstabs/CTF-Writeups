def swap_adjacent_bytes(input_file, output_file):
    with open(input_file, "rb") as f:
        data = bytearray(f.read())
    
    for i in range(0, len(data) - 1, 2):
        data[i], data[i + 1] = data[i + 1], data[i]
    
    with open(output_file, "wb") as f:
        f.write(data)

# Example usage
swap_adjacent_bytes("esrcte.wav", "output.wav")
