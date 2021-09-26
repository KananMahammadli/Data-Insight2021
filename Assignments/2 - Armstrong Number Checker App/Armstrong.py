from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QMessageBox
import sys

def num_length(num:int) -> int:
    res = 0
    while num > 0:
        res += 1
        num //= 10
    return res

def is_armstrong(num:str)->str:
    try:
        num = int(num)
        length = num_length(num)
        # creating copy so that we can check result with original number
        copy = num
        arm = 0
        arm_in_string_form = ''
        while copy > 0:
            rem = copy % 10
            arm += rem ** length
            arm_in_string_form = f'{rem}^{length} + ' + arm_in_string_form
            copy //= 10
        
        if num == 0:
            text1 = '0^0' + ' = ' + str(arm)
        else:
            text1 = arm_in_string_form[:-3] + ' = ' + str(arm)
            
        if arm == num:
            text1 += f' and {arm} = {num}.'
            text2 = f'Therefore {num} is an armstrong number.'
        else:
            text1 += f' and {arm} != {num}.'
            text2 = f'Therefore {num} is not an armstrong number!'
        
        return text1 + '\n' + text2
    
    except:
        return 'Invalid input!'

"""
This class creates a GUI that contains user input line with explained text label on the top,
followed by  a check button that uses is_armstrong function and displays input with explanatory text label,
and lastly a quit button to close the app with message box
"""
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(500, 350, 500, 350)
        self.setWindowTitle('Armstrong Number Checker')
        self.initUI()
    
    def initUI(self):
        self.input_label = QLabel(self)
        self.input_label.setText("Please, enter an integer: ")
        self.input_label.adjustSize()
        self.input_label.move(150, 10)
        
        self.line_edit = QLineEdit(self)
        self.line_edit.adjustSize()
        self.line_edit.move(175, 30)
        
        self.check_button = QPushButton('Check', self)
        self.check_button.clicked.connect(self.click_check)
        self.check_button.move(195, 60)
        
        self.output_text = QLabel('Result:', self)
        self.output_text.move(150, 90)
        
        self.output_label = QLabel(self)
        self.output_label.move(175, 118)
        
        self.quit_button = QPushButton('Quit', self)
        self.quit_button.clicked.connect(self.click_quit)
        self.quit_button.move(195, 160)
        
        self.show()

    def closeEvent(self, event):
        close_reply=QMessageBox.question(self,'Message','Are you sure you want to quit?',QMessageBox.Yes|QMessageBox.No,QMessageBox.No )
        if close_reply==QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    
    def click_quit(self):
        quit_reply=QMessageBox.question(self,'Message','Are you sure you want to quit?',QMessageBox.Yes|QMessageBox.No,QMessageBox.No )
        if quit_reply==QMessageBox.Yes:
            QApplication.instance().quit()
        else:
            pass

    def click_check(self):
        self.output_label.setText(is_armstrong(self.line_edit.text()))
        self.output_label.adjustSize()

def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
