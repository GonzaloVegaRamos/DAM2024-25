import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QStackedLayout, QHBoxLayout
from PyQt6.QtGui import QPalette, QColor

class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

#Ejercicio en el ejercio anterior de los tres botones añade una fila de abajo un stackedlayout como en el ejemplo anteior.
#  Los botónes les pones los nombres de los colores y tienes que asociar la señal de click "nombre_del_botón.pressed.connect" 
# para que cuando pulses cambies el setCurrentindex de stacklayout y que aparezca el color que quieres que salga.
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Color Switcher")

        main_layout = QVBoxLayout()
        self.stacked_layout = QStackedLayout()

        self.stacked_layout.addWidget(Color("red"))
        self.stacked_layout.addWidget(Color("green"))
        self.stacked_layout.addWidget(Color("blue"))
       

        self.stacked_layout.setCurrentIndex(3)

        widgetColor = QWidget()
        widgetColor.setLayout(self.stacked_layout)
        main_layout.addWidget(widgetColor)

        button_layout = QHBoxLayout()

        BotonRojo = QPushButton("Rojo")
        BotonVerde = QPushButton("Verde")
        BotonAzul = QPushButton("Azul")
       

        button_layout.addWidget(BotonRojo)
        button_layout.addWidget(BotonVerde)
        button_layout.addWidget(BotonAzul)
        

        BotonRojo.pressed.connect(lambda: self.stacked_layout.setCurrentIndex(0))
        BotonVerde.pressed.connect(lambda: self.stacked_layout.setCurrentIndex(1))
        BotonAzul.pressed.connect(lambda: self.stacked_layout.setCurrentIndex(2))
        

        main_layout.addLayout(button_layout)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
