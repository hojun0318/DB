# ❖ Todo App Project
### 아래 명세를 만족하는 Todo App을 제작하시오.

# ❖ Model
### 아래 ERD를 참고하여 todo 테이블을 정의한다.

# ❖ 필수 조건
​• User 모델은 django의 내장 User 모델을 대체하여 사용한다.

## 1. 회원가입

![1  회원가입](https://user-images.githubusercontent.com/104968672/194264774-7e0bddb9-f1d9-42e1-835c-95b506028a11.JPG)

```
{% extends 'base.html' %}

{% block content %}
<h1>Sign Up</h1>
<form action="{% url 'accounts:signup' %}" method="POST">
  {% csrf_token %}
  {{ form.as_p }}
  <input type="submit" value="SignUp!">
</form>
{% endblock content %}
```
## 2. 로그인

![2  로그인](https://user-images.githubusercontent.com/104968672/194264806-be4acd7a-3a27-43dd-8d9b-a94bd0691d51.JPG)

```
{% extends 'base.html' %}

{% block content %}
  <h1>Login</h1>
  <form action="" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="login">
  </form>
  <a href="{% url 'accounts:signup' %}">Signup</a>
{% endblock content %}

```
## 3. Todo 목록 (index)

![3  Todo 목록(index)](https://user-images.githubusercontent.com/104968672/194262656-c5183dcd-8ee3-496d-a990-7bccc9c858da.JPG)

```
{% extends 'base.html' %}

{% block content %}
<br>
  <h1>INDEX</h1>
  {% if request.user.is_authenticated %}
    <a href="{% url 'todos:new' %}">NEW</a>
  {% else %}
    <a href="{% url 'accounts:login' %}">NEW</a>
  {% endif %}
  <hr>
  {% for todo in todos %}
    <h2>{{ todo.title }}</h2>
    <p>작성자 : {{ todo.user }}</p>
    <p>완료여부: {{ todo.completed }}</p>
    <a href="{% url 'todos:detail' todo.pk %}">[detail]</a>
    <hr>
  {% endfor %}
{% endblock content %}

```
## 4. Todo 생성 (new)

![4  Todo 생성(new)](https://user-images.githubusercontent.com/104968672/194262687-0e6920b3-9e2a-42f5-a9ba-aa006d6d9c09.JPG)

```
{% extends 'base.html' %}

{% block content %}
  <h1>NEW</h1>
  <form action="" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="New">
  </form>
  <hr>
  <a href="{% url 'todos:index' %}">[back]</a>
{% endblock content %}

```

```
#todos/views.py
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
```

```
# todos/models.py
from django.db import models
from django.conf import settings
# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    completed = models.BooleanField()
```