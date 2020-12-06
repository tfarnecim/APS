class Usuario:

	def __init__(self, Cpf, Email, Senha):
		self.Cpf = Cpf
		self.Email = Email
		self.Senha = Senha

	def GetBilhetes(self):
		#Falta fazer
		pass

	def SetCpf(self, Cpf):
		self.Cpf = Cpf

	def GetCpf(self, Cpf):
		return self.Cpf

	def SetEmail(self, Email):
		self.Email = Email

	def GetEmail(self):
		return self.Email

	def SetSenha(self, Senha):
		self.Senha = Senha

	def GetSenha(self):
		return self.Senha

	
