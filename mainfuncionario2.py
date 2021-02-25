from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QLineEdit, QLabel, QListWidget, QTableWidgetItem
from PyQt5 import QtGui

import PyQt5

from filme import Filme
from sessao import Sessao
from bilhete import Bilhete
from usuario import Usuario
from funcionario import Funcionario
import psycopg2
import os

#Inicio das User Stories do programa

def AdicionarSessao():

	data = TelaAdicionarSessao.calendarWidget.selectedDate()
	
	dia = data.day()
	mes = data.month()
	ano = data.year()

	ok = True

	numsala = TelaAdicionarSessao.lineEdit_4.text()
	iniciohora  = TelaAdicionarSessao.lineEdit_5.text()
	iniciominuto = TelaAdicionarSessao.lineEdit_6.text()

	for caractere in numsala:
		if(not caractere.isdigit()):
			ok = False
			break

	if(not ok):
		QMessageBox.about(TelaAdicionarSessao, "Aviso", "No campo 'número da sala', apenas são aceitos números")
		return 1

	for caractere in iniciohora:
		if(not caractere.isdigit()):
			ok = False
			break

	if(not ok):
		QMessageBox.about(TelaAdicionarSessao, "Aviso", "No campo 'horário de início(horas)', apenas são aceitos números no intervalo [0,23]")
		return 1

	for caractere in iniciominuto:
		if(not caractere.isdigit()):
			ok = False
			break

	if(not ok):
		QMessageBox.about(TelaAdicionarSessao, "Aviso", "No campo 'horário de início(minutos)', apenas são aceitos números no intervalo [0,59]")
		return 1

	NUMSALA = int(numsala)
	INICIOHORA  = int(iniciohora)
	INICIOMINUTO = int(iniciohora)

	if(INICIOHORA > 23):
		QMessageBox.about(TelaAdicionarSessao, "Aviso", "No campo 'horário de início(horas)', apenas são aceitos números no intervalo [0,23]")
		return 1

	if(INICIOMINUTO > 59):
		QMessageBox.about(TelaAdicionarSessao, "Aviso", "No campo 'horário de início(minutos)', apenas são aceitos números no intervalo [0,59]")
		return 1

	ultimaposicao = TelaAdicionarFilme.tableWidget.rowCount()
	TelaAdicionarFilme.tableWidget.insertRow(ultimaposicao)

	TelaAdicionarFilme.tableWidget.setItem(ultimaposicao, 0, QtWidgets.QTableWidgetItem(str(dia)+'/'+str(mes)+'/'+str(ano)))
	TelaAdicionarFilme.tableWidget.setItem(ultimaposicao, 1, QtWidgets.QTableWidgetItem(str(INICIOHORA)+':'+str(INICIOMINUTO)))
	TelaAdicionarFilme.tableWidget.setItem(ultimaposicao, 2, QtWidgets.QTableWidgetItem(str(NUMSALA)))

	QMessageBox.about(TelaAdicionarSessao, "Aviso", "Sessão adicionada com sucesso!")

	TelaAdicionarSessao.hide()

def RemoverSessao():
	return 1

def AdicionarsAdicionarf():
	TelaAdicionarSessao.hide()

def AdicionarfAdicionars():
	TelaAdicionarSessao.show()

def PrincipalAdicionar():
	TelaPrincipalFuncionario.hide()
	TelaAdicionarFilme.show()

def PrincipalRemover():
	TelaPrincipalFuncionario.hide()
	TelaRemoverFilme.show()


def RemoverPrincipal():
	TelaRemoverFilme.hide()
	TelaPrincipalFuncionario.show()

def AdicionarPrincipal():
	TelaAdicionarFilme.hide()
	TelaPrincipalFuncionario.show()

def LoginRegistro():
	TelaLoginFuncionario.hide()
	TelaRegistroFuncionario.show()

def RegistroLogin():
	TelaRegistroFuncionario.hide()
	TelaLoginFuncionario.show()

def Logar():

	Cpf   = TelaLoginFuncionario.lineEdit.text()
	Senha = TelaLoginFuncionario.lineEdit_2.text()

	#1 Sucesso
	#2 Cpf não cadastrado
	#3 Senha errada

	con = psycopg2.connect(database='Cinema', user='postgres', password='postgres')
	cur = con.cursor()
	cur.execute("select cpf,senha from funcionario where cpf='%s';"%(Cpf))
	l = cur.fetchall()
	con.close()

	if(len(l)==0):
		QMessageBox.about(TelaLoginFuncionario, "Aviso", "Este CPF nao foi cadastrado")
		return 2

	if(Senha != l[0][1]):
		QMessageBox.about(TelaLoginFuncionario, "Aviso", "Voce digitou a senha errada")
		return 3

	f.SetCpf(Cpf)
	f.SetSenha(Senha)

	TelaLoginFuncionario.hide()
	TelaPrincipalFuncionario.show()

	return 1

def Cadastro():

	cpf   = TelaRegistroFuncionario.lineEdit.text()
	senha = TelaRegistroFuncionario.lineEdit_2.text()

	#1 Sucesso
	#2 Campo vazio
	#3 CPF inválido
	#4 Senha inválida
	#5 CPF já cadastrado

	if(cpf=="" or senha==""):
		QMessageBox.about(TelaRegistroFuncionario, "Aviso", "Algum campo esta vazio!")
		return 2

	con = psycopg2.connect(database='Cinema', user='postgres', password='postgres')
	cur = con.cursor()
	cur.execute("select cpf from funcionario where cpf='%s';"%(cpf))
	l = cur.fetchall()
	con.close()

	if(len(l) > 0):
		QMessageBox.about(TelaRegistroFuncionario, "Aviso", "CPF já cadastrado!")
		return 5

	if(len(cpf) != 11):
		QMessageBox.about(TelaRegistroFuncionario, "Aviso", "CPF inválido")
		return 3

	inv = False
	for i in cpf:
		if(not i.isdigit()):
			inv = True
			break

	if(inv):
		QMessageBox.about(TelaRegistroFuncionario, "Aviso", "CPF inválido")
		return 3

	if(len(senha) < 5 or len(senha) > 15):
		QMessageBox.about(TelaRegistroFuncionario, "Aviso", "Senha inválida")
		return 4

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
TelaRegistroFuncionario  = uic.loadUi("Telas/TelaRegistroFuncionario.ui")
TelaPrincipalFuncionario = uic.loadUi("Telas/TelaPrincipalFuncionario.ui")
TelaAdicionarFilme       = uic.loadUi("Telas/TelaAdicionarFilme.ui")
TelaRemoverFilme         = uic.loadUi("Telas/TelaRemoverFilme.ui")
TelaAdicionarSessao      = uic.loadUi("Telas/TelaAdicionarSessao.ui")

#explica aos botões quais funções devem ser acionadas ao serem clicados
TelaRegistroFuncionario.pushButton.clicked.connect(Cadastro)
TelaRegistroFuncionario.pushButton_2.clicked.connect(RegistroLogin)

TelaLoginFuncionario.pushButton.clicked.connect(LoginRegistro)
TelaLoginFuncionario.pushButton_2.clicked.connect(Logar)

TelaPrincipalFuncionario.pushButton.clicked.connect(PrincipalAdicionar)  
TelaPrincipalFuncionario.pushButton_2.clicked.connect(PrincipalRemover)

TelaAdicionarFilme.pushButton.clicked.connect(AdicionarPrincipal)
TelaAdicionarFilme.pushButton_2.clicked.connect(AdicionarfAdicionars)
TelaAdicionarFilme.pushButton_4.clicked.connect(RemoverSessao)

TelaAdicionarSessao.pushButton.clicked.connect(AdicionarsAdicionarf)
TelaAdicionarSessao.pushButton_2.clicked.connect(AdicionarSessao)

TelaRemoverFilme.pushButton.clicked.connect(RemoverPrincipal)

#cria o usuario que está usando o programa
f = Funcionario("","")

#chama a tela em que o programa deve começar
TelaLoginFuncionario.show()

#começa o programa
app.exec()
