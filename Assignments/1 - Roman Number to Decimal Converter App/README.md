# Roman Number to Decimal Converter App
This app uses a simple GUI to take input from a user which is expected to be a roman number and converts it to the integer (if the input is valid) or produces corresponding error message and shows it on the screen

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
These were the requirements for `Roman_to_Decimal.py`. The `Roman_to_Decimal.ipynb` requires [Jupyter Notebook](http://jupyter.org/install.html) to be installed on your computer.

## How to Run
Open the terminal or command window and run the code below:
* To run `Roman_to_Decimal.py`,
```bash
python Roman_to_Decimal.py
```
* To run `Roman_to_Decimal.ipynb`
```bash
jupyter notebook Roman_to_Decimal.ipynb
```

## App Usage Example
Put a Roman number in the input line and click on the **Convert** button to see its corresponding integer equivalent on the screen. Images below are some examples with different inputs, including wrong ones.
* App Interface <br />
<br />![Roman_1](https://user-images.githubusercontent.com/53794602/134482094-ca11159f-c466-4b44-9e27-2fcf037df350.png)<br />

* Valid Input<br />
<br />![correct_input](https://user-images.githubusercontent.com/53794602/134482161-477d683a-efc5-4854-90d3-d12adcdcd04b.png)<br />

* To handle wrong inputs from user, there is error message for non-roman characters<br />
<br />![invalid_input](https://user-images.githubusercontent.com/53794602/134482198-506e1b0b-fa25-4dd0-987e-a0315b718747.png)<br />


* Since roman numbers are all in capital form, small letter inputs are directly converted to capital leters<br />
<br />![case_sensitivity](https://user-images.githubusercontent.com/53794602/134482241-3171743e-44fc-4a96-8365-e0fef6f57e44.png)<br />

* Lastly, program doesn't allow to give 4 sequential characters since it is not accepted in roman numbers<br />
<br />![4_consecutive](https://user-images.githubusercontent.com/53794602/134482272-229e295b-9feb-4d45-9919-0f9beaead858.png)<br />

* When the **Quit** button or close window is clicked, message box appears to make sure user wants to close the app<br />
<br />![quit](https://user-images.githubusercontent.com/53794602/134482400-3c9f4acc-007a-4e39-8a3f-301f5f4bd873.png)<br />
