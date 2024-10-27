## Crack the Cat

> Find the flag, from the given file

File given: file4

On receiving a extension less file, I ran exiftool to figure out what its format is. exif data tells us that it is a 7zip file so I added the `.7z` extension to it. 

![image](https://github.com/user-attachments/assets/0536105c-0f0c-4c25-8f00-ab4680ba6ccb)

On opening the zip file, we get a password protected .txt file. I proceeded to bruteforce the .txt file using rockyou as wordlist and I found the password.

![image](https://github.com/user-attachments/assets/ff40fdaa-e72f-407c-9437-9e804610e3a9)


Password: `12345abc`

After opening the txt file, we find a large string of base64 data. Decoded this from base64, and saw a png header when it did so I rendered an image using the decrypted base64 data which got me the flag.

![image](https://github.com/user-attachments/assets/8c167582-ab99-4445-b45a-20799bc03fbd)

Flag: `fastctf{the hashcat goes meow}`



