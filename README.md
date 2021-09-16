# Scriptor
Text to Handwriting converter. Enter text and generate hand written PDF document in seconds.

## HOW TO USE
#### Step 1: 
Download the installer and install it normaly, make sure to make desktop shortcut. Run Scriptor.exe
#### Step 2:
Write/Paste text in text box  that is to be converted to hand writing.  Hit WRITE and wait patiently for program to execute
#### Step 3:
WALLAH! Handwritten pages and PDF is stored in the OUTPUT folder. ENJOY :)


## HOW IT WORKS
To convert text to handwriting it has pre-stored letters, numbers and characters cropped as small png to create a dateset, reads the text and starts placing these letters accordingly on a blank white background. 
Before all that, the text is parsed into Pages then Words then letters. All these letters are send to a function which takes letters as input and throws handwritten image as output.
It has various dependencies like TKINTER, PILLOW, FPDF and runs on Python 3.6 or above.
The excutable is created using auto-py-to-exe.


## Folder/File structure is as follows
#### RES: 
It contains letter's image dataset used by script to write.
#### OUTPUT:
The generated PDF and images of hand written page by the script is stored in this folder.
#### SCRIPTOR.PY:
Main script responsible for converting and storing.
#### CROPPER:
Contains scratch scripts that user can use to create its own handwritten image dataset

Disclaimer: Any illegal/non accepable use of the script is not recommended and is useres responsibilty.Do not use for offical work or WRITING ASSIGNMENTS or similar.

