import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap

from io import BytesIO
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
    
)

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()






        layout = QVBoxLayout()

        # Personalización de QLabel
        label = QLabel("Hello")
        font = label.font()
        font.setPointSize(30)
        label.setFont(font)
        label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        layout.addWidget(label)



        label = QLabel(self)
        pixmap = QPixmap('C:/Users/lacer/Downloads/gato.jpg')
        label.setPixmap(pixmap)
        label.setScaledContents(True)  # Permitir que la imagen se ajuste al QLabel
        label.setFixedSize(300, 200)
        label.setContentsMargins(150,0,0,0)
        layout.addWidget(label)
        self.resize(pixmap.width(),pixmap.height())

        widget = QCheckBox()
        widget.setCheckState(Qt.CheckState.Checked)

        # For tristate: widget.setCheckState(Qt.CheckState.PartiallyChecked)
        # Or: widget.setTristate(True)
        widget.stateChanged.connect(self.show_state)

        self.setCentralWidget(widget)

        def show_state(self, s):
           print(s == Qt.CheckState.Checked.value)
        



        # Lista de otros widgets
        widgets = [
            QCheckBox,
            QComboBox,
            QDateEdit,
            QDateTimeEdit,
            QDial,
            QDoubleSpinBox,
            QFontComboBox,
            QLCDNumber,
            QLabel,
            QLineEdit,
            QProgressBar,
            QPushButton,
            QRadioButton,
            QSlider,
            QSpinBox,
            QTimeEdit,
        ]

        # Agregar los widgets de la lista al layout
        for w in widgets:
            layout.addWidget(w())

        
        label = QLabel("Adios")
        font = label.font()
        font.setPointSize(30)
        label.setFont(font)
        label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        layout.addWidget(label)
        # Crear el widget contenedor y asignar el layout
        
        
        
        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
