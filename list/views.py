from django.shortcuts import render
from django.utils import timezone
from .models import Todo

# Create your views here.
def todo_list(request):
    todos = Todo.objects.filter(deadline_date__lte=timezone.now()).order_by('deadline_date')
    return render(request, 'list/todo_list.html', {'todos': todos})