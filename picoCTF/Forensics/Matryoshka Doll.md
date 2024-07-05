## Matryoshka doll

#### Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. What's the final one? 

Very simple challenge of decompressing an image to find another image to find another image

What I did was I checked the metadata and it gave an over whelming amount of info so it was only logical to run a `binwalk` to see what was inside.

![image](https://github.com/slowstabs/CTF-Writeups/assets/148702248/c26fec47-c804-4997-86a3-299407c350ba)

We see an image in `base_images/2_c.png` so we extract and binwalk over and over 3 times to finally get our flag.txt file

![image](https://github.com/slowstabs/CTF-Writeups/assets/148702248/504e8a80-ba9f-4fdb-9532-25c29607441f)


Flag: 

![image](https://github.com/slowstabs/CTF-Writeups/assets/148702248/8efca91f-e7d3-46d8-aa1c-d3f0dedc36eb)

Tip: Use [This](https://miniwebtool.com/remove-spaces/) to remove the spaces.

`picoCTF{e3f378fe6c1ea7f6bc5ac2c3d6801c1f}`


