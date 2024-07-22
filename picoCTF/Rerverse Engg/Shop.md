## Shop

> Best Stuff - Cheap Stuff, Buy Buy Buy... Store Instance: source. The shop is open for business at nc mercury.picoctf.net xxxxx.

On running opening the `source` file in notepad, the header says ELF idicating a binary. So on running the binary we get a shop which sells and buys some stuff.

![image](https://github.com/user-attachments/assets/d6862b4d-8ccd-4086-ac11-c6a6de877e0a)

On some playing around with it I realised that I could buy item 0 and and item 1 even when I had no money left, meaning it would go negative. But this didn't really help me.

Next I tried to see if the script accepts negative values for quantity, which happened so that item 0 and 1 did and 3 didn't. On entering a negative value, with each purchase my money went up, what a life :O
So like that I could afford item 3 which says `Fruitful Flag` which I assumed would be the flag and there it was :D

![image](https://github.com/user-attachments/assets/f1c79317-f037-4530-85c7-65c7685d575f)

Ran the same steps through the netcat link and got the flag
