## CrazyLCS

Points: 227

> The server plays hot-and-cold with your guesses—only telling you how much contiguous chunk matches the flag. No hints, no mercy, just pain. Can you piece it together, or will you substring yourself into madness? 😈🔍
nc iitmandi.co.in 8098

LCS which stands for longest common sequence, returns the length string depending on how similar two strings are in order from left to right. What we needed here was a script that could run through all alphanumeric characters and also symbols.

```python

import socket
import string

HOST = "iitmandi.co.in"
PORT = 8098

def get_lcs_length(guess):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.recv(1024)  # Read welcome message
        s.sendall(guess.encode() + b"\n")
        response = s.recv(1024).decode()
        return int(response.split(": ")[1])  # Extract LCS length

flag = "saic{"  # Start with the confirmed prefix

while True:
    found = False
    for char in string.printable:  # Test all printable characters
        test_flag = flag + char
        lcs_length = get_lcs_length(test_flag)
        
        if lcs_length == len(test_flag):  # If LCS matches guess length, it's correct
            flag = test_flag
            print(f"Progress: {flag}")
            found = True
            break  # Move to the next character
    
    if not found:
        print(f"Final flag: {flag}")
        break

```

This will take a while and eventually give us the flag. 

Flag: saic{3asy_dp_lc5_ch4ll3ng3}
