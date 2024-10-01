import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QGridLayout, QLabel

class Calculadora(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculadora")
        self.current_value = ""  # Almacena el valor actual que se muestra en la calculadora
        self.first_number = None  # Almacena el primer número ingresado
        self.operator = None  # Almacena la operación seleccionada

        layout = QVBoxLayout()

        # Label para mostrar el valor actual
        self.label = QLabel("0")
        layout.addWidget(self.label)

        # Crear un layout de cuadrícula para los botones
        grid = QGridLayout()

        n = 0

        # Crear los botones numéricos
        for i in range(0, 2):
            for j in range(0, 5):
                n += 1
                button = QPushButton(str(n-1))
                button.pressed.connect(lambda num=str(n-1): self.press_button(num))
                grid.addWidget(button, i, j)

        # Crear botones de operadores (+, -, *, /, =)
        operators = ["+", "-", "*", "/", "="]

        for index, symbol in enumerate(operators):
            button = QPushButton(symbol)
            button.pressed.connect(lambda sym=symbol: self.handle_operator(sym))
            grid.addWidget(button, 4, index)

        # Botón para limpiar la calculadora
        clear_button = QPushButton("C")
        clear_button.pressed.connect(self.limpiar)
        grid.addWidget(clear_button, 5, 0, 1, 5)

        layout.addLayout(grid)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    # Método que se ejecuta al presionar un número
    def press_button(self, num):
        self.current_value = str(self.current_value) + str(num)
        self.label.setText(self.current_value)

    # Método que se ejecuta al presionar un operador
    def handle_operator(self, operator):
        if operator == "=":
            # Si se presiona "=", realizar la operación
            if self.first_number is not None and self.operator is not None:
                second_number = float(self.current_value)
                result = self.calculate(self.first_number, second_number, self.operator)
                self.label.setText(str(result))
                self.current_value = str(result)
                self.first_number = None
                self.operator = None
        else:
            # Almacenar el primer número y el operador seleccionado
            if self.current_value != "":
                self.first_number = float(self.current_value)
                self.operator = operator
                self.current_value = ""  # Limpiar el valor actual para el siguiente número

    # Método para realizar las operaciones
    def calculate(self, first, second, operator):
        if operator == "+":
            return first + second
        elif operator == "-":
            return first - second
        elif operator == "*":
            return first * second
        elif operator == "/":
            if second != 0:
                return first / second
            else:
                return "Error"

    # Método para limpiar la calculadora
    def limpiar(self):
        self.current_value = ""
        self.operator = None
        self.first_number = None
        self.label.setText("0")

# Código para ejecutar la aplicación
app = QApplication(sys.argv)
window = Calculadora()
window.show()

app.exec()
