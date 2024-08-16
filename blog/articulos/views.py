from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import get_object_or_404
from .models import Entry, Comment
from .forms import CommentForm

class EntryListView(ListView):
    model = Entry
    template_name = 'blog/index.html'
    context_object_name = 'entries'

class EntryDetailView(DetailView):
    model = Entry
    template_name = 'blog/detail.html'
    context_object_name = 'entry'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['comments'] = self.object.comments.filter(active=True)
        return context



class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/add_comment.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = get_object_or_404(Entry, id=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.post.get_absolute_url()
    
    
# Create your views here.
