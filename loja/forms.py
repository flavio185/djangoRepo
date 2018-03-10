from django import forms
from .models import Roupas

class RoupasForm(forms.ModelForm):
	class Meta:
		model = Roupas
		fields = ['codigo', 'nome', 'tipo', 'genero', 'data_inclusao', 'tamanho', 'valor_pago', 
					'valor_venda', 'estoque','imagem', 'imagem1', 'imagem2'] 

class AdicionaProdutoCarrinho(forms.Forms):
    quantidade = forms.IntegerField(widget=forms.TextInput(attrs={'size':'2',
        'value1:'1', 'class':'quantidade', 'maxlength':'5'}),
        error_messages={'invalid':'Favor colocar uma quantidade válida.'},
        min_value=1)
    codigo_produto = forms.CharField(widget=forms.HiddenInput())
    
    #override the default __init__ so we can set the request
    def __init__(self,request=None, *args, **kwargs):
        self.request = request
        super(AdicionaProdutoCarrinho, self).__init__(*args, **kwargs)
        
    # custom validation to check for cookies
    def clean(self):
        if not self.request.session.test_cookie_worked():
            raise forms.ValidationError("Cookies devem estar ativados.")
    return self.cleaned_data