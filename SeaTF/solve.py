# def reverse_little_endian(input_file, output_file):
#     with open(input_file, "rb") as f:
#         data = f.read()

#     # Reverse bytes in little-endian chunks of 4
#     reversed_data = b"".join([data[i:i+4][::-1] for i in range(0, len(data), 4)])

#     with open(output_file, "wb") as f:
#         f.write(reversed_data)

#     print(f"Reversed file saved as: {output_file}")

# # Example usage
# reverse_little_endian("pariDpirate.dat", "output.wav")


import wave

# Open the WAV file normally
filename = "output.wav"

with wave.open(filename) as wav_file:  
    sample_rate = wav_file.getframerate()
    n_frames = wav_file.getnframes()
    sample_width = wav_file.getsampwidth()
    frames = wav_file.readframes(n_frames)

# Convert byte frames to integers
if sample_width == 1:  # 8-bit audio
    data = list(frames)
else:  # 16-bit or more
    data = list(int.from_bytes(frames[i:i+sample_width], byteorder='little', signed=True) 
                for i in range(0, len(frames), sample_width))

# Print the extracted values
print("Extracted Data:", data)


modified_data = [x - 500 for x in data]
print("After Subtracting 500:", modified_data)
