from .models import Todo, Comment
from .forms import TodoForm, CommentForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST, require_safe

# Create your views here.
@require_safe
def index(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos,
    }
    return render(request, 'todos/index.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def new(request):
    if request.method == 'POST':
        form = TodoForm(request.POST) 
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo = form.save()
            return redirect('todos:index')
    else:
        form = TodoForm()
    # print(form.errors)
    context = {
        'form': form,
    }
    return render(request, 'todos/new.html', context)


@require_safe
def detail(request, pk):
    todo = Todo.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = todo.comments.all()
    context = {
        'todo': todo,
        'comment_form' : comment_form,
        'comments': comments,
    }
    return render(request, 'todos/detail.html', context)


@require_POST
def delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    if request.user.is_authenticated:
        if request.user == todo.user:
            todo.delete()
            return redirect('todos:index')
    return redirect('todos:detail', todo.pk)


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    todo = Todo.objects.get(pk=pk)
    if request.user == todo.user:
        if request.method == 'POST':
            form = TodoForm(request.POST, instance=todo)
            if form.is_valid():
                form.save()
                return redirect('todos:detail', todo.pk)
        else:
            form = TodoForm(instance=todo)
    else:
        return redirect('todos:indexl')
    context = {
        'todo': todo,
        'form': form,
    }
    return render(request, 'todos/update.html', context)


def comments_create(request, pk):
    todo = Todo.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.todo = todo
        comment_form.save()
    return redirect('todos:detail', todo.pk)


def comments_delete(request, todo_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('todos:detail', todo_pk)


