import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout,QPushButton,QVBoxLayout,QHBoxLayout
from PyQt6.QtGui import QPalette, QColor

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

#Ejercicio Añade widgets a esta configuración y luego cambia la configuración con otra estructura.
#Ejercicio Crea un Vertical Layout y un Horizontal Layout Añade 3 botones QButtons en la primera línea y en la otra crea un widget de color


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")
        layoutv= QVBoxLayout()
        layouth= QHBoxLayout()
        layout = QGridLayout()


        button = QPushButton("Soy un boton")
        button1 = QPushButton("Soy un boton")
        button2 = QPushButton("Soy un boton")

        layouth.addLayout(layout)
        layouth.addLayout(layoutv)
        layout.addWidget(button,0,0)
        layout.addWidget(button1,0,1)
        layout.addWidget(button2,0,2)
        layout.addWidget(Color("green"),1,0)
        

        widget = QWidget()
        widget.setLayout(layouth)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()



