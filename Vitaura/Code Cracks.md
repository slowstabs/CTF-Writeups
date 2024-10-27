## Code Cracks

Find the flag, from the given file.

File Given: file5.exe

On getting a .exe, I did the most obvious thing and ran the file. It asked me for a number input which on entering a number, closed the window. 

I decompiled the .exe file in IDA and found a buffer overflow vulnerability in the program. 

![image](https://github.com/user-attachments/assets/270a1569-309e-4b5d-a071-88b149abac84)

I put a string that is longer than 64 characters and got the flag. 

![image](https://github.com/user-attachments/assets/5f76b3d9-86b2-4b03-8062-de9149f6d4b0)


Flag: `fastctf{badcodefails}`
PS: It was already there in the IDA decompiled code lol
