## giffy-5

Points: 379

> Description: This GIF isn't just for show—there's a hidden message scattered across its frames. Can you analyze the pieces, reconstruct the patterns, and uncover what’s concealed within?

Its a classic GIF QR code chall. Just need to split the frames of the gif for which I used ezgif. The first QR code gave us a flag which was encoded with vigenere cipher. The third QR code gave us the key for vigenere cipher. 

Key = vignere_it_is

On decoding it, we get our flag.

Flag: `saic{g1ffy_fr4m3s_4r3_W4tch1ng_u}`
