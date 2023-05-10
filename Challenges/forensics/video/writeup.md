# Video with audio

> Amanda Papacosta

## Solving the challenge

To solve the challenge no programming script is needed and instead it can be manually solved using different programs.

### Initial observations

When intitally downloading the mp4 file it simply seems to be a video of cars driving with some music in the background. However, the audio file is concealing a number of secret files, and the challenge is to extract these and find the hidden flag within one of them. 

### Extracting the files

To extract the secret files from the video file one can use a program such as [Deepsound](https://www.jpinsoft.net/deepsound/download.aspx) or [VLC Media Player](https://www.videolan.org/vlc/). 

### Fiding the flag

The first two files contain false flags which have been decrypted using ROT13 or base64. There is no obvious way to know which method of encryption was used so it is up to the students themselves to try different methods or skip the decryption step completely. The third file is simply a text file containing the string "boats", which is the password for extracting the file hidden inside the fourth file (which is an image of sailing boats). To extract the file inside the image one can use a steganography tool such as [this one](https://futureboy.us/stegano/decinput.html) to access the data. 