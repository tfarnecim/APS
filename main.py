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

def Cadastro(cpf,email,senha):

	#1 Sucesso
	#2 Campo vazio
	#3 CPF inválido
	#4 Senha inválida
	#5 Email inválido
	#6 CPF já cadastrado

	if(cpf=="" or email=="" or senha==""):
		return 2

	con = psycopg2.connect(database='Cinema', user='postgres', password='postgres')
	cur = con.cursor()
	cur.execute("select cpf from usuario where cpf='%s';"%(cpf))
	l = cur.fetchall()
	con.close()

	if(len(l) > 0):
		return 6

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

	cnt = 0
	p = -1

	for i in range(len(email)):
		if(email[i]=='@'):
			cnt+=1
			p = i

	if(cnt!=1):
		return 5

	if(p==0 or p==len(email)-1):
		return 5

	con = psycopg2.connect(database='Cinema', user='postgres', password='postgres')
	cur = con.cursor()
	cur.execute("insert into usuario values('%s','%s','%s');"%(cpf,email,senha))
	con.commit()
	con.close()

	return 1

def Login(Cpf, Senha):
	
	#1 Sucesso
	#2 Cpf não cadastrado
	#3 Senha errada

	con = psycopg2.connect(database='Cinema', user='postgres', password='postgres')
	cur = con.cursor()
	cur.execute("select cpf,senha from usuario where cpf='%s';"%(Cpf))
	l = cur.fetchall()
	con.close()

	if(len(l)==0):
		return 2

	if(Senha != l[0][1]):
		return 3

	return 1	


#Fim das User Stories do programa

#O Código do funcionamento do programa começa aqui

menu1 = 0

while(menu1!=3):

	os.system('cls')

	print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
	print("|                                 |")
	print("|        CINEMA CIDADE LUZ        |")
	print("|                                 |")
	print("|        [1]Registrar             |")
	print("|        [2]Login                 |")
	print("|        [3]Sair                  |")
	print("|                                 |")
	print("|                                 |")
	print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
	menu1 = int(input())

	if(menu1 == 1):#caso o usuario deseje se registrar

		menu2 = 0

		Log = [
			"",
			"Usuario Cadastrado",
			"Campo vazio",
			"CPF inválido",
			"Senha inválida (senhas devem conter de 5 a 15 caracteres)",
			"Email inválido",
			"CPF já cadastrado"
		]
		
		volta = False

		while(menu2 != 1):

			cpf = ""
			email = ""
			senha = ""

			os.system("cls")
			cpf = input("Digite seu CPF: ")
			email = input("Digite seu EMAIL: ")
			senha = input("Digite sua nova SENHA: ")

			menu2 = Cadastro(cpf,email,senha)
			print("\nLOG: %s"%(Log[menu2]))

			if(menu2!=1):
				print("\nDeseja retornar ao menu principal?\n[1]Sim\n[2]Nao\n")
				menu2 = int(input())
				if(menu2==1):
					volta = True
					break
			else:
				os.system("pause")

		if(volta == True):		
			continue


	if(menu1 == 2):#caso o usuario deseje logar
		
		menu2 = 0

		Log = [
			"",
			"Login efetuado com sucesso",
			"CPF não cadastrado",
			"Senha errada"
		]

		volta = False 

		while(menu2 != 1):

			cpf = ""
			senha = ""

			os.system("cls")

			cpf = input("Digite seu CPF: ")			
			senha = input("Digite sua SENHA: ")

			menu2 = Login(cpf,senha)
			
			print("\nLOG: %s"%(Log[menu2]))

			if(menu2!=1):
				print("\nDeseja retornar ao menu principal?\n[1]Sim\n[2]Nao\n")
				menu2 = int(input())
				if(menu2==1):
					volta = True
					break
			else:
				os.system("pause")

		os.system("cls")

		if(volta == True):
			continue

		print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
		print("|                                 |")
		print("|        CINEMA CIDADE LUZ        |")
		print("|                                 |")
		print("|        [1]Comprar filmes        |")
		print("|        [2]Usar bilhete          |")
		print("|        [3]Voltar                |")
		print("|                                 |")
		print("|                                 |")
		print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
		menu1 = int(input())

		while(1):
			pass

os.system("cls")
