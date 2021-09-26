# Armstrong Number Checker App
This app uses a simple user-friendly GUI to take input from the user and checks whether the given number is an Armstrong number or not and shows the result on the GUI (number is an Armstrong if sum of n-th power of each digit in the number is equal to number itself, where n is length of the number)

---
## Table of Contents
- [Requirements](#requirements)
- [How to Run](#how-to-run)
- [App Usage Example](#app-usage-example)
---


## Requirements
This project requires [Python3.8](https://www.python.org/downloads/release/python-380/) and the following Python library installed:
- [PyQt5](https://riverbankcomputing.com/software/pyqt)

Here is how to install the required library with the terminal or command window :<br />
```bash
pip install PyQt5
```
If you do not have pip installed, you can run the code below in the terminal or command window
- For Linux / MacOS
```bash
python get-pip.py
```
- For Windows
```bash
C:> py get-pip.py
```
These were the requirements for `Armstrong.py`. The `Armstrong.ipynb` requires [Jupyter Notebook](http://jupyter.org/install.html) to be installed on your computer.

## How to Run
Open the terminal or command window and run the code below:
* To run `Armstrong.py`,
```bash
python Armstrong.py
```
* To run `Armstrong.ipynb`
```bash
jupyter notebook Armstrong.ipynb
```

## App Usage Example
Put an integer in the input line and click on the **Check** button to see the result. Images below are some examples with different inputs, including wrong ones.

*  App Interface<br />
<br />![armstrong_1](https://user-images.githubusercontent.com/53794602/134506960-8c8a751a-2c05-415d-848d-bc29e15aee9f.png)<br />

* Valid input that is not an Armstrong number<br />
<br />![not_armstrong](https://user-images.githubusercontent.com/53794602/134586728-248b9604-22cb-48db-8359-ea5ed7bce123.png)<br />

* Valid input that is an Armstrong number<br />
<br />![is_armstrong](https://user-images.githubusercontent.com/53794602/134586748-c3463d5a-a8e6-46b6-b88b-554a00a5e2e4.png)<br />

* Special case - input 0 <br />
<br />![armstrong_0](https://user-images.githubusercontent.com/53794602/134586995-701c4857-fec7-4ce3-a8f4-0da9b585fad6.png)<br />


* If the user puts wrong input like float numbers, special characters or letters, it gives an error message<br />
<br />![armstrong_invalid](https://user-images.githubusercontent.com/53794602/134507572-36b5d7cd-a67d-4069-87fa-1bb46c3e18b6.png)<br />

* When the **Quit** button or close sign is clicked it asks the user whether he/she is sure about to close the app with the help of the message box<br />
<br />![armstrong_quit](https://user-images.githubusercontent.com/53794602/134507711-190192b0-3744-4527-b595-d2f161a03f3b.png)<br />
