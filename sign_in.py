def execute_signin():
    #Login created by Juan Picón
    from PyQt5.QtGui import QIcon, QPalette, QColor, QPixmap, QFont
    from PyQt5.QtCore import Qt
    from PyQt5.QtWidgets import (QApplication, QMainWindow, QFrame, QLabel, QLineEdit,QPushButton)
    # //////////// USUARIOS Y CLAVES ////////////
    dicc = {'JuanPicon':['picon','juan']}
    # //////////// VENTANA PRINCIPAL ////////////
    class VentanaPrincipal(QMainWindow):
        def __init__(self, parent=None):
            super(VentanaPrincipal, self).__init__(parent)
        
            # //////////// DISEÑO ////////////
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
            buttonMostrar = QPushButton("INGRESAR", self)
            buttonMostrar.setFixedWidth(135)
            buttonMostrar.setFixedHeight(28)
            buttonMostrar.move(130, 250)
            buttonMostrar.setToolTip("Ingresar")
        
            buttonRefrescar = QPushButton("", self)
            buttonRefrescar.setFixedWidth(30)
            buttonRefrescar.setFixedHeight(30)
            buttonRefrescar.move(340, 250)
            buttonRefrescar.setToolTip("Refrescar")
            imagenRefrescar = QLabel(buttonRefrescar)
            imagenRefrescar.setPixmap(QPixmap("Refresh.png").scaled(20, 20, Qt.KeepAspectRatio,
                                                                     Qt.SmoothTransformation))
            imagenRefrescar.move(5,5)

            # //////////// OLVIDASTE CONTRASEÑA? ////////////
            labelInformacion = QLabel("<a href='https://paypal.me/piconmtz?locale.x=es_XC'>Forgot anwer?</a>", self)
            labelInformacion.setOpenExternalLinks(True)
            labelInformacion.setToolTip("Olvidaste tu contraseña?")
            labelInformacion.move(10, 260)
        
            # ======================== EVENTOS PARA BOTON =========================
            buttonMostrar.clicked.connect(self.ingresar)
            buttonRefrescar.clicked.connect(self.refrescar)
    
        # ======================= FUNCIONES PARA TABLA ============================
        def refrescar(self):
            for line in [self.lineEditUsuario,self.lineEditContraseña]:
                line.clear()
            print("Refrescado...")
        
        def ingresar(self):
            print("Ingresando...")
            _Usuario_ = self.lineEditUsuario.text()
            #print(_Usuario_)
            _Contraseña_ = self.lineEditContraseña.text()
            #print(_Contraseña_)
        
            x = dicc.keys()
            y = dicc.values()
            for a in x:
                if _Usuario_ == a:
                    print("Usuario Correcto")
                else:
                    print("Usuario Incorrecto")   
            for b in y:
                x = b
            for e in x:
                print(e)
                if e == _Contraseña_:
                    print("Usuario correcto")
                    break
                else:
                    print("Usuario Incorrecto")
      
    if __name__ == '__main__':   
        import sys
        aplicacion = QApplication(sys.argv)
        fuente = QFont()
        fuente.setPointSize(11)
        fuente.setFamily("Bahnschrift Light")
        aplicacion.setFont(fuente)
        ventana = VentanaPrincipal()
        ventana.show()
        sys.exit(aplicacion.exec_())