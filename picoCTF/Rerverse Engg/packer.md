## Packer

First thing that came to my mind when Isaw this challenge was UPX cuz packer. So on quick sleuth using `strings out -n 10`, I found the string that had information regarding UPX. 

![image](https://github.com/user-attachments/assets/632b7ee2-ba46-4e87-bd33-ee8943e69724)

Ran a quick `upx -d out` to unpack it and then decompiled it on IDA. On IDA we find a hex number which is found to be the flag on decoding.

![image](https://github.com/user-attachments/assets/7c4c19f5-6267-4077-bbd5-984e56685be5)


Flag: picoCTF{U9X_UnP4ck1N6_B1n4Ri3S_e190c3f3}
