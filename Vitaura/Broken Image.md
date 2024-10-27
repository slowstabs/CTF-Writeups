## Broken Image

> The image is broken can you find the secret flag

File given: file7.JPEG

The file, as the title suggested is broken and cannot be viewed. I ran it through HxD to see what the Hex formatting looked like where I found IHDR and IEND at the start and bottom of the Hex conversion. This pattern is commonly observed in PNGs and so I noticed that it was very much the same except the header.

![image](https://github.com/user-attachments/assets/4dac1c40-2ea5-4052-a61b-87d668c81941)

I took another random PNG that I had and copied the header of that png onto this image. Then I changed the file extention and got the flag in the image (horrible handwriting btw).

![image](https://github.com/user-attachments/assets/4a9e7122-b2b4-411b-a88d-bf27643f95eb)

Flag: `fastctf{PNGesus}`
