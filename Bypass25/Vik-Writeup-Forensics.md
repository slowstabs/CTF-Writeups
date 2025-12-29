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

### 2. Silas's Last Voyage

Analysis of the disk img gives us a bunch of deleted files. We get 3 files which are different from the others, 2 images and one .wav. The wav had morse code which read `Logs first path second coin third` which was to do with the order of the flags. 

The found two images when XOR'ed with each other gives the word `tales` which hits towards coin so third part.

<img width="400" height="400" alt="flag" src="https://github.com/user-attachments/assets/494c6c11-d534-47a7-89a7-70ad8a73347b" />

Honestly forgot how I got part two but I got `tell_no_` from a base64 string and having `tell_no_tales` hinted towards the flag being `dead_men_tell_no_tales`. Which happened to be correct.

Flag: BYPASS_CTF{dead_men_tell_no_tales}







