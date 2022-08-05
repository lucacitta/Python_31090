from django.views.generic import ListView, DetailView, CreateView, DeleteView

from django.shortcuts import render
from blog.models import Articles

class List_articles(ListView):
    model = Articles
    template_name = 'articles/list_articles.html'

class Detail_article(DetailView):
    model = Articles
    template_name = 'articles/detail_articles.html'

class Create_article(CreateView):
    model = Articles
    template_name = 'articles/create_article.html'
    fields = '__all__'
    success_url = '/articles/list-articles/'

class Delete_article(DeleteView):
    model = Articles
    template_name = 'articles/delete_article.html'
    success_url = '/articles/list-articles/'













def create_article(request):
    new_article = Articles.objects.create(
        title = 'Bajo el Bitcoin', 
        description = 'Esta bajisimo, desesperen o salgan a comprar mas', 
        author = 'Jose Ignacio Tessio'
        )
    context = {
        'new_article':new_article
    }
    return render(request, 'articles/new_article.html', context=context)

