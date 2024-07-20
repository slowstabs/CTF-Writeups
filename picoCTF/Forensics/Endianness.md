## Endianness

This was a fairly simple challenge which required us to find the small endian and big endian value of a certain randomly constructed word.

The word we get is 5 letters `okewb` in my case. So we convert each letter to Hex on [ASCII to Hex](https://www.rapidtables.com/convert/number/ascii-to-hex.html)

Then we get something like `6F 6B 65 77 62`, this is your big endian representation
Flip that around and you get `62 77 65 6B 6F`, which is your little endian representation

Enter these into the netcat link without spaces and you'll get your flag :D

`picoCTF{3ndi4n_sw4p_su33ess_28329f0a}`
