from django.shortcuts import redirect, render, reverse, get_object_or_404
from loja.models import Roupas 
from loja.forms import RoupasForm
from django.views.generic import View

from django.views.generic.edit import CreateView

# Create your views here.

class ViewLoja(View):

    def get(self, request):
        """
        List the books that have reviews
        """
        roupas = Roupas.objects.all()
        query = request.GET.get("q")
        if query:
            roupas = roupas.filter(codigo__icontains=query)
        #roupas = Roupas.objects.exclude(date_reviewed__isnull=True).prefetch_related('authors')
        
    
        context = {
            'roupas': roupas,
        }
        return render(request, "loja.html", context)
        
    def post(self, request):
        form = RoupasForm(request.POST)
        roupas = Roupas.objects.all()
        
        if form.is_valid():
            cart = request.session.get('cart', {})
            cart[peca.codigo] = request.POST['quantidade']
            request.session['cart'] = cart
            return redirect('view_carrinho')
            
        context = {
            'form': form,
            'roupas': roupas,
        }
        
        return render(request, "loja.html", context)


def view_carrinho(request):
    cart = request.session.get('cart', {})
    # rest of the view
    context = {'cart': cart,}
    return render(request, "view-carrinho.html", context)

    
def view_peca(request, pk):
    """
    Review an individual book
    """
    peca = get_object_or_404(Roupas, pk=pk)
    
    if request.method == 'POST':
        # Process our form
        form = RoupasForm(request.POST, request.FILES, instance=peca)
        
        if form.is_valid():
            #book.is_favourite = form.cleaned_data['is_favourite']
            #book.review = form.cleaned_data['review']
            #book.reviewed_by = request.user
            peca.save()
            
            return redirect('loja:home')
        
    else:
        form = RoupasForm(instance=peca)
    
    context = {
        'peca': peca,
        'form': form,
    }
    
    return render(request, "edita-pecas.html", context)
    

class CreateRoupas(CreateView):
    model = Roupas
    fields = ['codigo', 'nome', 'tipo', 'genero', 'data_inclusao', 'tamanho', 'valor_pago', 
                    'valor_venda', 'estoque', 'imagem', 'imagem1', 'imagem2']
    template_name = "adiciona-pecas.html"
    
    def get_success_url(self):
        return reverse('loja:home')

class CreateImage(CreateView):
    model = Roupas
    fields = [ 'imagem' ]
    template_name = "adiciona-imagem.html"
    
    def get_success_url(self):
        return reverse('loja:home')

