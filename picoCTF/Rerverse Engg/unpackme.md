## unpackme

> Can you get the flag? Reverse engineer this binary.

On running the binary given in the challenge (called upackme-upx), it asks us for a favourite number. 

![image](https://github.com/user-attachments/assets/248420fb-3cf7-488f-b853-319e3a9c1e06)

To find this number, I did the most obvious thing and tried to open it in IDA but that didn't give me much. The file name said something related to UPX. So on running the command `strings unpackme-upx -n 20`, we find that it has indeed been packed with UPX.

![image](https://github.com/user-attachments/assets/b58d181b-9d38-48c8-af6c-becda2893565)
  
So using UPX we unpack it, and then run it in IDA again, find the pseudocode and we get the flag.

![image](https://github.com/user-attachments/assets/e003bec3-093c-4988-a2b4-3cae1fe2e8b7)

![image](https://github.com/user-attachments/assets/fa25385e-8fca-45d3-86c5-8496affa69ac)

![image](https://github.com/user-attachments/assets/26053ac7-ad29-4d51-ad11-dfdbe61e2cbf)

Flag: picoCTF{up><_m3_f7w_e510a27f}
