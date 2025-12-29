## BypassCTF Forensics Writeups

### 1. Captian's Session

We're given a script which validates the questions along with a bunch of logs.

First question by the script is `What is the url of the bookmarked website?` 
- On inspecting the logs, bunch of em are sqlite3 DBs. On inspecting the DB called `Bookmarks`, we get website `isdf.dev`.
- Enter the answer, we get part 1 -> `BYPASS_CTF{My_d0g`

Second question asks for a password
- Inspecting `Login Data` DB, we get the password as `stepped on`.
- Enter the answer, we get part 2 -> `_0st3pp3d_0n_`

Got the third part by checking the History DB's url table.

<img width="879" height="69" alt="image" src="https://github.com/user-attachments/assets/d1d10509-2dce-432b-a570-6744a6f03e90" />

Flag: BYPASS_CTF{My_d0g_0st3pp3d_0n_4_b33_shh}

---



