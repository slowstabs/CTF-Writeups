**Honest Mistake 🫠**

300

_One of organizers was a bit clumsy and revealed the questions to the public. However, they were smart enough to delete the solutions before leaking. But, hope you are smarter than them_

_Resources: seatf_questions.zip_

We have a zip file which is a git repository with a text file and two images. The images are red herrings but the text file gives us that we are ahead of time, so we need to go back in time. 

My first step was to try `git show` or `git log`. But both gave nothing.

On some searching I found `git fsck --full --no-reflogs` which lists orphaned commits as well. 

I found a commit there and I went back to it. 
![image](https://github.com/user-attachments/assets/9d4d55f4-b6b1-4054-b168-5d73562e74bd)

Ran `git log` on this branch to find more commits and went to correct one (trial and error)

**Honest Mistake 🫠**

300

_One of organizers was a bit clumsy and revealed the questions to the public. However, they were smart enough to delete the solutions before leaking. But, hope you are smarter than them_

_Resources: seatf_questions.zip_

We have a zip file which is a git repository with a text file and two images. The images are red herrings but the text file gives us that we are ahead of time, so we need to go back in time. 

My first step was to try `git show` or `git log`. But both gave nothing.

On some searching I found `git fsck --full --no-reflogs` which lists orphaned commits as well. 

I found a commit there and I went back to it. 
![image](https://github.com/user-attachments/assets/9d4d55f4-b6b1-4054-b168-5d73562e74bd)

Ran `git log` on this branch to find more commits and went to correct one (trial and error)





