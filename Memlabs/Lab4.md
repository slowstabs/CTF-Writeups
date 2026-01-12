## Lab 4 - Memlabs

> Challenge Description:
> My system was recently compromised. The Hacker stole a lot of information but he also deleted a very important file of mine. I have no idea on how to recover it. The only evidence we have, at this point of time is this memory dump. Please help me.
>
> Note: This challenge is composed of only 1 flag.

I started with running `pslist` as usual and really observed only one process of interest which was `StikyNot.exe`.

<img width="1403" height="398" alt="image" src="https://github.com/user-attachments/assets/2b614fb6-9290-4d24-9df0-280ef279978c" />

So therefore, I ran `filescan` to find the address, to then extract. (nvm brainfart dunno what it is yet, got the address tho, maybe useful -> `0x000000003fd095b0` )

Got stuck for a while so I tried using `clipboard` and found nothing again. So I looked at another writeup... and it told me to brute force so I used `filescan` to brute every single common file extention possible. So I used the following cmd and listed the files:

`vol2 -f MemoryDump_Lab4.raw --profile=Win7SP0x64 filescan | grep -i '\\Users\\' | grep -i "jpg\|jpeg\|png\|bmp\|txt\|exe\|py" `
 
<img width="1450" height="370" alt="image" src="https://github.com/user-attachments/assets/a5befe71-58e4-4d95-9097-df1288a4b023" />

Through this I found 3 mail files which stood out, `galf.jpeg`, `Screenshot1.png` and `Important.txt`. So I copied the addresses and then dumped the files to inspect using:

`vol2 -f MemoryDump_Lab4.raw --profile=Win7SP0x64 dumpfiles -Q 0x000000003e8ad250,0x000000003e8d19e0,0x000000003fc398d0 -D .`

One of the files didn't show up in the dump and it was `Important.txt`. On referring to the writeup again, I found out that this happens when a file is deleted. The way to retrieve it is to access the MFT data. Volatility has a plugin to get this data called `mftparser`. It does give a lot of data therefore it is adviced to store the output in a file.

On grep'ing through the output file, we can find the contents of Information.txt in a hex view which contained the flag. 

<img width="1473" height="679" alt="image" src="https://github.com/user-attachments/assets/0965bebe-8188-4fb0-94b1-6b78683f1f14" />

Final Flag: `inctf{1_is_n0t_EQu4l_7o_2_bUt_th1s_d0s3nt_m4ke_s3ns3}`




