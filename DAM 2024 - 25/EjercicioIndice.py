import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget, QComboBox

class miventana(QMainWindow):
    def __init__(self):  # Constructor
        super().__init__()
        self.setWindowTitle("Lista Desplegable") 
        
       
        layout = QVBoxLayout()

        self.label = QLabel()
        layout.addWidget(self.label) 

        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)
        layout.addWidget(self.input)  

        # Crear un desplegable
        self.desplegable = QComboBox()
        self.desplegable.addItems(["España", "Francia", "Alemania", "Portugal", "Irlanda"])
        self.desplegable.currentIndexChanged.connect(self.mostrar_opcion)  
        self.desplegable.currentIndexChanged.connect(self.mostrar_numero) 
        layout.addWidget(self.desplegable) 

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container) 

    def mostrar_opcion(self):
        
        opcion_seleccionada = self.desplegable.currentText()
        print(f"{opcion_seleccionada}")

    def mostrar_numero(self, index):

        print(f"{index}")


app = QApplication(sys.argv)
ventana = miventana()
ventana.show()
app.exec()
