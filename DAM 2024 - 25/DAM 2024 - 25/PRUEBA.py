
import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
 
class miventana (QMainWindow):
    def __init__(self): #Constructor
        super().__init__()
        self.setWindowTitle("Mi Ventana") #Nombre de la ventana
        button = QPushButton("Dale al botón") #Generar botón
        button.setCheckable(True)
        self.setCentralWidget(button) #Cambiar la posición en el centro de la ventana
        #button.clicked.connect(self.clickado)
        button.clicked.connect(self.chequeado)

    #def clickado(self):
        #print("clickado") 

        

    def chequeado(self, checked):
            
            if(checked==True):
                self.setWindowTitle("Gonzalo")
                  
                print("chequeado")
            else:
                   self.setWindowTitle("Mi Ventana")
                   print("no chequeado")
            
           

app = QApplication(sys.argv)
ventana = miventana()
ventana.show()
app.exec()

#Importación del encolador de eventos (QApplication), ventana gráfica (QWidget) y un botón (QPushButton)
from PyQt6.QtWidgets import QApplication,QWidget, QPushButton, QMainWindow
import sys
 
 
app = QApplication(sys.argv) #Atributo app para invocar el encolador de eventos
ventana = QWidget() #Atributo ventana para la creación de ventana
main = QMainWindow() #Atributo main que genera la ventana generadora
boton = QPushButton("Botón Rojo") #Atributo boton para invocar un botón de color rojo
main.show() #Mostra ventana generadora
boton.show() #Mostrar boton
ventana.show() #Mostrar ventana
app.exec() #Ejecutar aplicación
 