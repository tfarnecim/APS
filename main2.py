from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import psycopg2

def Sair():
	TelaInicioCliente.close()

def RegistrarTelaInicio():
	TelaInicioCliente.hide()
	TelaRegistroCliente.show()

def LoginTelaInicio():
	TelaInicioCliente.hide()
	TelaLoginCliente.show()

def VoltaRegistro():
	TelaRegistroCliente.hide()
	TelaInicioCliente.show()

def VoltaLogin():
	TelaLoginCliente.hide()
	TelaInicioCliente.show()

def RegistrarCliente():
	QMessageBox.about(TelaRegistroCliente, "Aviso", "Isso aqui ainda nao funciona")

def LogarCliente():
	QMessageBox.about(TelaRegistroCliente, "Aviso", "Isso aqui tambem ainda nao funciona")

#cria a aplicação
app = QtWidgets.QApplication([])

#carrega todas as telas criadas
TelaInicioCliente      = uic.loadUi("Telas/TelaInicioCliente.ui")
TelaRegistroCliente    = uic.loadUi("Telas/TelaRegistroCliente.ui")
TelaLoginCliente       = uic.loadUi("Telas/TelaLoginCliente.ui")
TelaPrincipalCliente   = uic.loadUi("Telas/TelaPrincipalCliente.ui")

#explica aos botões quais funções devem ser acionadas ao serem clicados

TelaInicioCliente.pushButton.clicked.connect(RegistrarTelaInicio)
TelaInicioCliente.pushButton_2.clicked.connect(LoginTelaInicio)
TelaInicioCliente.pushButton_3.clicked.connect(Sair)

TelaRegistroCliente.pushButton.clicked.connect(RegistrarCliente)
TelaRegistroCliente.pushButton_2.clicked.connect(VoltaRegistro)

TelaLoginCliente.pushButton.clicked.connect(LogarCliente)
TelaLoginCliente.pushButton_2.clicked.connect(VoltaLogin)

#chama a tela em que o programa deve começar
TelaInicioCliente.show()

#começa o programa
app.exec()
