from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Todo
from django.http import HttpResponseRedirect

import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize, word_tokenize, RegexpTokenizer


class IndexView(generic.ListView):
    template_name = 'todos/index.html'
    context_object_name = 'todo_list'

    def get_queryset(self):
        """Return all the latest todos."""
        return Todo.objects.order_by('-created_at')

def add(request):
    given_text = request.POST['title']
    title = "Sentences count: -->| " + str(len(sent_tokenize(given_text))) + " |<-- | Words count: -->| " + str(len(RegexpTokenizer(r'\w+').tokenize(given_text))) + " |<-- | All Words: " + str(RegexpTokenizer(r'\w+').tokenize(given_text))
    Todo.objects.create(title=title)

    return redirect('todos:index')

def delete(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.delete()

    return redirect('todos:index')

def update(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    isCompleted = request.POST.get('isCompleted', False)
    if isCompleted == 'on':
        isCompleted = True
    
    todo.isCompleted = isCompleted

    todo.save()
    return redirect('todos:index')