**Her Majesty’s Conundrum**

300

_Her Royal Highness is in a peculiar situation and since she hasn't touched a laptop since… forever, help her?_

_Link To Resources : https://drive.google.com/drive/folders/1Z5J6JpgI1OHgz3POkLRr4JAiEoQSonWg_

On the drive, we get an image and a zip file. While looking through the metadata of the image, exiftool said skipped bytes so I checked the image's hex and found `221BBakerStreet`.

The files in the blobs directory in the .rar file are all zip files so I ran a simple grep to find the string we just found. 

![image](https://github.com/user-attachments/assets/3da19d8e-878b-4e6a-92dc-b6bfbdd90875)

Going through the files in `dca7a6845ae23fac1b40d460a3acb443320dc53b66964acb93ac387307212400` we find a CPP program which has two github links, one with a QR code and other with obviously, a rickroll. 

```cpp
#include <iostream>
#include <string>

using namespace std;

int main(void){
	string ans = "drwa1s0n";
	string wngans = "221BBakerStreet";
	cout<<"Enter the magical text : ";
	string userinp;
	cin>>userinp;
	if(userinp == ans){
		cout<<"Voila!!! To all your questions, {{{Affine}}}}}}}}'s your answer."<<endl;
		cout<<"https://github.com/vin06eet/mltrek.git"<<endl;
	}
	else if(userinp == wngans){
		cout<<"Hurray Mate!!! You are now closer than ever to the truth"<<endl;
		cout<<"https://github.com/vin06eet/Sherlock.git"<<endl;
	}
	else{
		cout<<"Not So Fast Sherlock..."<<endl;
	}
	return 0;
}
```

The QR code took us to a google doc which had a string on it: `Nd3R15i993i7ivo30xPi6cX7ivo3kOi7xiz`.

On paying a little more attention on the cpp file, I spotted `Affine`, indicating affine cipher. 

But we need an A and B coefficient in Affine cipher, the indicator to this was the brackets in the code which had 3 on the right side and 8 on the left side. Using 3 and 8 as coefficients, we get our flag.

Flag: Th3D15a993a7anc30fLa6yF7anc3sCa7fax

