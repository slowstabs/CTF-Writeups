## Hidden Notes

Points: 460

Description: Not everything you hear tells the full story. Sometimes, the real message lies beneath the surface, waiting to be discovered. Can you tune in and uncover what’s hidden?

Files: esrcte.awv

We're given a file whose name roughly translates to `secret`, which meant every two letters were flipped. Which meant it was `secret.wav`.

Since this pattern of exchanging positions of every two characters was found in the name of the file, it led me to believe that it has something related to how the bytes are positioned. Therefore, I opened the wav file in HxD to inspect.

![image](https://github.com/user-attachments/assets/91215984-e820-4d13-b2c4-dcd322357148)

On reviewing the given bits, its quite clear that the same flipping of characters has occured here as well. Now all we need is a script that can flip every pair of bytes.

```python

def swap_adjacent_bytes(input_file, output_file):
    with open(input_file, "rb") as f:
        data = bytearray(f.read())
    
    for i in range(0, len(data) - 1, 2):
        data[i], data[i + 1] = data[i + 1], data[i]
    
    with open(output_file, "wb") as f:
        f.write(data)

# Example usage
swap_adjacent_bytes("esrcte.wav", "output.wav")


```

Then I put the new `output.wav` into Sonic Visualiser to view the stereogram for it, and we got the flag. 

![image](https://github.com/user-attachments/assets/ac2a8dd8-b654-489b-a3b4-7fb0aef549ed)


Flag: `saic{h1dd3n_n0735_4r3_10Ud357}`
