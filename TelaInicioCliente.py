from PyQt5 import uic, QtWidgets
import time

def Sair():
	TelaInicioCliente.close()

def Registrar():
	TelaInicioCliente.hide()
	TelaRegistroCliente.show()

def Login():
	TelaInicioCliente.hide()
	TelaRegistroCliente.show()

#cria a aplicação
app = QtWidgets.QApplication([])

#carrega todas as telas criadas
TelaInicioCliente      = uic.loadUi("Telas/TelaInicioCliente.ui")
TelaRegistroCliente    = uic.loadUi("Telas/TelaInicioCliente.ui")
TelaLoginCliente       = uic.loadUi("Telas/TelaInicioCliente.ui")
TelaPrincipalCliente   = uic.loadUi("Telas/TelaInicioCliente.ui")

#explica aos botões quais funções devem ser acionadas ao serem clicados
Tela.pushButton_3.clicked.connect(Sair)


#chama a tela em que o programa deve começar
TelaInicioCliente.show()

#começa o programa
app.exec()
