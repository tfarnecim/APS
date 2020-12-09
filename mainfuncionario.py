'''

© All rights reserved to GuaraTec

'''

from filme import Filme
from sessao import Sessao
from bilhete import Bilhete
from usuario import Usuario
from funcionario import Funcionario
import psycopg2
import os

#Inicio das User Stories do programa

def Cadastro(cpf,senha):

	#1 Sucesso
	#2 Campo vazio
	#3 CPF inválido
	#4 Senha inválida
	#5 CPF já cadastrado

	if(cpf=="" or senha==""):
		return 2

	con = psycopg2.connect(database='Cinema', user='postgres', password='postgres')
	cur = con.cursor()
	cur.execute("select cpf from funcionario where cpf='%s';"%(cpf))
	l = cur.fetchall()
	con.close()

	if(len(l) > 0):
		return 5

	if(len(cpf) != 11):
		return 3

	inv = False
	for i in cpf:
		if(not i.isdigit()):
			inv = True
			break

	if(inv):
		return 3

	if(len(senha) < 5 or len(senha) > 15):
		return 4

	con = psycopg2.connect(database='Cinema', user='postgres', password='postgres')
	cur = con.cursor()
	cur.execute("insert into funcionario values('%s','%s');"%(cpf,senha))
	con.commit()
	con.close()

	return 1

#Fim das User Stories do programa

#O Código do funcionamento do programa começa aqui


