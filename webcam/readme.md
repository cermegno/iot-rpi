##Face Recognition
This folder contains a number of sample scripts to interact with the webcam. They are from a book from "MAKE". They are stepping stones to build the Photobooth experiment I showed during the session. The script with all the functionality is "photobooth.py" but you might find interesting other scripts like face-detector.py

If you want to use a standard USB webcam you will have to test that it works first. This link contains the list of hardware that is known to work with Raspberry PI:

http://elinux.org/RPi_VerifiedPeripherals

Although the list of webcams has been moved here

http://elinux.org/RPi_USB_Webcams

Use the "lucview" application. Please note that the official Raspberry Pi camera uses different software, but it is much better documented.
```
sudo apt-get install lucview
lucview
```
If the video is choppy you can reduce the resolution by doing 
```
lucview -s 320x240
```
The face recognition functionality is provided by SimpleCV. This one relies on other modules you need to install first
```
sudo apt-get install python-pip python-opencv python-scipy python-numpy
sudo pip install https://github.com/ingenuitas/SimpleCV/zipball/master
```
##Taking photos
Another handy tip for your projects is the ability to simply take a photo with a webcam even if you don't need face recognition or other stuff, ex: you might want to do the processing of that photo using an external API. A tool to do that is "fswebcam".

```
sudo apt-get install fswebcam
fswebcam -r 640x480 name_of_my_photo
```
If you need to trigger this from a Python script you can use "subprocess". This is comes by default so no need for pip here. Each word of the command you would have to run from the command line is an item in the list.
```python
import subprocess
subprocess.call(["notepad.exe","test.txt"])
# or if you have fswebcam installed ...
subprocess.call(["fswebcam","-r","640x480","name_of_my_photo"])
```

