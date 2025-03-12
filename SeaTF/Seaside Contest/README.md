**Seaside Contest**

300

_It is common for ship captains to communicate to the Light house about their route via Radio frequencies. But NITK Light house has a very unorthodox way of responding back._

Files: crypt.png

Wasn't able to solve this in time but here's the writeup anyways. 

On checking `zsteg`, I got a base64 string which decoded into a brainfuck cipher which finally decoded to the letter s. Thats it, this is where I was stuck.

-x-

Solution to this was extracting data LSB bit order on 0 plane. Which gave us the full base64 string, which I decoded to brainfuck then decode it to get the flag.

![image](https://github.com/user-attachments/assets/475a2a62-ce14-454e-88f7-5b4675b0fe28)

Flag: seaTF{lI8h0us3}
