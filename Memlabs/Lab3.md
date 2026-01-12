## Lab 3 - Memlabs

> Challenge Description: 
> 
> A malicious script encrypted a very secret piece of information I had on my system. Can you recover the information for me please?
> Note-1: This challenge is composed of only 1 flag. The flag split into 2 parts.
> Note-2: You'll need the first half of the flag to get the second.
> 
> You will need this additional tool to solve the challenge,
>
> $ sudo apt install steghide

### Part 1

Firstly I ran `imageinfo` and `pslist` on the given memory file using volitility to list out the processes that were carried out:

Commands: 
`vol2 -f MemoryDump_Lab3.raw imageinfo`
`vol2 -f MemoryDump_Lab3.raw --profile=Win7SP0x86 pslist`

<img width="1273" height="250" alt="image" src="https://github.com/user-attachments/assets/6eb1acfb-8bb3-4257-875a-7b6cebfecdff" />

Mainly 3 processes mainly caught my eye in pslist , `TrustedInstall`, `audiodg.exe` and `notepad.exe`. Since I checked out notepad related stuff in the previous challenges I ran `cmdline` to see what arguments were given to notepad.

<img width="1902" height="675" alt="image" src="https://github.com/user-attachments/assets/0d41e820-bed4-4663-a779-d13938011839" />

PS: I googled up on trustedinstall and audiodg as their location was /Windows and /System32 so they are mostly system files. 

I saw that `vip.txt` and `evilscript.py` were opened in notepad. I proceeded to extract the two files into my system using the `filescan` to get the address and `dumpfiles` command to extract the files. Exact commands are given below:

`vol2 -f MemoryDump_Lab3.raw --profile=Win7SP0x86 filescan | grep -i vip` 
`vol2 -f MemoryDump_Lab3.raw --profile=Win7SP0x86 filescan | grep -i evilscript.py` 
(executing took a while for some reason)

<img width="1657" height="304" alt="image" src="https://github.com/user-attachments/assets/f35f451e-10ea-4182-b449-b2301d6d0c67" />

vip.txt gave me a base64 string which looked like gibberish on decoding and evilscript.py gave me the script which was used to get the string. It was a xor + b64 encryption therefore I decrypted it and found the first part of the flag

<img width="1464" height="93" alt="image" src="https://github.com/user-attachments/assets/25f3362a-8d22-4a22-8ee6-1a600aa3164f" />
<img width="1344" height="206" alt="image" src="https://github.com/user-attachments/assets/b5a0642a-93c7-4a5e-bb3b-1e9a3cb3cb17" />

Flag part 1: `inctf{0n3_h4lf`

### Part 2

In the beginning, we were told that we'll need `steghide` indicating steganography in an image. So I looked for any such image files that would be of use, using filescan. A little googling told me that steghide mainly takes jpg/jpeg/bmp files so I used that as my grep query. 

<img width="1919" height="383" alt="image" src="https://github.com/user-attachments/assets/63d2edd8-3317-42ac-a9b0-4ade45ce624c" />

I found a file called `suspicion1.jpeg` in the many entries and extracted it using `dumpfiles`. Then I used steghide to extract hidden data. 

```steghide --extract -sf suspicion1.jpeg```

for the passphrase, I remembered that the challenge said, we need part 1 for part 2, possibly indicating the part 1 flag was the passphrase for it and it was.

<img width="1591" height="313" alt="image" src="https://github.com/user-attachments/assets/a4d12b38-48cb-40b8-80a0-17ec530e067c" />

Flag part 2: `_1s_n0t_3n0ugh}`

--- 

Final Flag: `inctf{0n3_h4lf_1s_n0t_3n0ugh}`

---

### Personal gains:

1. Solved it completely by myself
2. Learned a cool grep trick (the grep -iE 'xy|pq|ab' thing)
3. Started using terminal/py for b64 and xor conversions instead of running to cyberchef :> 











