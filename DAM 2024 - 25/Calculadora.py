import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QGridLayout, QLabel

class Calculadora(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculadora")
        self.current_value = "" 
        
        layout = QVBoxLayout()

       
        self.label = QLabel("0")
        layout.addWidget(self.label)

        
        grid = QGridLayout()

        n = 0

        
        for i in range(0, 2):
            for j in range(0, 5):
                n += 1
                button = QPushButton(str(n-1))
                button.pressed.connect(lambda num=str(n-1): self.press_button(num))
                grid.addWidget(button, i, j)

        
        operators = ["+", "-", "*", "="]

        for index, symbol in enumerate(operators):
            button = QPushButton(symbol)
            button.pressed.connect(lambda sym=symbol: self.press_button(sym))
            grid.addWidget(button, 4, index) 

        layout.addLayout(grid)
        clear_button = QPushButton("C")
        clear_button.pressed.connect(self.limpiar)
        grid.addWidget(clear_button, 5, 0, 1, 5)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

   
    def press_button(self, num):
    
     self.current_value = str(self.current_value) + str(num)
    
     self.label.setText(self.current_value)


        
    def limpiar(self):
        self.label.current_value = ""
        self.label.operator = None
        self.label.first_number = None
        self.label.setText("0")   
        self.current_value = ""



app = QApplication(sys.argv)
window = Calculadora()
window.show()

app.exec()
