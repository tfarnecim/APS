from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QLineEdit, QLabel
from PyQt5 import QtGui

from filme import Filme
from sessao import Sessao
from bilhete import Bilhete
from usuario import Usuario
from funcionario import Funcionario
import psycopg2
import os

#Inicio das User Stories do programa

def LoginRegistro():
	TelaLoginFuncionario.hide()
	TelaRegistroFuncionario.show()

def RegistroLogin():
	TelaRegistroFuncionario.hide()
	TelaLoginFuncionario.show()

def Logar():
	pass

def Cadastro():

	cpf = TelaRegistroFuncionario.lineEdit.text()
	senha   = TelaRegistroFuncionario.lineEdit_2.text()

	#1 Sucesso
	#2 Campo vazio
	#3 CPF inválido
	#4 Senha inválida
	#5 CPF já cadastrado

	if(cpf=="" or senha==""):
		QMessageBox.about(TelaRegistroFuncionario, "Aviso", "Algum campo esta vazio!")

	con = psycopg2.connect(database='Cinema', user='postgres', password='postgres')
	cur = con.cursor()
	cur.execute("select cpf from funcionario where cpf='%s';"%(cpf))
	l = cur.fetchall()
	con.close()

	if(len(l) > 0):
		QMessageBox.about(TelaRegistroFuncionario, "Aviso", "CPF já cadastrado!")

	if(len(cpf) != 11):
		QMessageBox.about(TelaRegistroFuncionario, "Aviso", "CPF inválido")

	inv = False
	for i in cpf:
		if(not i.isdigit()):
			inv = True
			break

	if(inv):
		QMessageBox.about(TelaRegistroFuncionario, "Aviso", "CPF inválido")

	if(len(senha) < 5 or len(senha) > 15):
		QMessageBox.about(TelaRegistroFuncionario, "Aviso", "Senha inválida")

	con = psycopg2.connect(database='Cinema', user='postgres', password='postgres')
	cur = con.cursor()
	cur.execute("insert into funcionario values('%s','%s');"%(cpf,senha))
	con.commit()
	con.close()

	QMessageBox.about(TelaRegistroFuncionario, "Aviso", "Funcionario Cadastrado com sucesso!")
	TelaRegistroFuncionario.hide()
	TelaLoginFuncionario.show()

	return 1


#cria a aplicação
app = QtWidgets.QApplication([])

#carrega todas as telas criadas
TelaLoginFuncionario     = uic.loadUi("Telas/TelaLoginFuncionario.ui")
TelaRegistroFuncionario   = uic.loadUi("Telas/TelaRegistroFuncionario.ui")

#explica aos botões quais funções devem ser acionadas ao serem clicados
TelaRegistroFuncionario.pushButton.clicked.connect(Cadastro)
TelaRegistroFuncionario.pushButton_2.clicked.connect(RegistroLogin)

TelaLoginFuncionario.pushButton.clicked.connect(LoginRegistro)
TelaLoginFuncionario.pushButton_2.clicked.connect(Logar)

#cria o usuario que está usando o programa
f = Funcionario("","")

#chama a tela em que o programa deve começar
TelaLoginFuncionario.show()

#começa o programa
app.exec()
