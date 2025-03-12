**Pari D Pirate**

300

_Pirates hum a tune so free, Drums and fiddles on the sea. Gold for spices, names are lost, Swapping guns, swords, & Indians—at what cost? Ships set sail, the deals are spun, Fortunes shift with the setting sun. Who keeps a score of 500 when all is done?_

Files: pariDpirate.dat

When inspecting the dat file, I saw strings along the lines of `FFIR tmfEVAW`, which in reverse was `RIFF WAVEfmt` which identified as a wav file. 

Since the it was in reverse, I made a script to convert the file into little endian.

```python
def reverse_little_endian(input_file, output_file):
    with open(input_file, "rb") as f:
        data = f.read()

    # Reverse bytes in little-endian chunks of 4
    reversed_data = b"".join([data[i:i+4][::-1] for i in range(0, len(data), 4)])

    with open(output_file, "wb") as f:
        f.write(reversed_data)

    print(f"Reversed file saved as: {output_file}")

reverse_little_endian("pariDpirate.dat", "output.wav")

```

Which gave me `output.wav`. 
