from django.views.generic import UpdateView, DeleteView, CreateView
from django.shortcuts import get_object_or_404
from .models import Entry, Comment
from .forms import CommentForm
from django.urls import reverse_lazy
from articulos.forms import EntryForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class EntryListView(ListView):
    model = Entry
    template_name = 'entry_list.html'
    context_object_name = 'entries'
    paginate_by = 10  

class EntryDetailView(DetailView):
    model = Entry
    template_name = 'entry_detail.html'
    context_object_name = 'entry'

class EntryCreateView(CreateView):
    model = Entry
    form_class = EntryForm
    template_name = 'create_entry.html'
    success_url = reverse_lazy('entry_list') 

class EntryUpdateView(UpdateView):
    model = Entry
    form_class = EntryForm
    template_name = 'update_entry.html'
    success_url = reverse_lazy('entry_list')

class EntryDeleteView(DeleteView):
    model = Entry
    template_name = 'delete_entry.html'
    success_url = reverse_lazy('entry_list')

#Comentarios

class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'create_comment.html'
    success_url = reverse_lazy('entry_list')  # Redirige a la lista de entradas o a donde prefieras

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'update_comment.html'
    success_url = reverse_lazy('entry_list')

class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'delete_comment.html'
    success_url = reverse_lazy('entry_list')
    
# Create your views here.
