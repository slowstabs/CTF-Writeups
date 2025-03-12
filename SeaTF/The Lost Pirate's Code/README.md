**The Lost Pirate’s Code**

300

_Ahoy, matey! A legendary pirate’s hidden treasure lies within a set of mysterious artifacts, but the map has been encoded in a way only the sharpest minds can decipher. The infamous Captain Blackbeard has left behind clues, and it’s up to you to break the curse and claim the gold!_

_Treasure Chest Contents: 🏴‍☠️ Ancient Relic 1 – A weathered parchment, holding secrets of the past. 🏴‍☠️ Ancient Relic 2 – Another fragment of the lost treasure map. ⚓ cipher_script.py – A cryptic script that might need some tweaks to reveal the truth._

_Use your wits, follow the clues, and unlock the pirate’s code!_

_Resources : https://drive.google.com/drive/folders/1ZDrL2OsVbPUBE_pqVaDHKjo9VZkRXlPh https://drive.google.com/file/d/1c9hnzoV34XNFQe1JU_hYlFA3WVEWv96N/view?usp=sharing_ 

Our first step is fix the QR code using the script given which has a variable called `mississippi` . 

Through the second drive link we get the formula to calculate mississippi

![image](https://github.com/user-attachments/assets/e6596c97-7b63-47d1-a10e-ee8f59cd4b6c)

We find the mississippi by finding the values usingL 

```python
from PIL import Image
import numpy as np

# Load the uploaded image
image_path = "image2.jpg"
image = Image.open(image_path)

# Convert image to numpy array
image_array = np.array(image)

# Extract color channels
red_channel = image_array[:, :, 0].astype(int)
green_channel = image_array[:, :, 1].astype(int)
blue_channel = image_array[:, :, 2].astype(int)

# Compute required sums
sum_blue = np.sum(blue_channel)
sum_red_minus_green = np.sum(red_channel - green_channel)

# Compute "mississippis" value
if sum_red_minus_green != 0:
    mississippis = sum_blue // sum_red_minus_green  # Floor division
else:
    mississippis = None  # Avoid division by zero

```
Which comes out to be `17`

Input the value of mississippi into the original script given and we get our fixed QR code, which on scanning leads to a password protected PDF called `sigmaredtimessigmagreen.pdf`.

Indicating the password is the number of red pixels times the number of green ones. I used another script to find the number:

```python
from PIL import Image
import numpy as np

# Load the image
image_path = "/mnt/data/image2.jpg"
image = Image.open(image_path)

# Convert image to numpy array
image_array = np.array(image)

# Extract red and green channels
red_channel = image_array[:, :, 0]  # Red channel
green_channel = image_array[:, :, 1]  # Green channel

# Calculate the sum of red and green values
sum_red = np.sum(red_channel)
sum_green = np.sum(green_channel)

# Compute the product of the sums
result = sum_red * sum_green
```
Which gave me the password `1206825409333124`.

And then I had Sheldon Cooper looking at me with the flag.

Flag: SeaTF{ML_Mystery_1231y_decoded}


