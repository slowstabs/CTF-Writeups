## What lies within

> There's something in the building. Can you retrieve the flag?

We get an image called `buildings.png`, whose metadata I checked and it happened to actually be a png. Ran a quick `binwalk buildings.png` and observed compressed data in the image.

![image](https://github.com/user-attachments/assets/1dfe8267-7ce8-4ec4-a2c8-00b45063fd47)

Compressed data in png? zsteg is the key!

Ran a quick zsteg command to get the flag :D

![image](https://github.com/user-attachments/assets/418d8ea2-5037-4070-8e51-3a061d795c28)


