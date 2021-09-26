from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QMessageBox
import sys

def roman_to_integer(roman:str) -> str:
    # clearing white spaces
    roman = roman.strip()
    dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    res = 0
    n = len(roman)
    for i in range(n):
        # check for invalid character
        if roman[i].upper() not in dic:
            return f'{roman[i]} is not a Roman character!'
        
        # check for 4 consecutive characters
        if i < n - 3:
            if ((roman[i].upper() == roman[i+1].upper()) and (roman[i].upper() == roman[i+2].upper()) \
                and (roman[i].upper() == roman[i+3].upper())):
                return '4 consecutive characters are not allowed!'
            
        # check for beginning and having smaller value at the left, if it's the case
        # we add corresponding integer for current character and subtract twice for on the left
        if i > 0 and dic[roman[i].upper()] > dic[roman[i-1].upper()]:
            res += dic[roman[i].upper()] - 2 * dic[roman[i-1].upper()]
            
        else:
            res += dic[roman[i].upper()]
            
    return str(res)

"""
This class creates user inerface that contains user input line explained by text label on the top,
followed by convert button that uses roman_to_integer function and displays output with explanatory text label,
and lastly a quit button to close the app with message box
"""                
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(500, 350, 500, 350)
        self.setWindowTitle('Roman to Decimal Converter')
        self.initUI()
    
    def initUI(self):
        self.input_label = QLabel(self)
        self.input_label.setText("Please, enter the Roman number: ")
        self.input_label.adjustSize()
        self.input_label.move(150, 10)
        
        self.line_edit = QLineEdit(self)
        self.line_edit.adjustSize()
        self.line_edit.move(175, 30)
        
        self.convert_button = QPushButton('Convert', self)
        self.convert_button.clicked.connect(self.click_convert)
        self.convert_button.move(195, 60)
        
        self.output_text = QLabel('Result:', self)
        self.output_text.move(150, 90)
        
        self.output_label = QLabel(self)
        self.output_label.move(175, 115)
        
        self.quit_button = QPushButton('Quit', self)
        self.quit_button.clicked.connect(self.click_quit)
        self.quit_button.move(195, 140)
        
        self.show()

    def closeEvent(self, event):
        close_reply=QMessageBox.question(self,'Message','Are you sure you want to quit?',\
            QMessageBox.Yes|QMessageBox.No,QMessageBox.No )
        if close_reply==QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    
    def click_quit(self):
        quit_reply=QMessageBox.question(self,'Message','Are you sure you want to quit?',\
            QMessageBox.Yes|QMessageBox.No,QMessageBox.No )
        if quit_reply==QMessageBox.Yes:
            QApplication.instance().quit()
        else:
            pass

    def click_convert(self):
        self.output_label.setText(roman_to_integer(self.line_edit.text()))
        self.output_label.adjustSize()

def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()