# =================== Importaciones =============================
from PyQt5.QtGui import QIcon, QPalette, QColor, QPixmap, QFont
from PyQt5.QtWidgets import (QApplication, QMainWindow, QFrame, QLabel, QComboBox, QLineEdit,
                             QPushButton,QHeaderView,QRadioButton,QButtonGroup,QVBoxLayout,QCheckBox,QDialog, QMessageBox,QTableWidget,
                             QTableWidgetItem)
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5 import QtCore
import mysql.connector
from io import open
import pandas as pd

# ==== Lista de Almacen ====
Alumnos = list()
def conexionbase():
    try:
        mycursor = conexion.cursor()
        mycursor.execute("USE Estudiantes")
        print("Conexión a la Base de Datos exitosa")   
    except:
        mycursor = conexion.cursor()
        print("Error102. Error no existe la Base de Datos")
        mycursor.execute("CREATE DATABASE Estudiantes")
        conexionbase()
        
def reg_tabla():
    try:
        mycursor = conexion.cursor()
        mycursor.execute("USE Estudiantes")
        mycursor.execute("CREATE TABLE alumnos (id INT AUTO_INCREMENT PRIMARY KEY, Nombre VARCHAR(255), ApellidoPaterno VARCHAR(255), ApellidoMaterno VARCHAR(255), Matricula INT, Edad INT, Calle VARCHAR(255), Carrera VARCHAR(255), Estado VARCHAR(255), Municipio VARCHAR(255), Beca VARCHAR(255), Materias VARCHAR(255))")
        print("Tabla creada exitosamente")
    except:
        print("Error103. Error Tabla existente")
        print("Tabla usada existosamente")

try:
    conexion = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "557855") #ESTO SE CAMBIA A SU CONTRASEÑA
    print("Conexión a SQL exitosa")
    conexionbase()
    reg_tabla() 
    print("ok")
except:
    print("Error101. Error al conectar con MySQL")
    print("Verificar contraseña del MySQL")
        
    # ========================== Ventana para Consulta Matricula ===============================  
class Dialogo2(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        # ========= Diseño para la ventana de Tabla ==================
        print("Diseño de ventana")
        self.setFixedSize(500, 500)
        self.setWindowTitle("Consultar Alumno")
        self.setWindowIcon(QIcon("iconofacp.png"))
        self.paleta = QPalette()
        self.paleta.setColor(QPalette.Background, QColor('Gray'))
        self.frame = QFrame(self)
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.frame.setAutoFillBackground(True)
        self.frame.setPalette(self.paleta)
        self.frame.setFixedWidth(800)
        self.frame.setFixedHeight(50)
        self.fuenteTitulo = QFont()
        self.fuenteTitulo.setPointSize(20)
        self.fuenteTitulo.setBold(True)
        self.labelTitulo = QLabel("<font color='white'>   Consulta por matrícula  </font>", self.frame)
        self.labelTitulo.setFont(self.fuenteTitulo)
        self.labelTitulo.move(94, 10)
        
        self.labelMatricula2 = QLabel("Matricula", self)
        self.labelMatricula2.move(60, 80)
        
        self.frameMatricula2 = QFrame(self)
        self.frameMatricula2.setFrameShape(QFrame.StyledPanel)
        self.frameMatricula2.setFixedWidth(280)
        self.frameMatricula2.setFixedHeight(28)
        self.frameMatricula2.move(60, 106)
        
        self.lineEditMatricula2 = QLineEdit(self.frameMatricula2)
        self.lineEditMatricula2.setFrame(False)
        self.lineEditMatricula2.setTextMargins(8, 0, 4, 1)
        self.lineEditMatricula2.setFixedWidth(238)
        self.lineEditMatricula2.setFixedHeight(26)
        self.lineEditMatricula2.move(40, 1)  

        print("Tabla widget")
        self.tabla2 = QTableWidget(self)
        self.tabla2.resize(460,230)
        self.tabla2.move(20,170)
        
        self.tabla2.setRowCount(11)  
        self.tabla2.setColumnCount(2)
        
        header = self.tabla2.horizontalHeader()  
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        
        self.tabla2.setItem(0, 0, QTableWidgetItem("Matricula:"))
        self.tabla2.setItem(1, 0, QTableWidgetItem("Nombre:"))
        self.tabla2.setItem(2, 0, QTableWidgetItem("Apellido P:"))
        self.tabla2.setItem(3, 0, QTableWidgetItem("Apellido M:"))
        self.tabla2.setItem(4, 0, QTableWidgetItem("Edad:"))
        self.tabla2.setItem(5, 0, QTableWidgetItem("Calle:"))
        self.tabla2.setItem(6, 0, QTableWidgetItem("Carrera:"))
        self.tabla2.setItem(7, 0, QTableWidgetItem("Estado:"))
        self.tabla2.setItem(8, 0, QTableWidgetItem("Municipio:"))
        self.tabla2.setItem(9, 0, QTableWidgetItem("Beca:"))
        self.tabla2.setItem(10, 0, QTableWidgetItem("Materias:"))
        # ======================== BOTONES PARA LA CONSULTA =========================
        self.botonConsultar = QPushButton("Consultar", self)
        self.botonConsultar.setFixedWidth(100)
        self.botonConsultar.setFixedHeight(60)
        self.botonConsultar.move(200, 430)
        # ======================== EVENTOS PARA BOTONES DE LA CONSULTA =========================
        self.botonConsultar.clicked.connect(self.consultar_)
    # ======================= FUNCIONES PARA LA CONSULTA ============================
    # ==================== CONSULTAR =========================
    def consultar_(self):
        print("matricula")
        Consulta = str(self.lineEditMatricula2.text())
        print(type(Consulta))
        if Consulta == "":
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Information)
            msg.setText("Nada ingresado")
            msg.setInformativeText("Introduzca una matricula de alumno")
            msg.setWindowTitle("Error 107")
            msg.show()
        elif Consulta.isalpha():
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Information)
            msg.setText("Error108. Error valor alphanumerico")
            msg.setInformativeText("Introduzca una matricula de alumno")
            msg.setWindowTitle("Error 108")
            msg.show()
            
        else:
            Consulta = int(Consulta)
            mycursor = conexion.cursor()
            mycursor.execute("USE Estudiantes")
            sql = "SELECT * FROM alumnos WHERE Matricula = %s"
            adr = (Consulta, )
            mycursor.execute(sql, adr)
            resultado = mycursor.fetchall()
            print(resultado)
            print(type(resultado))
            a = len(resultado)
            if a == 0:
                msg = QMessageBox(self)
                msg.setIcon(QMessageBox.Information)
                msg.setText(str(Consulta))
                msg.setInformativeText("NO existente")
                msg.setWindowTitle("Error 106")
                msg.show()
            
            
            for e in resultado:
                self.tabla2.setItem(0, 1, QTableWidgetItem(str(e[4])))#Matricula
                self.tabla2.setItem(1, 1, QTableWidgetItem(e[1]))#Nombre
                self.tabla2.setItem(2, 1, QTableWidgetItem(e[2]))#Apellido Paterno
                self.tabla2.setItem(3, 1, QTableWidgetItem(e[3]))#Apellido Materno
                self.tabla2.setItem(4, 1, QTableWidgetItem(str(e[5])))#Edad
                self.tabla2.setItem(5, 1, QTableWidgetItem(e[6]))#Calle
                self.tabla2.setItem(6, 1, QTableWidgetItem(e[7]))#Carrera
                self.tabla2.setItem(7, 1, QTableWidgetItem(e[8]))#Estado
                self.tabla2.setItem(8, 1, QTableWidgetItem(e[9]))#Municipio
                self.tabla2.setItem(9, 1, QTableWidgetItem(e[10]))#Beca
                if e[10] == "100%":
                    print(e[1])
                    print("Tiene la beca del 100%")
                    self.tabla2.item(9, 1).setBackground(QtGui.QColor('lightGreen'))
                
                self.tabla2.setItem(10, 1, QTableWidgetItem(e[11]))#Materias
# ========================== Ventana para Tabla ===============================  
class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        # ========= Diseño para la ventana de Tabla ==================
        self.setFixedSize(1122, 500)
        self.setWindowTitle("TABLA REGISTRO")
        self.setWindowIcon(QIcon("iconofacp.png"))
        
        self.paleta = QPalette()
        self.paleta.setColor(QPalette.Background, QColor('Gray'))
        self.frame = QFrame(self)
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.frame.setAutoFillBackground(True)
        self.frame.setPalette(self.paleta)
        self.frame.setFixedWidth(510)
        self.frame.setFixedHeight(90)
        self.frame.move(600, 410)
        self.labelIcono = QLabel(self.frame)
        self.labelIcono.setFixedWidth(70)
        self.labelIcono.setFixedHeight(70)
        self.labelIcono.setPixmap(QPixmap("registro.png").scaled(80, 80, Qt.KeepAspectRatio,
                                                             Qt.SmoothTransformation))
        self.labelIcono.move(15, 8)
        self.fuenteTitulo = QFont()
        self.fuenteTitulo.setPointSize(25)
        self.fuenteTitulo.setBold(True)
        self.labelTitulo = QLabel("<font color='white'>Registro de Alumnos</font>", self.frame)
        self.labelTitulo.setFont(self.fuenteTitulo)
        self.labelTitulo.move(110, 18)
        
        # ======== TABLA DE DATOS ========
        self.tabla = QTableWidget(self)
        self.tabla.resize(1100,400)
        self.tabla.move(10,10)
        self.tabla.setRowCount(12)  
        self.tabla.setColumnCount(11) 
        self.tabla.horizontalHeader().setStretchLastSection(7)
        self.tabla.horizontalHeader().setSectionResizeMode(7) 

        nombreColumnas = ("Nombre","Apellido P.", "Apellido M.","Matricula","Edad", "Calle",
                          "Carrera","Estado","Municipio","Beca","Materia(s)")
        self.tabla.setHorizontalHeaderLabels(nombreColumnas)
        
        # ========= INSERTAR DATOS A LA TABLA =======
        row = 0
        mycursor = conexion.cursor()
        mycursor.execute("USE Estudiantes")
        mycursor.execute("SELECT * FROM alumnos")
        resultado = mycursor.fetchall()
        
        for e in resultado:
            self.tabla.setRowCount(row + 1)
            self.tabla.setItem(row, 0, QTableWidgetItem(e[1]))
            self.tabla.setItem(row, 1, QTableWidgetItem(e[2]))
            self.tabla.setItem(row, 2, QTableWidgetItem(e[3]))
            self.tabla.setItem(row, 3, QTableWidgetItem(str(e[4])))
            self.tabla.setItem(row, 4, QTableWidgetItem(str(e[5])))
            self.tabla.setItem(row, 5, QTableWidgetItem(e[6]))
            self.tabla.setItem(row, 6, QTableWidgetItem(e[7]))
            self.tabla.setItem(row, 7, QTableWidgetItem(e[8]))
            self.tabla.setItem(row, 8, QTableWidgetItem(e[9]))
            self.tabla.setItem(row, 9, QTableWidgetItem(e[10]))
            if e[10] == "100%":
                print(e[1])
                print("Tiene la beca del 100%")
                self.tabla.item(row, 9).setBackground(QtGui.QColor('lightGreen'))
                
            self.tabla.setItem(row, 10, QTableWidgetItem(e[11]))
            row += 1 
        self.tabla.setAlternatingRowColors(True)
            
        # =================== BOTONES VENTANA TABLA ==================
        self.botonEliminarFila = QPushButton("Eliminar fila",self)
        self.botonEliminarFila.setFixedWidth(100)
        self.botonEliminarFila.move(250, 435)

        self.botonCerrar = QPushButton("Volver", self)
        self.botonCerrar.setFixedWidth(100)
        self.botonCerrar.move(100, 435)
        
        botonLimpiar = QPushButton("Limpiar", self)
        botonLimpiar.setFixedWidth(100)
        botonLimpiar.move(400, 435)
            
        # ======================== EVENTOS PARA BOTONES DE TABLA =========================
        self.botonEliminarFila.clicked.connect(self.eliminarFila)
        self.botonCerrar.clicked.connect(self.close)
        botonLimpiar.clicked.connect(self.limpiarTabla)

    # ======================= FUNCIONES PARA TABLA ============================
    # ==================== Eliminar una fila =========================

    def eliminarFila(self):
        print("Eliminar Fila")
        filaSeleccionada = self.tabla.selectedItems()
        if filaSeleccionada:
            fila = filaSeleccionada[0].row()
            lafila = fila + 1
            lefile = lafila + 1
            print(lafila)
        
            mycursor = conexion.cursor()
            #mycursor.execute("USE Estudiantes")
            sql = ("DELETE FROM alumnos WHERE id = %s")
            valor = (lafila,)
            
            mycursor.execute(sql,valor)
            print(mycursor.rowcount, "record(s) deleted")
            mycursor.execute("SELECT * FROM alumnos")
            resultado = mycursor.fetchall()
            print(resultado)       
            
            conexion.commit()
            self.tabla.removeRow(fila)
            self.tabla.clearSelection()
        else:
            QMessageBox.critical(self, "Eliminar fila", "Seleccione una fila.   ",
                                 QMessageBox.Ok)
            
    # ================= Limpiar toda la tabla ==========================  
    def limpiarTabla(self):
        # ========= Mensaje de advertencia =============
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)
        msg.setText("Atención.")
        msg.setInformativeText("Se borrara toda la información permanentemente.")
        msg.setWindowTitle("¡ADVERTENCIA!")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msg.exec()
        # ===== Empieza a borrar =====
        if returnValue == QMessageBox.Ok:
            self.tabla.clearContents()
            self.tabla.setRowCount(0)
            del Alumnos[:]
            try:
                mycursor = conexion.cursor()
                mycursor.execute("USE Estudiantes")
                mycursor.execute("TRUNCATE TABLE alumnos")
                print("Tabla vaciada")
            except:
                print("Error105. Error al vaciar tabla")

# ======================== Ventana Principal =============================  
class Dialogo3(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle("REGISTRO ALUMNOS")
        self.setWindowIcon(QIcon("iconofacp.png"))
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)
        self.setFixedSize(750, 580)
        paleta = QPalette()
        paleta.setColor(QPalette.Background, QColor(243, 243, 243))
        self.setPalette(paleta)
        self.initUI()
        
        self.labelIcono = QLabel(self)
        self.labelIcono.setFixedWidth(80)
        self.labelIcono.setFixedHeight(80)
        self.labelIcono.setPixmap(QPixmap("nuevo.png").scaled(80, 80, Qt.KeepAspectRatio,
                                                             Qt.SmoothTransformation))
        self.labelIcono.move(90, 410)
        
        self.labelIcono2 = QLabel(self)
        self.labelIcono2.setFixedWidth(90)
        self.labelIcono2.setFixedHeight(90)
        self.labelIcono2.setPixmap(QPixmap("mostrar.png").scaled(90, 90, Qt.KeepAspectRatio,
                                                             Qt.SmoothTransformation))
        self.labelIcono2.move(245, 408)
    # ================================================================  
    def initUI(self):
      # ==================== FRAME ENCABEZADO ====================
      # ============ Más Diseño para la Ventana Principal ============
        paleta = QPalette()
        paleta.setColor(QPalette.Background, QColor('Gray'))
        frame = QFrame(self)
        frame.setFrameShape(QFrame.NoFrame)
        frame.setFrameShadow(QFrame.Sunken)
        frame.setAutoFillBackground(True)
        frame.setPalette(paleta)
        frame.setFixedWidth(800)
        frame.setFixedHeight(84)
        frame.move(0, 0)
        
        labelIcono = QLabel(frame)
        labelIcono.setFixedWidth(70)
        labelIcono.setFixedHeight(70)
        labelIcono.setPixmap(QPixmap("iconofacp.png").scaled(70, 70, Qt.KeepAspectRatio,
                                                             Qt.SmoothTransformation))
        labelIcono.move(20, 8)
        fuenteTitulo = QFont()
        fuenteTitulo.setPointSize(25)
        fuenteTitulo.setBold(True)
        labelTitulo = QLabel("<font color='white'>Equipo 2</font>", frame)
        labelTitulo.setFont(fuenteTitulo)
        labelTitulo.move(100, 15)
        fuenteSubtitulo = QFont()
        fuenteSubtitulo.setPointSize(20)
        labelSubtitulo = QLabel("<font color='white'>Captura de Información de Alumnos", frame)
        labelSubtitulo.setFont(fuenteSubtitulo)
        labelSubtitulo.move(100, 46)

      # ========== Widgets de la Ventana Principal =============
        # ======== QLineEdit Nombre =========
        labelNombre = QLabel("Nombre", self)
        labelNombre.move(60, 110)
        frameNombre = QFrame(self)
        frameNombre.setFrameShape(QFrame.StyledPanel)
        frameNombre.setFixedWidth(280)
        frameNombre.setFixedHeight(28)
        frameNombre.move(60, 136)
        self.lineEditNombre = QLineEdit(frameNombre)
        self.lineEditNombre.setFrame(False)
        self.lineEditNombre.setTextMargins(8, 0, 4, 1)
        self.lineEditNombre.setFixedWidth(238)
        self.lineEditNombre.setFixedHeight(26)
        self.lineEditNombre.move(40, 1)

        # ======== QLineEdit Apellido Paterno =========
        labelApellido_Paterno = QLabel("Apellido", self)
        labelApellido_Paterno.move(60, 170)
        labelApellido_Paterno = QLabel(" Paterno", self)
        labelApellido_Paterno.move(115, 170)
        frameApellido_Paterno = QFrame(self)
        frameApellido_Paterno.setFrameShape(QFrame.StyledPanel)
        frameApellido_Paterno.setFixedWidth(280)
        frameApellido_Paterno.setFixedHeight(28)
        frameApellido_Paterno.move(60, 196)
        self.lineEditApellido_Paterno = QLineEdit(frameApellido_Paterno)
        self.lineEditApellido_Paterno.setFrame(False)
        self.lineEditApellido_Paterno.setTextMargins(8, 0, 4, 1)
        self.lineEditApellido_Paterno.setFixedWidth(238)
        self.lineEditApellido_Paterno.setFixedHeight(26)
        self.lineEditApellido_Paterno.move(40, 1)
        
        # ======== QLineEdit Apellido Materno =========
        labelApellido_Materno = QLabel("Apellido", self)
        labelApellido_Materno.move(60, 224)
        labelApellido_Materno = QLabel(" Materno", self)
        labelApellido_Materno.move(115, 224)
        frameApellido_Materno = QFrame(self)
        frameApellido_Materno.setFrameShape(QFrame.StyledPanel)
        frameApellido_Materno.setFixedWidth(280)
        frameApellido_Materno.setFixedHeight(28)
        frameApellido_Materno.move(60, 250)
        self.lineEditApellido_Materno = QLineEdit(frameApellido_Materno)
        self.lineEditApellido_Materno.setFrame(False)
        self.lineEditApellido_Materno.setTextMargins(8, 0, 4, 1)
        self.lineEditApellido_Materno.setFixedWidth(238)
        self.lineEditApellido_Materno.setFixedHeight(26)
        self.lineEditApellido_Materno.move(40, 1)
        
        # ======== QLineEdit Matrícula =========
        labelMatricula = QLabel("Matrícula", self)
        labelMatricula.move(60, 280)
        frameMatricula = QFrame(self)
        frameMatricula.setFrameShape(QFrame.StyledPanel)
        frameMatricula.setFixedWidth(280)
        frameMatricula.setFixedHeight(28)
        frameMatricula.move(60, 305)
        self.lineEditMatricula = QLineEdit(frameMatricula)
        self.lineEditMatricula.setFrame(False)
        self.lineEditMatricula.setTextMargins(8, 0, 4, 1)
        self.lineEditMatricula.setFixedWidth(238)
        self.lineEditMatricula.setFixedHeight(26)
        self.lineEditMatricula.move(40, 1)
        
        # ======== QLineEdit Edad =========
        labelEdad = QLabel("Edad", self)
        labelEdad.move(60, 340)
        frameEdad = QFrame(self)
        frameEdad.setFrameShape(QFrame.StyledPanel)
        frameEdad.setFixedWidth(280)
        frameEdad.setFixedHeight(28)
        frameEdad.move(60, 365)
        self.lineEditEdad = QLineEdit(frameEdad)
        self.lineEditEdad.setFrame(False)
        self.lineEditEdad.setTextMargins(8, 0, 4, 1)
        self.lineEditEdad.setFixedWidth(238)
        self.lineEditEdad.setFixedHeight(26)
        self.lineEditEdad.move(40, 1)
        
        # ======== QLineEdit Calle =========
        labelCalle = QLabel("Calle", self)
        labelCalle.move(400, 110)
        frameCalle = QFrame(self)
        frameCalle.setFrameShape(QFrame.StyledPanel)
        frameCalle.setFixedWidth(142)
        frameCalle.setFixedHeight(28)
        frameCalle.move(400, 136)
        self.lineEditCalle = QLineEdit(frameCalle)
        self.lineEditCalle.setFrame(False)
        self.lineEditCalle.setTextMargins(8, 0, 4, 1)
        self.lineEditCalle.setFixedWidth(100)
        self.lineEditCalle.setFixedHeight(26)
        self.lineEditCalle.move(40, 1)
        
        # ======== QLineEdit Numero Calle =========
        labelNumero_Calle = QLabel("Número", self)
        labelNumero_Calle.move(550, 110)
        frameNumero_Calle = QFrame(self)
        frameNumero_Calle.setFrameShape(QFrame.StyledPanel)
        frameNumero_Calle.setFixedWidth(143)
        frameNumero_Calle.setFixedHeight(28)
        frameNumero_Calle.move(550, 136)
        self.lineEditNumero_Calle = QLineEdit(frameNumero_Calle)
        self.lineEditNumero_Calle.setFrame(False)
        self.lineEditNumero_Calle.setTextMargins(8, 0, 4, 1)
        self.lineEditNumero_Calle.setFixedWidth(100)
        self.lineEditNumero_Calle.setFixedHeight(26)
        self.lineEditNumero_Calle.move(40, 1)
        
        # ==================== QComboBox Estado ===========================
        labelMunicipio = QLabel("Estado", self)
        labelMunicipio.move(400, 170)
        
        self.comboBoxEstado= QComboBox(self)
        self.comboBoxEstado.addItems(["Nuevo León"])
        self.comboBoxEstado.setCurrentIndex(-1)
        self.comboBoxEstado.setFixedWidth(280)
        self.comboBoxEstado.setFixedHeight(26)
        self.comboBoxEstado.move(400, 195)
        
         # ==================== QComboBox Municipio ===========================
        labelCarrera = QLabel("Carrera", self)
        labelCarrera.move(400, 227)

        self.comboBoxCarrera = QComboBox(self)
        self.comboBoxCarrera.addItems(["Licenciado en Tecnologías de la Información",
                                       "Contador Público y Auditor","Licenciado en Administración de Empresas",
                                       "Licenciado en Negocios Internacionales"])
        self.comboBoxCarrera.setCurrentIndex(-1)
        self.comboBoxCarrera.setFixedWidth(280)
        self.comboBoxCarrera.setFixedHeight(26)
        self.comboBoxCarrera.move(400, 250)
        
        # ==================== QComboBox Municipio ===========================
        labelMunicipio = QLabel("Municipio", self)
        labelMunicipio.move(400, 280)

        self.comboBoxMunicipio = QComboBox(self)
        self.comboBoxMunicipio.addItems(["Abasolo", "Agualeguas", "Allende Anáhuac","Apodaca", "Aramberri", "Bustamante",
                                         "Cadereyta", "Jiménez", "Cerralvo", "Ciénega de Flores","China Doctor", "Arroyo",
                                         "Doctor Coss", "Doctor González", "El Carmen", "Galeana","García", "General Bravo",
                                         "General Escobedo", "General Terán","General Treviño","General Zaragoza","General Zuazua",
                                         "Guadalupe", "Hidalgo", "Higueras", "Hualahuises", "Iturbide","Juárez","Lampazos de Naranjo", "Linares",
                                         "Los Aldamas Los Herreras","Los Ramones", "Marín", "Melchor Ocampo", "Mier y Noriega","Mina",
                                         "Montemorelos","Monterrey","Parás","Pesquería","Rayones","Sabinas","Hidalgo","Salinas Victoria",
                                         "San Nicolás de los Garza","San Pedro Garza García","Santa Catarina","Santiago","Vallecillo","Villaldama"])
        self.comboBoxMunicipio.setCurrentIndex(-1)
        self.comboBoxMunicipio.setFixedWidth(280)
        self.comboBoxMunicipio.setFixedHeight(26)
        self.comboBoxMunicipio.move(400, 305)
        
        # ================== QRadioButton Porcentaje Beca ===================
        labelBeca = QLabel("Porcentaje",self)
        labelBeca.move(400,340)
        labelBeca = QLabel(" Beca",self)
        labelBeca.move(470,340)
        self.cerobtn = QRadioButton('0%',self)
        self.cerobtn.move(400,360)
        self.veinticincobtn = QRadioButton('25%',self)
        self.veinticincobtn.move(470,360)
        self.cincuentabtn = QRadioButton('50%',self)
        self.cincuentabtn.move(540,360)
        self.cienbtn = QRadioButton('100%',self)
        self.cienbtn.move(610,360)
        
        # ==================== QCheckBox Materias Favoritas =====================
        labelMaterias = QLabel("Materia(s)",self)
        labelMaterias.move(400,395)
        labelMaterias = QLabel("Favorita(s)" ,self)
        labelMaterias.move(480,395)
        
     
        # ============= Lista con el orden de los QLineEdit ====================
        self.les = [self.lineEditNombre,self.lineEditApellido_Paterno,self.lineEditApellido_Materno,self.lineEditMatricula,
                    self.lineEditEdad, self.lineEditCalle, self.lineEditNumero_Calle]
        
        # ===================== BOTONES VENTANA PRINCIPAL =========================
        buttonGuardar = QPushButton("Grabar", self)
        buttonGuardar.setFixedWidth(135)
        buttonGuardar.setFixedHeight(28)
        buttonGuardar.move(60, 500)

        buttonMostrar = QPushButton("Mostrar", self)
        buttonMostrar.setFixedWidth(135)
        buttonMostrar.setFixedHeight(28)
        buttonMostrar.move(220, 500)
        
        buttonImprimir = QPushButton("Imprimir", self)
        buttonImprimir.setFixedWidth(135)
        buttonImprimir.setFixedHeight(28)
        buttonImprimir.move(380, 500)
        
        buttonConsultar = QPushButton("Consultar", self)
        buttonConsultar.setFixedWidth(145)
        buttonConsultar.setFixedHeight(48)
        buttonConsultar.move(580, 18)
        
        buttonLimpiar = QPushButton("Limpiar", self)
        buttonLimpiar.setFixedWidth(135)
        buttonLimpiar.setFixedHeight(28)
        buttonLimpiar.move(540, 500)
        
        # ==================== SEÑAL BOTONES VENTANA PRINCIPAL =====================
        buttonGuardar.clicked.connect(self.Guardar_)
        buttonMostrar.clicked.connect(self.Mostrar_)
        buttonImprimir.clicked.connect(self.Imprimir_)
        buttonLimpiar.clicked.connect(self.Limpiar_)
        buttonConsultar.clicked.connect(self.Consultar_)
        
    # ======================= FUNCIONES VENTANA PRINCIPAL ============================
    # ================= Abre la ventana de la TABLA ============================
    def abrirDialogo(self):
        self.dialogo.exec_()
    # ================= Abre la ventana de la TABLA ============================
    def abrirDialogo2(self):
        self.dialogo2.exec_()
        
    # ================ Con la tecla Enter pasa a otro QLineEdit =================
    def keyPressEvent(self, event):
        if event.key()==Qt.Key_Return:
            wfocus = QApplication.focusWidget() 
            if wfocus in self.les: 
                ix = self.les.index(wfocus) 
                if ix != len(self.les)-1:
                    self.les[ix+1].setFocus()

    # ================= Pasar los Datos validados a un archivo ===================        
    def Mostrar_(self):
        mycursor = conexion.cursor()
        mycursor.execute("USE Estudiantes")
        mycursor.execute("SELECT * FROM alumnos")
        resultado = mycursor.fetchall()
        print("Alumnos Creados",len(resultado))
        
        a = len(resultado)
        if a > 0:
            self.dialogo = Dialogo()
            self.abrirDialogo()
        else:
            print("vacio")
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Information)
            msg.setText("No existen alumnos")
            msg.setInformativeText("¡Ups no hay nada que mostrar!")
            msg.setWindowTitle("Error 104")
            msg.show()
        
    def Imprimir_(self):
        print("Imprimiendo")
        import itertools
        from arrow import utcnow, get
        #Librerias a ocupar para el pdf
        from reportlab.lib.pagesizes import A4
        from reportlab.pdfgen import canvas
        
        def grouper(iterable, n):
            args = [iter(iterable)] * n
            return itertools.zip_longest(*args)
        
        def export_to_pdf(data): # Funcion para generar el pdf
            c = canvas.Canvas("Alumnos Reporte.pdf", pagesize=A4)
            w, h = A4
            max_rows_per_page = 30
            # Margen
            x_offset = 20
            y_offset = 120
            # Space between rows.
            padding = 15
            xlist = [x + x_offset for x in [0, 70, 155, 255, 332, 410,448,485,570]]
            ylist = [h - y_offset - i*padding for i in range(max_rows_per_page + 1)]
            a = 0
            for rows in grouper(data, max_rows_per_page):
                rows = tuple(filter(bool, rows))
                c.grid(xlist, ylist[:len(rows) + 1])
                for y, row in zip(ylist[:-1], rows):
                    for x, cell in zip(xlist, row):
                        c.drawString(x + 2, y - padding + 3, str(cell))
                c.drawCentredString(300, 750,"REPORTE DE ALUMNOS")
        
                #FECHA#
                fecha = utcnow().to("local").format("dddd, DD - MMMM - YYYY", locale="es")
                fechaReporte = fecha.replace("-", "de")
                c.drawString(380,790,fechaReporte)
      
                a = a + 1
                pagina = "Pagina " + str(a)
                c.drawString(40,40,str(pagina))
                
                image = 're.jpg'
                c.drawInlineImage(image, 500,20)
                c.showPage()
            c.save()
            print("Impreso correctamente")
            print("vacio")
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Information)
            msg.setText("REPORTE ALUMNOS")
            msg.setInformativeText("ARCHIVO PDF CREADO")
            msg.setWindowTitle("ÉXITO!")
            msg.show()
            import webbrowser as wb
            wb.open_new(r'C:\Users\juanp\Desktop\Clases python\Alumnos Aplicación\Alumnos Reporte.pdf')
    
        ##Columnas
        data = [("CARRERA","MATRICULA","NOMBRE","APELLIDO P.","APELLIDO M.","EDAD","BECA","ESTADO")]

        ##llenado
        try:
            import mysql.connector
            mycursor = conexion.cursor()
            mycursor.execute("USE Estudiantes")
        except:
            print("Error al conectar")

        mycursor = conexion.cursor()
        mycursor.execute("SELECT Carrera,Matricula,Nombre,ApellidoPaterno,ApellidoMaterno,Edad,Beca,Estado From alumnos ORDER BY Carrera")
        resultado = mycursor.fetchall()
        print(resultado)
        print(type(resultado))

        for e in resultado:
            data.append(e)
        export_to_pdf(data)
        
    def Consultar_(self):
        print("Consultando")
        self.dialogo2 = Dialogo2()
        self.abrirDialogo2()

    # =========== Se Guarda la información para la TABLA ============
    def Guardar_(self):
        # ==== Obtenemos los valores ingresados ====
        Nombre = self.lineEditNombre.text()
        Apellido_Paterno = self.lineEditApellido_Paterno.text()
        Apellido_Materno = self.lineEditApellido_Materno.text()
        Matricula = self.lineEditMatricula.text()
        Edad = self.lineEditEdad.text()
        Calle = self.lineEditCalle.text()
        Numero_Calle = self.lineEditNumero_Calle.text()
        Estado = self.comboBoxEstado.currentText()
        Municipio = self.comboBoxMunicipio.currentText()
        Carrera = self.comboBoxCarrera.currentText()
        # == Metodo para guardar las casillas checadas ==
        Materias = list()
        if self.Programacionbox.isChecked()==True:
                Programacion = "Programacion"
                Materias.append(Programacion)
        if self.Contabilidadbox.isChecked()==True:
                Contabilidad = "Contabilidad"
                Materias.append(Contabilidad)
        if self.Estadísticabox.isChecked()==True:
                Estadística = "Estadística"
                Materias.append(Estadística)
        if self.Basebox.isChecked()==True:
                Base = "Base de Datos"
                Materias.append(Base)      
        if self.Investigaciónbox.isChecked()==True:
                Investigación = "Investigación"
                Materias.append(Investigación)
        # == Metodo para guardar el radio seleccionado ==
        Porcentaje = list()
        if self.cerobtn.isChecked():
            cero = self.cerobtn.text()
            Porcentaje.append(cero)
        if self.veinticincobtn.isChecked():
            veinticinco = self.veinticincobtn.text()
            Porcentaje.append(veinticinco)
        if self.cincuentabtn.isChecked():
            cincuenta = self.cincuentabtn.text()
            Porcentaje.append(cincuenta)
        if self.cienbtn.isChecked():
            cien = self.cienbtn.text()
            Porcentaje.append(cien)
       
        # === Impresion en consola de los datos y los adjuntamos ==
        Alumno = list()
        Alumno.append(Nombre)
        Alumno.append(Apellido_Paterno)
        Alumno.append(Apellido_Materno)
        Alumno.append(Matricula)
        Alumno.append(Edad)
        Alumno.append(Calle)
        Alumno.append(Numero_Calle)
    
        if Carrera == "Licenciado en Tecnologías de la Información":
            Carrera = "LTI"
        elif Carrera == "Licenciado en Administración de Empresas":
            Carrera = "LA"
        elif Carrera == "Contador Público y Auditor":
            Carrera = "CP"
        elif Carrera == "Licenciado en Negocios Internacionales":
            Carrera = "LNI"
            
        Alumno.append(Carrera)
        Alumno.append(Estado)
        Alumno.append(Municipio)
        Porcentajes = str(Porcentaje)
        Materiadas = str(Materias)
        x = Porcentajes.replace("'", "")
        y = x.replace("[", "")
        Porcentajereal = y.replace("]", "")
        print(Porcentajereal)
        a = Materiadas.replace("'", "")
        b = a.replace("[", "")
        Materiadasreales = b.replace("]", "")
        Alumno.append(Porcentajereal)
        Alumno.append(Materiadasreales)
        c = " "
        d = " "
        Calle_Completa = Calle + c + Numero_Calle
        print(Calle_Completa)
 
            
        # == Validacion graba los datos completos ==
        lleno = True

        for datos in Alumno:
            if datos == "":
                lleno = False
            elif datos == "[]":
                lleno = False
        #Si no esta lleno elimina lo registrado
        if lleno == False:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Information)
            msg.setText("Faltan datos")
            msg.setInformativeText("Favor de llenar el Registro")
            msg.setWindowTitle("¡ADVERTENCIA!")
            msg.show()
            del Porcentajes
            del Materiadas
            del Alumno
        
        else:
            lista_validacion_numerica = [Matricula,Edad,Numero_Calle]
            lista_validacion_str = [Nombre,Apellido_Paterno,Apellido_Materno,Calle]
            
            Valido = True
            Valido2 = True
            
            for a in lista_validacion_numerica:
                print(a)
                print(type(a))
                if a.isnumeric() == True:
                    print("Todo correcto",a)
                    
                elif a.isnumeric() == False:
                    msg = QMessageBox(self)
                    msg.setIcon(QMessageBox.Information)
                    msg.setText(a)
                    msg.setInformativeText("Introduzca un valor numérico")
                    msg.setWindowTitle("Error 102")
                    msg.show()
                    Valido = False
                    
            for b in lista_validacion_str:
                for space in b:
                    if space == " ": #If the word had spaces
                        b = b.replace(' ','')
                        
                if b.isalpha() == True:
                    print("Todo correcto en",b)
                    
                elif b.isalpha() == False:
                    msg = QMessageBox(self)
                    msg.setIcon(QMessageBox.Information)
                    msg.setText(b)
                    msg.setInformativeText("Introduzca un valor SIN numeros")
                    msg.setWindowTitle("Error 103")
                    msg.show()
                    Valido2 = False
                    
            print("TODOS LOS CAMPOS NUMERICOS",Valido)
            print("TODOS LOS CAMPOS DE TEXTO",Valido2)
            
            if Valido == True:
                if Valido2 == True:
                    # == Llamamos a la TABLA para su visualización ==
                    Alumnos.append(Alumno)
                    # == MYSQL INSERTAR DATOS ==
                    try:
                        mycursor = conexion.cursor()
                        mycursor.execute("USE Estudiantes")
                        sql = "INSERT INTO alumnos (Nombre,ApellidoPaterno,ApellidoMaterno, Matricula,Edad,Calle,Carrera,Estado,Municipio,Beca,Materias) VALUES (%s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s)"
                        val = [(Nombre, Apellido_Paterno, Apellido_Materno, Matricula, Edad, Calle, Carrera, Estado, Municipio,Porcentajereal,Materiadasreales)]
                        mycursor.executemany(sql, val)
                        conexion.commit()
                        print(mycursor.rowcount, "registro(s) fueron insertados.")
                        
                    except:
                        print("Errror104. Error datos ya insertados")   
            else:
                pass          
    # ====== Limpiar los datos que esten en Pantalla Principal =========
    def Limpiar_(self):
        # == Metodo para borrar los datos en ComboBox ==
        self.comboBoxMunicipio.setCurrentIndex(-1)
        self.comboBoxEstado.setCurrentIndex(-1)
        self.comboBoxCarrera.setCurrentIndex(-1)
        
        # == Ciclo para borrar los datos en los LineEdit ==
        for line in [self.lineEditNombre, self.lineEditApellido_Paterno,self.lineEditApellido_Materno,
                     self.lineEditMatricula,self.lineEditEdad,self.lineEditCalle,self.lineEditNumero_Calle]:
            line.clear()
        # == Ciclo para borrar los datos en los CheckBox ==
        for box in [self.Programacionbox,self.Contabilidadbox,self.Estadísticabox,
                    self.Basebox,self.Investigaciónbox]:
            box.setChecked(False)
        # == Ciclo para borrar los datos en los RadioButton ==
        for btn in [self.cerobtn, self.veinticincobtn, self.cincuentabtn, self.cienbtn]:
            btn.setAutoExclusive(False)
            btn.setChecked(False)
            btn.repaint()
            btn.setAutoExclusive(True)
            
# //////////// USUARIOS Y CLAVES ////////////
dicc = {'JuanPicon':['picon','juan']}

class ventanaLogin(QMainWindow):
    def __init__(self, parent=None):
        # ============= Diseño de Ventana Principal ==================
        super(ventanaLogin, self).__init__(parent)
        self.setWindowTitle("Proyecto Prototype")
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)
        self.setFixedSize(400, 300)
        paleta = QPalette()
        paleta.setColor(QPalette.Background, QColor('lightblue'))
        frame = QFrame(self)
        frame.setFrameShape(QFrame.NoFrame)
        frame.setFrameShadow(QFrame.Sunken)
        frame.setAutoFillBackground(True)
        frame.setPalette(paleta)
        frame.setFixedWidth(800)
        frame.setFixedHeight(70)
        frame.move(0, 0)
        fuenteTitulo = QFont()
        fuenteTitulo.setPointSize(25)
        fuenteTitulo.setBold(True)
        labelTitulo = QLabel("<font color='black'>¡Bienvenido al Proyecto!</font>", frame)
        labelTitulo.setFont(fuenteTitulo)
        labelTitulo.move(10, 15)
        
            # //////////// USUARIO ////////////
        labelUsuario = QLabel("Usuario", self)
        labelUsuario.move(60, 90)
        frameUsuario = QFrame(self)
        frameUsuario.setFrameShape(QFrame.StyledPanel)
        frameUsuario.setFixedWidth(280)
        frameUsuario.setFixedHeight(28)
        frameUsuario.move(60, 116)
        self.lineEditUsuario = QLineEdit(frameUsuario)
        self.lineEditUsuario.setFrame(False)
        self.lineEditUsuario.setTextMargins(8, 0, 4, 1)
        self.lineEditUsuario.setFixedWidth(238)
        self.lineEditUsuario.setFixedHeight(26)
        self.lineEditUsuario.move(40, 1)
        
        # //////////// CONTRASEÑA ////////////
        labelContraseña = QLabel("Contraseña", self)
        labelContraseña.move(60, 160)
        frameContraseña = QFrame(self)
        frameContraseña.setFrameShape(QFrame.StyledPanel)
        frameContraseña.setFixedWidth(280)
        frameContraseña.setFixedHeight(28)
        frameContraseña.move(60, 186)
        self.lineEditContraseña = QLineEdit(frameContraseña)
        self.lineEditContraseña.setFrame(False)
        self.lineEditContraseña.setTextMargins(8, 0, 4, 1)
        self.lineEditContraseña.setFixedWidth(238)
        self.lineEditContraseña.setFixedHeight(26)
        self.lineEditContraseña.move(40, 1)
        self.lineEditContraseña.setEchoMode(QLineEdit.Password)
        self.lineEditContraseña.setToolTip("Ingresar contraseña")
        
        # //////////// BOTON ////////////
        self.buttonMostrar = QPushButton("ADELANTE", self)
        self.buttonMostrar.setFixedWidth(135)
        self.buttonMostrar.setFixedHeight(28)
        self.buttonMostrar.move(130, 250)
        self.buttonMostrar.setToolTip("Ingresar")
        
        self.buttonRefrescar = QPushButton("", self)
        self.buttonRefrescar.setFixedWidth(30)
        self.buttonRefrescar.setFixedHeight(30)
        self.buttonRefrescar.move(340, 250)
        self.buttonRefrescar.setToolTip("Refrescar")
        self.imagenRefrescar = QLabel(self.buttonRefrescar)
        self.imagenRefrescar.setPixmap(QPixmap("Refresh.png").scaled(20, 20, Qt.KeepAspectRatio,
                                                                     Qt.SmoothTransformation))
        self.imagenRefrescar.move(5,5)
        
        self.las = [self.lineEditUsuario,self.lineEditContraseña]

         # //////////// OLVIDASTE CONTRASEÑA? ////////////
        labelInformacion = QLabel("<a href='https://paypal.me/piconmtz?locale.x=es_XC'>Forgot anwer?</a>", self)
        labelInformacion.setOpenExternalLinks(True)
        labelInformacion.setToolTip("Olvidaste tu contraseña?")
        labelInformacion.move(10, 260)
        
            # ======================== EVENTOS PARA BOTON =========================
        self.buttonMostrar.clicked.connect(self.ingresar)
        self.buttonRefrescar.clicked.connect(self.refrescar)
    
        # ======================= FUNCIONES PARA TABLA ============================
    def refrescar(self):
        for line in [self.lineEditUsuario,self.lineEditContraseña]:
            line.clear()
        print("Refrescado...")
    
    def abrirDialogo3(self):
        self.dialogo3.exec_()
        
    def ingresar(self):
        print("Ingresando...")
        _Usuario_ = self.lineEditUsuario.text()
        #print(_Usuario_)
        _Contraseña_ = self.lineEditContraseña.text()
        #print(_Contraseña_)
        usuario = None
        contraseña = None
        x = dicc.keys()
        y = dicc.values()
        
        c = len(_Usuario_)
        d = len(_Contraseña_)
        print(c)
        print(d)
        
        if c & d== 0:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Information)
            msg.setText("Ingreso Vacio")
            msg.setInformativeText("Introduzca un usuario y una contraseña valida")
            msg.setWindowTitle("Atención!")
            msg.show()
        else:
            for a in x:
                if _Usuario_ == a:
                    print("Usuario Correcto")
                    usuario = True
                else:
                    print("Usuario Incorrecto")
                    msg = QMessageBox(self)
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("USUARIO INCORRECTO")
                    msg.setInformativeText("Introduzca un usuario valido")
                    msg.setWindowTitle("Error 110")
                    msg.show()
                    usuario = False         
            for b in y:
                x = b    
            for e in x:          
                if e == _Contraseña_:
                    print("Contraseña correcto")
                    contraseña = True
                    break
                else:
                    contraseña = False
            if contraseña == False:
                print("Contraseña Incorrecto")
                msg = QMessageBox(self)
                msg.setIcon(QMessageBox.Information)
                msg.setText("CONTRASEÑA INCORRECTA")
                msg.setInformativeText("Introduzca una contraseña valida")
                msg.setWindowTitle("Error 111")
                msg.show()
                
            if usuario == True:
                if contraseña == True:
                    ventana.close()
                    self.dialogo3 = Dialogo3()
                    self.abrirDialogo3()
             
    def keyPressEvent(self, event):
        if event.key()==Qt.Key_Return:
            wfocus = QApplication.focusWidget() 
            if wfocus in self.las: 
                ix = self.las.index(wfocus) 
                if ix != len(self.las)-1:
                    self.las[ix+1].setFocus()
    
# =========== Iniciamos todo lo creado anteriormente ===========
if __name__ == '__main__':
    import sys
    aplicacion = QApplication(sys.argv)
    fuente = QFont()
    fuente.setPointSize(11)
    fuente.setFamily("Bahnschrift Light")
    aplicacion.setFont(fuente)
    ventana = ventanaLogin()
    ventana.show()
    sys.exit(aplicacion.exec_())