
class Botao():
	# FALTA ENCAPSULAR
	def __init__(self, imagem, x_pos, y_pos, mensagem, fonte, cor_base_texto, cor_mouse):
		self.imagem = imagem
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.mensagem = mensagem
		self.fonte_texto = fonte
		self.cor_base_texto = cor_base_texto
		self.cor_mouse = cor_mouse
		self.text = self.fonte_texto.render(self.mensagem, True, self.cor_base_texto)
		if self.imagem is None:   # caso não tenha imagem, cria um botão apenas do texto
			self.imagem = self.mensagem
		self.rect = self.imagem.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, tela):
		if self.imagem is not None:
			tela.blit(self.imagem, self.rect)
		tela.blit(self.text, self.text_rect)

	'''
	Verifica se o mouse está dentro do botão e retorna True caso esteja
	Serve para detectar o clique e executar uma função destinada ao botão
	'''
	def detecta_mouse(self, posicao):
		if posicao[0] in range(self.rect.left, self.rect.right) and posicao[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	'''
	Mesma funcionalidade da função acima, porém é feita para rodar sempre
	no loop principal para mudar a cor do texto caso o mouse esteja sobre o botão
	'''
	def muda_cor(self, posicao):
		if posicao[0] in range(self.rect.left, self.rect.right) and posicao[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.fonte_texto.render(self.mensagem, True, self.cor_mouse)
		else:
			self.text = self.fonte_texto.render(self.mensagem, True, self.cor_base_texto)