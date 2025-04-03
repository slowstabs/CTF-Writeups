## Back in Time -1 (Welcome)

Solves: 41

Description: "Nothing to see here," they said. "Just ignore this file," they insisted. But we both know you're not a well-behaved bot, are you? 😏

Some secrets are hidden in plain sight—right where they told you NOT to look. Go on, take a peek. 🔍

---

This challenge was pretty straightforward with the flag just being directly available on the Welcome page on the website. The challenge name hinted directly towards it.

![image](https://github.com/user-attachments/assets/9f6d1122-0517-44d5-900d-3f17cfb854a3)

Flag: SAIC{w3lc0m3_t0_chr0n0s_ctf_2025}


## Back in Time - 2

Solves: 24

Description: Our secret club 'SAIC,IIT mandi' had a mole! 🕷️ One of our members couldn't keep their mouth shut and leaked some highly confidential information. As a result, we kicked them out—no more late-night hacking sessions or rooftop chai discussions for them!

But who was this traitor? 🤔

Our website has been cleaned up, but traces of the past might still exist. Your mission is to uncover the identity of the ex-member. Look carefully, dig deep, and find his README.

🕵️ Can you track him down before his mistakes are lost to time?

---

The challenge description asks us to find a person who was part of the saic club but was removed. The description was hinting heavily towards two things, one being their website and the other being the past. The website was available on the CTFd page and to go to the past we use Wayback Machine.

On inspecting Wayback Machine, we see a snapshot on `24th March 2025`. On going through the members page on the website, we find one that is not on the newer website anymore.

![image](https://github.com/user-attachments/assets/28d2e7be-1fe6-41df-b167-38950ce95704)

The website had the github link of that person who's readme had the flag.

![image](https://github.com/user-attachments/assets/964da13c-730c-45dc-9437-b15a8023ce44)

Flag: `saic{p@v1tr_g0t_c4ugh7_1n_w4yb4ck_w3b!!}`


## Back to Time - 3

Solves : 14

Description: A secret folder has been left behind on ex-SAIC member's GitHub that was never meant to be found. But what’s locked inside remains a mystery.

Rumors suggest that the key to unlocking it is hidden somewhere on the web, buried within paragraphs...

Your mission is to track down the password and reveal what lies within.

---

On inspecting the dude's github more, we find a repository called `Back to time III`. The repository had a zip file called `FLAG.zip` with a markdown file called `something.md`. `FLAG.zip` was as expected, password protected and was not crackable with rockyou.

I went through `something.md` which had a link which lead me to the wikipedia link of SpiderMan. The markdown file also had a hint saying that it is more than 8. Which made me interpret that the password for the zip was on the wikipedia page of Spiderman and had a length of more than 8 characters.

Therefore, I got a script to get all the words on the wikipedia site which were either 8 letters or longer and made a wordlist of them.

```python
import requests
from bs4 import BeautifulSoup
import re

# Wikipedia page URL
url = "https://en.wikipedia.org/wiki/Spider-Man"  # Change this to your target page

# Fetch the page content
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extract text content
text = soup.get_text()

# Extract words (considering only alphabetic words)
words = re.findall(r'\b[a-zA-Z]{8,}\b', text)

# Remove duplicates and sort
unique_words = sorted(set(words))

# Save to a wordlist file
with open("wordlist.txt", "w") as f:
    for word in unique_words:
        f.write(word + "\n")

print("Wordlist saved as wordlist.txt")

```

On using the new `wordlist.txt` as the wordlist on the hash of FLAG.zip, we get our password. 

![image](https://github.com/user-attachments/assets/6e4d48a7-00c2-4297-840c-b12ca50b80fd)

On opening the zip file with the password, we find the flag in it.

Flag: `saic{c3wl_w0rd5_f0r_bru73f0rc1ng!!}`


## Back to Time - 5


