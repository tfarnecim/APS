from usuario import Usuario
from sessao import Sessao

class Bilhete:
	
	def __init__(self, Id, Usuario, Sessao):
		self.Id = Id
		self.Usuario = Usuario
		self.Sessao = Sessao

	def GetId(self):
		return self.Id

	'''

	NAO FAZ SENTIDO

	def SetId(self, Id):
		self.Id = Id

	'''