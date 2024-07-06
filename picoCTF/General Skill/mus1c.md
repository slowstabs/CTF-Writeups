## Mus1c

#### I wrote you a song. Put it in the picoCTF{} flag format. Hint: Do you think you can master rockstar?

What we get is a simple text file with lyrics to a very shitty song. On some slueth its just a normal txt file. So we take a look at the hint and it hints to "Mastering Rockstar"

Searching online we find [rockstar code](https://codewithrockstar.com/online). So we enter the given lyrics into it and we get numbers like so: 

![image](https://github.com/slowstabs/CTF-Writeups/assets/148702248/30a9ac05-f4be-438a-be50-a8a2c09d2c86)

All seem to be around 100 which hints to it being ASCII values, hence we use an [online converter](https://www.browserling.com/tools/ascii-to-text) to convert it to a string. 

`picoCTF{rrrocknrn0113r}`
