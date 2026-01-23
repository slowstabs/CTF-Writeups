# DFIR Labs - 2 Layer Security

>The police organized a surprise attack to catch the hacker along with all the exhibits at the scene. However, the hacker had foreseen that, so he encrypted his secret file before that. He even sarcastically said "you are too stupid to decrypt my 2-layer security"
> 
> Note: This challenge doesn't have any questions but the flag itself!

As the handout, I was given a linux file system. 

First thing I did was I went to the Desktop folder and there I found a file called `recycle.bin`. Couldn't do much of it since it seemed like gibberish data, might be useful later. Next I went to find `.bashrc_history` but I wasn't there but I found `.zsh_history` which showed certain commands being run on the zsh terminal. Something related encrypting a pdf with gpg and then deleting the original file.

<img width="1229" height="511" alt="image" src="https://github.com/user-attachments/assets/f1698088-50f6-4844-b9e9-7c5a78ea7dea" />





```
powershell -ExecutionPolicy Bypass -File .\fix.ps1
```
