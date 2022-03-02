from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy

from core.paginas.models import *
from core.paginas.forms import *

# Create your views here.
class ListFormPaginas(ListView):

    model = Paginas
    template_name = 'list_page.html'

    #mantener Datos
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['title']='Listado de Productos'
        return context

class CreateFormPage(CreateView):
    model = Paginas
    form_class=paginaForm
    template_name='create_page.html'
    success_url=reverse_lazy('list_page')

    def post(self, request, *args, **kwargs):
        form = paginaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.success_url)
        self.object = None
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return super().post(request, self.template_name, context)
    
    def get_context_data(self, **kwargs) :
            context = super().get_context_data(**kwargs)
            context['title1']="Creacion de paginas"
            return context


class UpdateFormPage(UpdateView):
    model=Paginas
    form_class = paginaForm
    template_name='create_page.html'
    success_url = reverse_lazy('list_page')

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['title']="Editar Pagina"
        return context

class DeleteFormPage(DeleteView):
    model=Paginas
    form_class = paginaForm
    template_name='delete_page.html'
    success_url = reverse_lazy('list_page')

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['title1']="Eliminar pagina"
        return context