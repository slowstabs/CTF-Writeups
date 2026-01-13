## Lab 6 - Memlabs

> We received this memory dump from the Intelligence Bureau Department. They say this evidence might hold some secrets of the underworld gangster David Benjamin. This memory dump was taken from one of his workers whom the FBI busted earlier this week. Your job is to go through the memory dump and see if you can figure something out. FBI also says that David communicated with his workers via the internet so that might be a good place to start.
> Note: This challenge is composed of 1 flag split into 2 parts.
> 
> The flag format for this lab is: inctf{s0me_l33t_Str1ng}


On running the usual `imageinfo` and `pslist`, I got 3 main processes that were of interest of to me. Chrome, firefox and WinRaR. 

<img width="1279" height="650" alt="image" src="https://github.com/user-attachments/assets/6442fd8f-0378-4974-8fd1-7d1eda2f1472" />

I ran `cmdline` to see what arguments were given/ran on these processes (winrar in specific) and found `flag.rar` in the results. 

<img width="1486" height="708" alt="image" src="https://github.com/user-attachments/assets/17f81782-349c-4523-9346-0faa380e66fc" />

Then using `filescan`, I found the address of the flag.rar and extracted it using `dumpfiles`. Seeing, how the challenges were before, this is probably needs a password and it did. So I pivoted from here towards the two other processes we found:

1. Chrome
 
From a previous challenge, I remember using `chromehistory` when chrome stuff was mentioned so I tried the same on this challenge. 

<img width="1628" height="748" alt="image" src="https://github.com/user-attachments/assets/87e68096-7065-44dd-b002-7edb5334097e" />

I got a lot of chrome history but one that stood out was a pastebin link with a google docs link inside it. Also mentioning a key sent in E-Mail, might need this later but for now onto the google doc.

<img width="1289" height="462" alt="image" src="https://github.com/user-attachments/assets/22d63423-50b2-435b-9f03-5fe78cc3695f" />

The google doc had a lot of placeholder text but in the middle of page four there was a mega.nz asking for a decryption key. Now we need a key. It didn't seem like the chrome history had anything more so I switched to get the `firefoxhistory`. 

Command: `vol2 --plugins=/mnt/c/volatility-plugins -f MemoryDump_Lab6.raw --profile=Win7SP1x64 firefoxhistory`


nothing showed up...

Next I tried running `netscan` to see for any SMTP related stuff so that maybe I'd get something there. Again nothing.
I tried running `clipboard` and `screenshot` after this as a last resort and got a file name in one of the screenshots. 

<img width="1444" height="732" alt="image" src="https://github.com/user-attachments/assets/cf19b31c-fce0-46d6-a9e0-78c0de5c35a3" />

Using the string `Mega file key` I ran strings on the memory dump to see if I get anything useful, and I did get something.

<img width="1919" height="873" alt="image" src="https://github.com/user-attachments/assets/67246b08-3e0c-4cb5-901f-e02c572241c7" />

Since we got the key, I decrypted the file on mega and then downloaded it.






   
   
