import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget,QHBoxLayout,QLabel,QLineEdit,QVBoxLayout
from PyQt6.QtGui import QPalette, QColor


#Ejercicio 2. pon un Qlabel y un QLineEdit
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        layout = QVBoxLayout()

        self.label = QLabel("Hola mi nombre es: ")
        self.label1 = QLabel()

        self.input = QLineEdit()
        self.input.textChanged.connect(self.label1.setText)
        layout.addWidget(self.input)  
        layout.addWidget(self.label) 
        layout.addWidget(self.label1) 



        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        
app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()