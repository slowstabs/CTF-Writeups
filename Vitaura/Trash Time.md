## Trash time

> When was the flag deleted? Format: "YYYY-MM-DD HH:MM:SS"

Very annoyed that I wasn't able to solve this cuz of a very tiny thing.

We get a zip file with a folder inside with a hidden file inside it which contains a `desktop.ini` and `INFO2`. On a little research I realised that INFO2 files contain information about deleted files. 

On searching online I found a tool called `rifiuti2` which shows when a file was deleted similar to how a git log shows data. On running the command `rifiuti2 INFO2` I found when the files was deleted hence also the flag.

![image](https://github.com/user-attachments/assets/ab210291-9d81-4c7e-bb75-b968fe9b9ae0)

Flag: `2018-11-04 02:43:31`

PS: Mistaka I made was using `rifiuti` instead of `rifiuti2` :<<<

