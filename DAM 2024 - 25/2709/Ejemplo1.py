import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget,QVBoxLayout,QLabel,QLineEdit,QComboBox,QPushButton
from PyQt6.QtGui import QPalette, QColor

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)
#Ejercicio 1. Añade componentes diferentes a los widget y muestrame la pantalla
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        layout = QVBoxLayout()
        
        button = QPushButton("Soy un boton")
        layout.addWidget(button)

        self.label = QLabel()
       

        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)
        layout.addWidget(self.input)  
        layout.addWidget(self.label) 
        # Crear un desplegable
        self.desplegable = QComboBox()
        self.desplegable.addItems(["España", "Francia", "Alemania", "Portugal", "Irlanda"])

        layout.addWidget(self.desplegable) 



        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()