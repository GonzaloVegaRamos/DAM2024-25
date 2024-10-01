
import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget
 
class miventana (QMainWindow):
    def __init__(self): #Constructor
        super().__init__()
        self.setWindowTitle("Mi Ventana") #Nombre de la ventana

        self.label = QLabel()

        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)


        
       
        self.setCentralWidget(layout) #Cambiar la posición en el centro de la ventana
        #button.clicked.connect(self.clickado)
        
app = QApplication(sys.argv)
ventana = miventana()
ventana.show()
app.exec()
    #def clickado(self):
        #print("clickado") 
