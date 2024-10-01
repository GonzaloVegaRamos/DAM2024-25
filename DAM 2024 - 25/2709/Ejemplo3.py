import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget,QHBoxLayout,QVBoxLayout
from PyQt6.QtGui import QPalette, QColor

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

#Ejercicio modifica el nested layout a otra configuración con los colores ;)

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()
        
        




       
        layout2.addWidget( Color("blue"))
        layout2.addWidget(Color('red'))
        layout2.addWidget( Color("blue"))
        layout2.addWidget(Color('red'))
        layout2.addWidget(Color('blue'))
    

        layout1.addLayout( layout2 )
        layout1.addLayout( layout3 )

        layout3.addWidget(Color('red'))
        layout3.addWidget(Color('blue'))
        layout3.addWidget( Color("red"))
        layout3.addWidget(Color('blue'))
        layout3.addWidget(Color('red'))

        layout1.addLayout( layout3 )

        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()