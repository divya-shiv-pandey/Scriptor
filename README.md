# Scriptor
Text to Handwriting converter. Enter text and generate hand written PDF document in seconds.To convert text to handwriting it has pre-stored letters, numbers and characters cropped as small png to create a dateset, reads the text and starts placing these letters accordingly on a blank white background. 

Before that all the text in the text is parsed into Pages then Words then letters. All these letters are send to a function which takes letters as input and throws handwritten image as output.

It has various dependencies like PILLOW, FPDF and runs on Python 3.6 or above.

## Foldar layout is as follows
### FILE: 
It contains letter's image dataset used by script to write.
### OUTPUT:
The generated PDF and images of hand written page by the script is stored in this folder.
### BLACK.TXT:
Script converts text in this file to hand writtting.
### SCRIPTOR.PY:
Main script responsible for converting and storing.
### CROPPER:
Contains scratch scripts that user can use to create its own handwritten image dataset

## HOW TO USE
### Step 1: 
UNZIP the folder
### Step 2:
Paste to be written text in BLACK.TXT file and save it.
### Step 3:
Run the SCRIPTOR.PY and wait for it to execute and auto exit.
### Step 4:
Handwritten pages and PDF is stored in the OUTPUT folder. ENJOY :)

Disclaimer: Any illegal/non accepable use of the script is not recommended and is useres responsibilty.Do not use for offical work or ASSIGNMENTS or similar.



