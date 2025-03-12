**Black Pearl’s Cursed Cipher**

300 Pts

_Ahoy matey! Set sail on the perilous digital seas and dare to conquer the cursed binary to seize Captain Blackbeard’s secret flag! But beware—the dark sorcery of encrypted lore hides the treasure, and only the cleverest pirates shall prevail. To unlock the binary’s secrets, ye must first solve this ancient riddle:_

_Ciphertext: Hjg_KiFTyVaO_KvMcYHoYg_fReIoHi In a chest of secrets, the key awaits— Use "BLACKBEARD" to unlock the gates. Then shift each letter back by ten, so true— And the treasure will reveal its clue to you!_

_Use this command to run the file nc -v 0.cloud.chals.io 20832_

A cipher text with a key and immediate thought is Vigenere Cipher, which gave some random string which needs to be rotated by -10 according to question. This gave the text `Wow_YoUFoUnD_PlAiNTeXt_uWuWuWu`

Entered this as the netcat input, which gave a base64 string which on decoding gave the flag. 

![image](https://github.com/user-attachments/assets/3a1d2335-d28f-44e5-a69a-32b84a544337)

Flag: SeaTF{dAmN_ReVerSe_enGiNeEr_PrO}
