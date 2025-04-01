## Naughty Cat

Points: 436

>  One sneaky cat has tucked something away in a secure vault, wrapped up tight with a password. You’ve got the key… or at least, a way to find it. Can you crack open the mystery and uncover what the feline is hiding? 🐱🔐

We are given a zip file called `secret.zip` which is password protected. On bruteforcing with rockyou, we get the password to be `trustno1`. We get an image of the beluga cat pfp saying "Im not hiding".

tbf, I forgot what cmd I used but it said something along the lines of there being stuff after the trailer. This made me check the trailers on HxD, and there I found two trailers with the ending bit of jpgs which is `FF D9`. On looking at the first one, there seems to another jpg header right after the first one, indicating the presense of another image.

![image](https://github.com/user-attachments/assets/3c0e1129-69a2-4d60-968e-e03213d04a30)

I split the top and bottom into two different files and got two images. One of them gave us the flag.

![naughty2](https://github.com/user-attachments/assets/4c8c3391-d7fe-403d-9f06-14d78883cf8b)


Flag: `saic{f1n4lly_y0u_c4p7ur3d_m3_h1dd3n!!}`
