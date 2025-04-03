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

---

