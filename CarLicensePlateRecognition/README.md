# Project Description
Aim to read characters in car number plates using image processing from scratch without OpenCV. Implementation of the project is done using Python.

## Installing requirements.txt
```
pip install -r requirements.txt
```
Project has no virtual environment. You can use your own environment to test the program.

## File CS373LicensePlateDetection.py  
This is the main task for the assignment. Plate recognition are done raw without OpenCV. Sample license plate (numberplate1 to 6) used for the markers to check the program are given in the directory. 

## File CS373_AssignmentExtension.py
This is the extension of the project. We are allowed to use libraries for the extension part. I used OpenCV, pytesseract, numpy and Pillow for the character recognition. First I used the main program from CS373LicensePlateDetection.py to read the characters, if the program is not giving any results in attempt to read the number plates, the program will then use the libraries I imported to try reading the plate for the 2nd time. I downloaded images numberplate7 to 10 as well as shortplate.png for the extension to see how accurate the image processing works. 

### Based on the results I got from the Extension part of the assignment, I provided the report in ExtensionReport.pdf

