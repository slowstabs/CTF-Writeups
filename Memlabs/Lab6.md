## Lab 6 - Memlabs

> We received this memory dump from the Intelligence Bureau Department. They say this evidence might hold some secrets of the underworld gangster David Benjamin. This memory dump was taken from one of his workers whom the FBI busted earlier this week. Your job is to go through the memory dump and see if you can figure something out. FBI also says that David communicated with his workers via the internet so that might be a good place to start.
> Note: This challenge is composed of 1 flag split into 2 parts.
> 
> The flag format for this lab is: inctf{s0me_l33t_Str1ng}


On running the usual `imageinfo` and `pslist`, I got 3 main processes that were of interest of to me. Chrome, firefox and WinRaR. 

<img width="1279" height="650" alt="image" src="https://github.com/user-attachments/assets/6442fd8f-0378-4974-8fd1-7d1eda2f1472" />

I ran `cmdline` to see what arguments were given to these processes (winrar in specific) and found `flag.rar` in the results. 

<img width="1486" height="708" alt="image" src="https://github.com/user-attachments/assets/17f81782-349c-4523-9346-0faa380e66fc" />

Then using `filescan`, I found the address of the flag.rar and extracted it using `dumpfiles`. Seeing, how the challenges were before, this is probably needs a password and it did. So I pivoted from here towards the two other processes we found:
1. Chrome
 
From a previous challenge, I remember using `chromehistory` when chrome stuff was mentioned so I tried the same on this challenge. 



   
   
