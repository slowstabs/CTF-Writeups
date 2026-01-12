## Lab 5 - Memlabs

> We received this memory dump from our client recently. Someone accessed his system when he was not there and he found some rather strange files being accessed. Find those files and they might be useful. I quote his exact statement, `The names were not readable. They were composed of alphabets and numbers but I wasn't able to make out what exactly it was.`
> 
> Also, he noticed his most loved application that he always used crashed every time he ran it. Was it a virus?
> 
> Note-1: This challenge is composed of 3 flags. If you think 2nd flag is the end, it isn't!! :P
> Note-2: There was a small mistake when making this challenge. If you find any string which has the string "L4B_3_D0n3!!" in it, please change it to "L4B_5_D0n3!!" and then proceed.
> Note-3: You'll get the stage 2 flag only when you have the stage 1 flag.

On running `pslist` there's quite a few interesting processes. 

<img width="1484" height="658" alt="image" src="https://github.com/user-attachments/assets/15675b76-c64e-4fe8-a7c9-d91a3587bcfc" />

There's 4 different processes of `NOTEPAD.exe` which doesn't seem right. On running `cmdline` we also see that `WerFault.exe` is also being executed from `/SysWOW64/` taking arguments as the PID of the (potential) fake notepad, indicating a crash ie: matching the chall desc. Finally a .rar file called `SW1wb3J0YW50.rar`

<img width="1690" height="720" alt="image" src="https://github.com/user-attachments/assets/29a413ad-d3aa-4a02-8d60-cbcf7bf995aa" />

> WerFault (Windows Error Reporting): Used for handling errors, it is an external program which is called as soon as a program crashes or runs into an error, with arguments being PID and Thread ID.

Now I dumped the 3 supposed fake notepads and the .rar file using `dumpfiles`.

<img width="1417" height="284" alt="image" src="https://github.com/user-attachments/assets/74be7b03-6b56-4abd-a802-fffd484fb80a" />

<img width="1213" height="391" alt="image" src="https://github.com/user-attachments/assets/5ac1754a-357d-4634-af5e-11b64181c372" />


The .rar file needed a password, meaning it was for the second stage. 

I got pretty lost now since I don't really know any vol based approaches from here so I just tried a little reverse engineering as `file` showed that the dumps were .exe files. On running IDA on the .dat file, I found a flag in the IDA view. 

<img width="1370" height="608" alt="image" src="https://github.com/user-attachments/assets/040bda06-e90c-43af-99f7-e739a81f550e" />

Flag: `bi0s{M3m_l4B5_OVeR_!}`

I tried the flag as the password for the .rar, and it failed. Which meant that this was the 3rd flag. 

To find the first flag, I kinda lost all ideas so I looked it up and I had to run `screenshot`. When I did, it output around 15 images, in which one of them had a base64 string in the image. 

<img width="1292" height="347" alt="image" src="https://github.com/user-attachments/assets/1a8b9ee1-abac-4e75-8e5d-b9179878aad1" />

I ran `strings` on the memory dump and found the string in it instead of typing it out and converted it to plaintext from b64.

<img width="968" height="300" alt="image" src="https://github.com/user-attachments/assets/c59b13d3-05b0-4a2e-8d79-0ff22590a44d" />

Flag 1: `flag{!!_w3LL_d0n3_St4g3-1_0f_L4B_5_D0n3_!!}`

Finally using flag 1 as password for the archive, I got flag 2 which was inside the image.

<img width="1080" height="1080" alt="Stage2" src="https://github.com/user-attachments/assets/6532dffe-6cb0-454b-8ee9-1f6d02be428d" />

Flag 2: `flag{W1th_th1s_$taGe_2_1s_c0mPL3T3_!!}`

---

### Personal Gains

1. Learned that you should try everything. I didn't check `screenshot` or `clipboard` this time around which would've allowed me to solve the entire thing myself.
2. Learned about WER a little just off it being there, which is pretty cool. 







