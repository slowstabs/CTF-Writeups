## File Types 

##### -> This file was found among some files marked confidential but my pdf reader cannot read it, maybe yours can. You can download the file from here.

(there was a much easier challenge by the same name so fuck this shit)

Ok so buckle up cuz this challenge is long long

First we are given a pdf called `File.pdf`, which when you try to open, says that it can't be opened. So we check what kind of file it is :

![image](https://github.com/slowstabs/CTF-Writeups/assets/148702248/3449e176-0b12-49f2-8707-69a9d78f2ed4)

We see that its a `.sh` file, so we change the file extention to .sh, give permissions are run the shell script

![image](https://github.com/slowstabs/CTF-Writeups/assets/148702248/7326de79-2a1e-4e88-9541-7d2d4f048c90)

On running the script we get a file called `flag`, this will happen multiple times so just repeat the process of finding out file type and extracting it again and again and again.
Many things can be extracted with `binwalk`, if not then the given zip types in the upcoming files will have their own decompressing so do that over and over.

Here's the order of files I had to go through with the decompression commands:

1. b2zip - `binwalk -e flag`
2. gzip - `binwalk -e 64`
3. lzip - `lzip -d -k flag`
4. lz4 - `lz4 -d -k flag`
5. lzma - `lzma -d -k flag`
6. lzop - `lzop -d -k 0`
7. so on i got bored


Finally you'll get to your final stage which will have a ASCII text file and inside it you'll see a string which looks like hex, run that in CyberChef and voila!

`picoCTF{f1len@m3_m@n1pul@t10n_f0r_0b2cur17y_3c79c5ba}`












