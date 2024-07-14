## convert_it

> What is palindrome?

We're given a zip file which on opening gave us a folder called `task` which had two files: 

![image](https://github.com/user-attachments/assets/b2491310-a37c-47b4-be6b-06e6b1b5a037)

The `testdata.zip` had a password protected .txt file and `datafile` folder had a bunch of .exe 

On a basic sleuth of the sizes of the .exe files, we find that just one isn't the same size as the others :
![image](https://github.com/user-attachments/assets/18f9491b-3746-4183-a602-b91152c31629)

On opening the file in terminal we get this string of characters: 
![image](https://github.com/user-attachments/assets/da5f0dd7-0fc7-415a-91f3-a5bef2d058de)

On observing we find a palindrome in it, we use this as the password of the .txt to get a base64 string which on decoding gives us the flag :D 

![image](https://github.com/user-attachments/assets/fd1d70bb-42aa-476e-9a36-6fe8dea22de4)
