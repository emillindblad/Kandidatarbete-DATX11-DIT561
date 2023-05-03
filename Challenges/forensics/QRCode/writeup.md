# QR code 

> Amanda Papacosta

## Solving the challenge

To solve the challenge no programming script is needed and instead can be manually solved using different programs or Unix commands.

### Initial observations
Upon first glance the challenge consists of a seriers of QR code frames appearing one after the other. The first step is to find a way to extract the different frames to then assemble into whole QR codes.

### Extracting and assembling the QR codes

To extract the frames from the GIF file there are multiple different online programs one can use, one example being [ezgif.com](https://ezgif.com/). After the frames have been extracted and downloaded, sort them into different folders for the different colors. Next step is to merge the same colored frames together into one large picture, which can be done in one of the following ways:

* Use an online program such as [filesmerge.com](https://www.filesmerge.com/merge-images)
* Use the Unix command *convert -append [filenames] [outputFile]* 

### Finding the flag

When the five QR codes have been assembled the next step is to scan them and realize that only the purple and red QR codes contain different parts of the flag. A hint for realizing how to decode the flag is the fact that the data from the red QR code ends in a “=”, which means it is the end of a base64 encoded string (since there was not a clean multiple of 3). Therefore, the string to be decoded looks like the following: "purpleString" ++ "redString". To decode the full string one can either use an online program such as [base64decode.org](https://www.base64decode.org/) or from the command line tool using *echo "theStringToBeDecoded" | base64 -d*.

