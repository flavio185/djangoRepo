from django.db import models
from django.utils.timezone import now

# Create your models here.
	
#Method to create autoincrement id for boats.
def auto_increment_roupa_id():
	try:
		last_roupa = Roupas.objects.all().order_by('codigo').last().codigo
		roupa_id = int(last_roupa)+1
		roupa_id = str(roupa_id).zfill(4)
	except Exception as e:
		roupa_id = '0001'
	
	return roupa_id

ESCOLHA_GENERO = (
    ('Feminino', 'FEMININO'),
    ('Masculino','MASCULINO'),
    ('Unisex','UNISEX'),
)

class Roupas(models.Model):
	#owner = models.ForeignKey('cliente.Cliente', related_name='embarcacao')
	codigo = models.CharField(max_length=10, default=auto_increment_roupa_id)
	nome = models.CharField(max_length=70)
	tipo = models.CharField(max_length=70)
	genero = models.CharField(max_length=10, choices=ESCOLHA_GENERO)
	data_inclusao = models.DateTimeField(blank=True, null=True)
	tamanho = models.CharField(max_length=10, blank=True, null=True)
	valor_pago = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
	valor_venda = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
	estoque = models.IntegerField(blank=True, null=True, default=1)
	imagem = models.FileField( upload_to='imagens_roupas', blank=True,)
	imagem1 = models.FileField( upload_to='imagens_roupas', blank=True,)
	imagem2 = models.FileField( upload_to='imagens_roupas', blank=True,)

	#methods
	def __str__(self):
		return self.nome

	#what todo after saving
	def save(self, *args, **kwargs):
		if (self.data_inclusao is None):
			self.data_inclusao = now()
		#captalize: deixa primeira letra maiuscula
		for field_name in ['nome', 'tipo' ]:
			val = getattr(self, field_name, False)
			if val:
				setattr(self, field_name, val.capitalize())
		#upper(): deixa todas as letras maiusculas.
		for field_name in [ 'tamanho' ]:
                        val = getattr(self, field_name, False)
                        if val:
                                setattr(self, field_name, val.upper())
		#important to call superclass method.
		#If you want the method to be called after is saved,
		#add yoiur lines after super method call
		super(Roupas, self).save(*args, **kwargs)


	def image_url(self):
		"""
		Returns the URL of the image associated with this Object.
		If an image hasn't been uploaded yet, it returns a stock image

		:returns: str -- the image url

		"""
		if self.imagem and hasattr(self.imagem, 'url'):
			return self.imagem.url           
		else:
			return '/static/images/sample.jpg'

	def image1_url(self):
		if self.imagem1 and hasattr(self.imagem1, 'url'):
			return self.imagem1.url
		else:
			return '/static/images/sample.jpg'

	def image2_url(self):
		if self.imagem2 and hasattr(self.imagem2, 'url'):
			return self.imagem2.url
		else:
			return '/static/images/sample.jpg'

