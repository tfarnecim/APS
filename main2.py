from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QLineEdit, QLabel

from usuario import Usuario
from sessao import Sessao
from filme import Filme
from funcionario import Funcionario
from bilhete import Bilhete

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
	
	cpf = TelaRegistroCliente.lineEdit.text()
	email = TelaRegistroCliente.lineEdit_2.text()
	senha   = TelaRegistroCliente.lineEdit_3.text()

	#1 Sucesso
	#2 Campo vazio
	#3 CPF inválido
	#4 Senha inválida
	#5 Email inválido
	#6 CPF já cadastrado

	if(cpf=="" or email=="" or senha==""):
		QMessageBox.about(TelaRegistroCliente, "Aviso", "Algum campo esta vazio!")
		return 2

	con = psycopg2.connect(database='Cinema', user='postgres', password='postgres')
	cur = con.cursor()
	cur.execute("select cpf from usuario where cpf='%s';"%(cpf))
	l = cur.fetchall()
	con.close()

	if(len(l) > 0):
		QMessageBox.about(TelaRegistroCliente, "Aviso", "CPF ja cadastrado")
		return 6

	if(len(cpf) != 11):
		QMessageBox.about(TelaRegistroCliente, "Aviso", "CPF invalido")
		return 3

	inv = False
	for i in cpf:
		if(not i.isdigit()):
			inv = True
			break

	if(inv):
		QMessageBox.about(TelaRegistroCliente, "Aviso", "CPF invalido")
		return 3

	if(len(senha) < 5 or len(senha) > 15):
		QMessageBox.about(TelaRegistroCliente, "Aviso", "Senha Invalida\n\nPara uma senha ser valida ela deve\nConter de 5 a 15 caracteres")
		return 4

	cnt = 0
	p = -1

	for i in range(len(email)):
		if(email[i]=='@'):
			cnt+=1
			p = i

	if(cnt!=1):
		QMessageBox.about(TelaRegistroCliente, "Aviso", "Email invalido")
		return 5

	if(p==0 or p==len(email)-1):
		QMessageBox.about(TelaRegistroCliente, "Aviso", "Email invalido")
		return 5

	con = psycopg2.connect(database='Cinema', user='postgres', password='postgres')
	cur = con.cursor()
	cur.execute("insert into usuario values('%s','%s','%s');"%(cpf,email,senha))
	con.commit()
	con.close()

	QMessageBox.about(TelaRegistroCliente, "Aviso", "Usuario cadastrado com Sucesso !!")

	TelaRegistroCliente.hide()
	TelaInicioCliente.show()

	c.SetCpf(Cpf)
	c.SetSenha(Senha)

	return 1


def LogarCliente():

	Cpf   = TelaLoginCliente.lineEdit.text()
	Senha = TelaLoginCliente.lineEdit_3.text()

	#1 Sucesso
	#2 Cpf não cadastrado
	#3 Senha errada

	con = psycopg2.connect(database='Cinema', user='postgres', password='postgres')
	cur = con.cursor()
	cur.execute("select cpf,senha,email from usuario where cpf='%s';"%(Cpf))
	l = cur.fetchall()
	con.close()

	if(len(l)==0):
		QMessageBox.about(TelaRegistroCliente, "Aviso", "Este CPF nao foi cadastrado")
		return 2

	if(Senha != l[0][1]):
		QMessageBox.about(TelaRegistroCliente, "Aviso", "Voce Digitou a senha errada")
		return 3

	c.SetCpf(Cpf)
	c.SetSenha(Senha)
	c.SetEmail(l[0][2])

	TelaLoginCliente.hide()
	TelaPrincipalCliente.label.setText(c.GetCpf())
	TelaPrincipalCliente.label_2.setText(c.GetEmail())
	TelaPrincipalCliente.show()

	return 1

def VoltaPrincipal():
	TelaPrincipalCliente.hide()
	TelaInicioCliente.show()

def CompraPrincipal():
	pass

def UsaPrincipal():
	pass

#cria a aplicação
app = QtWidgets.QApplication([])

#carrega todas as telas criadas
TelaInicioCliente     = uic.loadUi("Telas/TelaInicioCliente.ui")
TelaRegistroCliente   = uic.loadUi("Telas/TelaRegistroCliente.ui")
TelaLoginCliente      = uic.loadUi("Telas/TelaLoginCliente.ui")
TelaPrincipalCliente  = uic.loadUi("Telas/TelaPrincipalCliente.ui")

#explica aos botões quais funções devem ser acionadas ao serem clicados

TelaInicioCliente.pushButton.clicked.connect(RegistrarTelaInicio)
TelaInicioCliente.pushButton_2.clicked.connect(LoginTelaInicio)
TelaInicioCliente.pushButton_3.clicked.connect(Sair)

TelaRegistroCliente.pushButton.clicked.connect(RegistrarCliente)
TelaRegistroCliente.pushButton_2.clicked.connect(VoltaRegistro)

TelaLoginCliente.pushButton.clicked.connect(LogarCliente)
TelaLoginCliente.pushButton_2.clicked.connect(VoltaLogin)

TelaPrincipalCliente.pushButton.clicked.connect(CompraPrincipal)
TelaPrincipalCliente.pushButton_2.clicked.connect(UsaPrincipal)
TelaPrincipalCliente.pushButton_3.clicked.connect(VoltaPrincipal)

#cria o usuario que está usando o programa

c = Usuario("","","")

#chama a tela em que o programa deve começar
TelaInicioCliente.show()

#começa o programa
app.exec()
