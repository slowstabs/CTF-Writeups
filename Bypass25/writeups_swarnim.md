# Bypass25 CTF Writeups  
## Team: **TrickedMyAunty**

---

## 📑 Index

### 🔐 Cryptography
- [Chaotic Trust](#chaotic-trust)
- [Whispers of the Cursed Scroll](#whispers-of-the-cursed-scroll)
- [The Key Was Never Text](#the-key-was-never-text)
- [Once More Unto the Same Wind](#once-more-unto-the-same-wind)

### 📂 Steganography
- [Gold Challenge](#gold-challenge)


### 🌐 Web
- [The Lost Log Book](#the-lost-log-book)
- [Pirate's Hidden Cove](#pirates-hidden-cove)
- [Pirate's Treasure Hunt](#pirates-treasure-hunt)
- [A Treasure That Doesn’t Exist](#a-treasure-that-doesnt-exist)
- [The Cursed Archive](#the-cursed-archive)

### 🎲 Miscellaneous
- [Level Devil](#level-devil)
- [The Heart Beneath the Hull](#the-heart-beneath-the-hull)
- [Follow the trend](#follow-the-trend)
- [Hungry, Not Stupid](#hungry-not-stupid)

### 🧭 Other
- [No Follow, No Treasure 1](#no-follow-no-treasure-1)

---

## 🔐 Cryptography

---

## Chaotic Trust

**Category:** Cryptography  

### Challenge Description
Chaos was used to generate a keystream for encrypting the flag using XOR.
A partial keystream leak was left behind during debugging.

Chaos on computers isn’t always unpredictable.
Can you exploit floating-point precision and recover the flag?

**Files Provided**
- `chall.py`
- `output_cphsRGh.txt`


### Solution
- uses the equation `xn+1​=r⋅xn​⋅(1−xn​) with r=3.99`
- so x2 is​ using the logistic map and checked if its last 2 bytes match the second chunk of the leak.
- got the python script generated to XOR with ciphertext to recover plaintext
```
import struct

cipher_hex = "9f672a7efb6ec57d0379727c360bc968c07e8b6a256acc0a850f4c608b6a9e0b5472f11f0d"
cipher = bytes.fromhex(cipher_hex)

seed = 0.123456 

def logistic_map(x, r=3.99):
    return r * x * (1 - x)

keystream = b""
x = seed
while len(keystream) < len(cipher):
    x = logistic_map(x)
    keystream += struct.pack('<f', x)[-2:]

flag = bytes(a ^ b for a, b in zip(cipher, keystream))
print(f"Flag: {flag.decode()}")
```
```
fsociety@FSOCIETY:~$ python3 0.py
Flag: BYPASS_CTF{CH40T1C_TRU57_15_4W350M3!}
```
### Flag
**BYPASS_CTF{CH40T1C_TRU57_15_4W350M3!}**


---

## Whispers of the Cursed Scroll

**Category:** Cryptography  

### Challenge Description
An old pirate scroll has resurfaced from the depths of the sea.
It looks ordinary… maybe even some code.

But sailors who dismissed it were never seen again.

Legends say the message was hidden not in what is written,

The sea doesn’t shout its secrets.
Only those who read between the lines survive. ☠️⚓

Don't trust me I am Lier...

**File Provided**
- `They_call_me_Cutie.txt`

### Solution
- When opened file it was S, T and L's 
- By looking up the [Whitespace language specification](https://en.wikipedia.org/wiki/Whitespace_(programming_language)), the code repeats a specific structure:
- [Space] [Space] (Mapped as S S).
- Binary values `S=0` `T=1`
- [Line Feed] (Mapped as L)
```
remove command S S: We are left with S T S S S S T S L.

remove terminator L: We are left with S T S S S S T S.

convert to binary:

    S → 0

    T → 1

    result: 01000010

convert to ASCII: 01000010 in binary is 66 in decimal.

result: ASCII 66 is the letter 'B'.
```
- So we write a quick py script to decode the whole thing and we get the flag `BYPASS_CTF{Wh1tsp4c3_cut13_1t_w4s}`

### Flag
**BYPASS_CTF{Wh1tsp4c3_cut13_1t_w4s}**


---

## The Key Was Never Text

**Category:** Cryptography  

### Challenge Description
He never trusted digital things.
His favorite key was something with hands but no voice.

>“The face tells you everything if you know how to read it.”

You recovered this message:

18 5 25 11 10 1 22 9 11 9 3 5 12 1 14 4

Flag Format- BYPASS_CTF{ANSWER_IN_UPPERCASE_NO_SPACES}

**Flag Format**
BYPASS_CTF{ANSWER_IN_UPPERCASE_NO_SPACES}



### Solution
- the hint itself tells this is a `A1Z26 cipher`
- headed to [A1Z26 cipher decoder](https://cryptii.com/pipes/a1z26-cipher)
![cipher](img/A1Z26.png)

### Flag
**BYPASS_CTF{REYKJAVIKICELAND}**


---

## Once More Unto the Same Wind

**Category:** Cryptography  

### Challenge Description
The crew of the Black Horizon believed their cipher unbreakable.
Captain Blackwind swore by the Galois Seal — “no blade can cut it, no storm can bend it.”

Yet in his haste, the navigator trusted the same wind to carry more than one message.

**Files Provided**
- `output_RIIqaYT.txt`
- `nn.txt`
- `enq_EQq1fJa.py`

### Analysis
reusing the same key or nonce in cryptography is fatal.  
the phrase *“same wind”* hints at **key reuse**.

### Solution
- this is a `AES-GCM` keystream is XORed with the plaintext to create the ciphertext
- `enq_EQq1fJa.py` had static key and static nonce 
- two different plaintexts `known_plaintext` and `FLAG` are encrypted using this exact same Key/Nonce pair
- got a py script to decode this.
```
import binascii

def solve():
    c1_hex = "7713283f5e9979693d337dc27b7f5575350591c530d1d4c9070607c898be0588e5cf437aef"
    c2_hex = "740b393f4c8b676b283447f14f534b5d071bb2e105e4f0fa19332ee8b7a027a0d4e66749d3"

    c1 = bytes.fromhex(c1_hex)
    c2 = bytes.fromhex(c2_hex)

    p1 = b"A" * len(c1)

    flag_bytes = bytes([b1 ^ b2 ^ b3 for b1, b2, b3 in zip(c1, c2, p1)])

    print(f"Flag found: {flag_bytes.decode('utf-8')}")

if __name__ == "__main__":
    solve()
```
```
fsociety@FSOCIETY:~$ python3 4.py
Flag found: BYPASS_CTF{rum_is_better_than_cipher}

fsociety@FSOCIETY:~$
```

### Flag
**BYPASS_CTF{rum_is_better_than_cipher}**

---

## 📂 Steganography

---

## Gold Challenge

**Category:** Steganography

### Challenge Description
The challenge is contained within the Medallion_of_Cortez.bmp file.

This cursed coin holds more than just gold.

They say the greed of those who plundered it left a stain upon its very soul—a fractured image, visible only to those who can peel back the layers of light.

To lift the curse, you must first reassemble the key. Once the key is whole, its message will grant you the power to unlock the true treasure within.

Beware, for the final step is guarded, and only the words revealed by the light will let you pass.

**File Provided**
- `Medallion_of_Cortez.bmp`

### Solution
- the des and clues `peel back the layers of light` and `fractured image` says its a  Bit Plane Slicing, specifically looking at the Least Significant Bits `LSB`
- py script to extract LSB of RGB channel
```
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

img_path = 'Medallion_of_Cortez.bmp'
img = Image.open(img_path)
data = np.array(img)

r_lsb = (data[:, :, 0] & 1) * 255
g_lsb = (data[:, :, 1] & 1) * 255
b_lsb = (data[:, :, 2] & 1) * 255

fig, axes = plt.subplots(1, 3, figsize=(15, 5))
titles = ['Red Channel LSB', 'Green Channel LSB', 'Blue Channel LSB']
layers = [r_lsb, g_lsb, b_lsb]

for ax, layer, title in zip(axes, layers, titles):
    ax.imshow(layer, cmap='gray')
    ax.set_title(title)
    ax.axis('off')

plt.tight_layout()
plt.savefig('extracted_layers.png')
```

- this gives us `extracted_layers.png` which has a `qr code`
![extracted](img/extracted_layers.png)

- when scanned the qr code we get the key `SunlightRevealsAll`
- now it is clear, thats not the flag but ran to run `steghide`

<img src="img/steghide.png" width="500">

### Flag
**BYPASS_CTF{Aztec_Gold_Curse_Lifted}**

---

## 🌐 Web

---

## The Lost Log Book

**Category:** Web  

### Challenge Description
Sail into unsafe waters where faulty authentication and obscured routes guard valuable secrets. There’s more than meets the eye in this pirate portal — hidden methods await those bold enough to look past the browser’s limits.

Flag Format:- BYPASS_CTF{.......}

**URL**
http://20.196.136.66:18008/

### Solution

- website had a login page, so tried sql injection payload `' or true--` in password field and username random.
![login](img/sqlreq.png)
![loginsuccess](img/loginsuccess.png)

- Request fetch treasure map had an output `Zvffvat K-Cvengr urnqre.` decoded rot13 to `Missing X-Pirate header.`
![fetch](img/fetch.png)

- Added headers as `X-Pirate: Jack` then it gives `VHJhY2UgbG9nYm9vaw==` when decoded base64 it gives `Trace logbook`

- sent request to `/logbook` with method `TRACE`
![trace](img/trace.png)

### Flag
**BYPASS_CTF{D0nt_trust_a11}**

---

## Pirate's Hidden Cove

**Category:** Web  

### Challenge Description
You've discovered a secret pirate cove, hidden deep within the Tor network — a place where digital buccaneers stash their treasures. Somewhere on these sites lies the captain's flag. Can you find the 📄.

**URL**
[sjvsa2qdemto3sgcf2s76fbxup5fxqkt6tmgslzgj2qsuxeafbqnicyd.onion](http://sjvsa2qdemto3sgcf2s76fbxup5fxqkt6tmgslzgj2qsuxeafbqnicyd.onion/)

### Solution
- Start your tor and browse the url given.
![tor](img/tor.png)

- Ran ffuf `ffuf -u http://sjvsa2qdemto3sgcf2s76fbxup5fxqkt6tmgslzgj2qsuxeafbqnicyd.onion/FUZZ -w dirsearch.txt -e .txt,.html,.md,.zip,.bak,.env -x socks5://127.0.0.1:9050` 
![ffuf](img/ffuf.png)

- the .env had the flag in plain text.

### Flag
**BYPASS_CTF{T0r_r0ut314}**

---

## Pirate's Treasure Hunt

**Category:** Web  

### Challenge Description
Set sail on an adventure through the treacherous seas of mathematics! Navigate through 20 nautical challenges, each more perilous than the last. Solve riddles of arithmetic under time pressure as the Kraken closes in. Only those who master the pirate code of division, multiplication, and conquest can claim the legendary pirate's map.

**URL**
http://20.196.136.66:3600/

### Solution
- This chall was where we get 5 seconds to solve each question which was easy to hardesttt impossible to solve in 5 seconds, so i thought of interceptiog the request and i saw the server side was not validating the progress so sent it to intruder and added numbers payload from 1 to 20 for a garbage value (aim was to send this request 20 times untill the progress is 20)
![reqqq](img/reqint.png)

- Response with less length had the flag.
![flagmath](img/flagmath.png)

### Flag
**BYPASS_CTF{d1v1d3_n_c0nqu3r_l1k3_4_p1r4t3}**


---

## A Treasure That Doesn’t Exist

**Category:** Web  

### Challenge Description
The page insists it's not here — a digital dead end. Yet, something about this absence feels… intentional.  
> Pages may lie, but the browser doesn’t.

**URL**
https://tressurefound.vercel.app/


### Solution
- Inspect network requests, navigated to /favicon.ico which throwed a 404, but still had a response, when tried to save it directly it showed file not available on server, so tried to download it from the `Network Tab > Preview`
![pirate](img/pirate.png)

- Now ran `strings favicon.ico` and got the flag. ;-;
![pirate](img/stringspirate.png)

### Flag
**BYPASS_CTF{404_Err0r_N0t_F0und_v}**

---

## The Cursed Archive

**Category:** Web  

### Challenge Description
We stumbled upon a strange fan site hosting a collection of Pirates of the Caribbean movies. It looks like a simple static gallery, but our scanners picked up strange energy signatures coming from the server. Do React.

**URL**
http://20.196.144.202:3000/

### Solution
- When I loaded the webpage i saw the headers in request had `rsc, next-router` running on `nextjs 16.0.6` there I knew it was a CVE.
- As a bugbounty hunter I knew about `CVE-2025-55182` and I used to use an extension from [mrknow001](https://github.com/mrknow001/RSC_Detector) to hunt for vulns. there it was confirmed that it was a `React2Shell`
![r2c](img/r2s.png)

- now when I ran `ls` I found there was a `flag.txt` but when you read it it gave whitespaces so had to read it as base64 so used `base64 flag.txt` 
![bflag](img/bflag.png)

- now ran this command on my terminal and got the flag.txt on my terminal `echo "BASE64_HERE" | base64 -d > flag.txt`

- now when removed whitespaces \x00 and decoded as
```
P1: BYPASS_CTF{R34ct

checking vc might help

```
- the flag had 3 parts P1, P2 and P3. so we got the P1 `BYPASS_CTF{R34ct` and it says checking vc which means `version control .git` and looking into previous commits.

```
[+] Command: git branch
[+] Output:
  check
* main
```
- check branch looked suspicious so I tried to look into check branch `git show check`

![p3](img/p3.png)

- BOOM!!! P3: `Acc3ss}`
- Now we have P1 and P3, so P2?
- I remember saw few trails `6b71d2c` `9bca028^`
- So I ran `git show 6b71d2c` and got a [pastebin](https://pastebin.com/D7V0Urjh) link.
- Got the P2: `_2she111_`
- Now the final flag `P1+P2+P3 = BYPASS_CTF{R34ct_2she111_Acc3ss}`

### Flag
**BYPASS_CTF{R34ct_2she111_Acc3ss}**

---

## 🎲 Miscellaneous

---

## Level Devil

**Category:** Miscellaneous  

### Challenge Description
Looks simple. Plays dirty.

Welcome to Level Devil, a platformer that refuses to play fair.
The path looks obvious, the goal seems close—but this level thrives on deception.

Hidden traps, unreliable platforms, and misleading progress will test your patience and awareness.
Not everything you see is safe, and not every solution lies in plain sight.

Your mission is simple:
Reach the end and claim what’s hidden.

But remember—
in this level, trust is your biggest weakness.

Good luck. You’ll need it.

**Link**
https://level-devil-dcmi.onrender.com/

### Solution
- this chall has a browser-based game
- the game is designed to be extremely difficult, hidden spikes, falling platforms, and "troll" mechanics that kill the player unexpectedly.
- upon inspecting the source `ctrl+u` the game logic was exposed.
- mostly three specific API calls found in the script 
- `POST /api/start` – Initiates a session and returns a `session_id`.
- `POST /api/collect_flag` – Called when the player touches the specific "flag" tile in the game.
- `POST /api/win` – Called when the player reaches the door.
- server side does not verify if the player actually jumped over the spikes or traversed the map, it only checks if the API calls are made in the correct order for a valid session ID.
- here had to write a js to run in the browser console and also added the sleeper to avoid `Time-Based Heuristic (Speed Check)`
```
(async () => {
    const start = await fetch('/api/start', { method: 'POST' }).then(r => r.json());
    console.log(`[+] Session Active: ${start.session_id}`);

    console.log("[*] Simulating human gameplay (Waiting 25s)...");
    await new Promise(r => setTimeout(r, 25000));

    await fetch('/api/collect_flag', {
        method: 'POST',
        headers: {'Content-Type':'application/json'},
        body: JSON.stringify({session_id: start.session_id})
    });

    const response = await fetch('/api/win', {
        method: 'POST',
        headers: {'Content-Type':'application/json'},
        body: JSON.stringify({session_id: start.session_id})
    }).then(r => r.json());

    if (response.flag) {
        console.log("%c[PWNED] Flag: " + response.flag, "color:lime; font-size:14px");
        alert(response.flag);
    } else {
        console.error("Failed:", response);
    }
})();
```
![game](img/game.png)

### Flag
**BYPASS_CTF{l3v3l_d3v1l_n0t_s0_1nn0c3nt}**

---


## The Heart Beneath the Hull

**Category:** Miscellaneous  

### Challenge Description
Not all treasures are buried in sand,

**File Provided**
- `yo.png`

### Solution
- so the image when opened showed a devboard with pin numbers
- `68 65 61 72 74 5f 69 6e 5f 61 5f 63 68 65 73 74`
- opened cyber chef and decoded it to ascii `heart_in_a_chest`
![cc](img/cc.png)

### Flag
**BYPASS_CTF{heart_in_a_chest}**

---


## Follow the trend

**Category:** Miscellaneous  

### Challenge Description
Did you Doomscroll??

>This challenge filters spectators from participants. Spectators don’t get flag

**Link**
https://www.instagram.com/bypass_ctf/

### Solution
- This was one more hilarious I can say.
- It took me to their instagram page, I started looking into bio, links, nothing worked, then read the chall description again.
- questioned myself, what do i do when i open instagram?
- sad realization that `no interaction = no flag`
- i had to login from my alt acc and then i started liking commenting `(flag, bypass_ctf)` on all reels, then I got a dm saying `here your flag pirate`
<img src="img/insta.jpeg" width="350">

### Flag
**BYPASS_CTF{i_l0v3_i$d4}**

---

## Hungry Not Stupid

**Category:** Miscellaneous  

### Challenge Description
The snake is hungry — not desperate. Most food is a lie. Only those who observe, experiment, and learn will survive long enough to reach the flag.

**Link**
https://snack-mxc1.onrender.com/

### Solution
- this chall was a snake game where we had "eat the correct food" to reveal the flag, character by character. A single wrong move resets the entire game progress. With multiple food options spawning each turn and no visual indicators of which was correct, the probability of guessing correctly 20+ times in a row was impossible.
- found the game logic in the [game.js](https://snack-mxc1.onrender.com/static/js/game.js) file
- the game was controlled via a REST APIs
- `POST /api/start` - Initiates the game, returns grid size and initial food.
- `POST /api/eat` - Validates a move. Returns `status: "correct"` (with a flag) or `status: "wrong"` (reset).
- while interceptiong the request found it was giving a json output
![snakereq](img/snakereq.png)

- now with the apis had to write a py script to get the correct food and get the flag
```
import requests, zlib, base64, json

BASE_URL = "https://snack-mxc1.onrender.com"

def decode_cookie(cookie_value):
    if cookie_value.startswith('.'): cookie_value = cookie_value[1:]
    payload = cookie_value.split('.')[0]
    payload += '=' * (4 - (len(payload) % 4)) # Fix padding
    return json.loads(zlib.decompress(base64.urlsafe_b64decode(payload)))

def pwn():
    s = requests.Session()
    s.post(f"{BASE_URL}/api/start")
    
    collected_flag = ""
    while True:
        try:
            data = decode_cookie(s.cookies['session'])
            target = data['correct_food_pos']
            
            res = s.post(f"{BASE_URL}/api/eat", json={
                "eaten_food_pos": target, 
                "snake_body": [{"x":0,"y":0}] 
            }).json()
            
            if res['status'] == 'correct':
                collected_flag += res['flag_char']
                print(f"Flag: {collected_flag}")
            elif res['status'] == 'win':
                print(f"FULL FLAG: {res['full_flag']}")
                break
        except Exception:
            break

if __name__ == "__main__":
    pwn()
```
<img src="img/snakeflag.png" width="450">

### Flag
**BYPASS_CTF{5n4k3_1s_v3ry_l0ng}**

---

## 🧭 Other

---

## No Follow, No Treasure 1

**Category:** Other  

### Challenge Description
Access denied.

Reason: No social footprint detected.

Authenticate yourself at the official Bypass CTF page
and leave a visible trace.

Flag unlocks post-verification.

>Just look around the ship; sometimes the pirates carry the flag.

**Link**
https://discord.gg/MkDXpPm6Pt

### Solution
- Part1: in #welcome channel description had a spoiler text `BYPASS_CTF{w3lc0m3`
![spoiler](img/spoiler.png)

- Part2: this one tricked me out so bad. when I saw the emojies in the server one said `:_t00_:`
![emoji](img/emoji.png)

- Part3: description said `pirates carry the flag`, I started asking mods for the flags lol, but when I opened `jrdevadattan`s profile banner had the flag `byp4ss_ctf}`
![deva](img/deva.png)

### Flag
**BYPASS_CTF{w3lc0m3_t00_byp4ss_ctf}**

---

## SOCIALS

- [LinkedIn](https://www.linkedin.com/in/swarnimbandekar)
- [Medium](https://medium.com/@swarnimbandekar)
- [GitHub](https://github.com/swarnimbandekar)
---
